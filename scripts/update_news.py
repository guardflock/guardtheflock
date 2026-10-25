#!/usr/bin/env python3
"""Build a safe, static JSON snapshot from the configured public RSS feeds."""

from __future__ import annotations

import concurrent.futures
import json
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "news.json"
ITEMS_PER_FEED = 8
MAX_ITEMS = 120
REQUEST_TIMEOUT = 15
USER_AGENT = "GuardTheFlockNewsBot/1.0 (+https://github.com/jamescwk/guardtheflock)"

SOURCES = [
    {"name": "The Roys Report", "url": "https://roysreport.com/feed/", "cat": "accountability"},
    {"name": "The Wartburg Watch", "url": "https://www.thewartburgwatch.com/feed/", "cat": "accountability"},
    {"name": "MinistryWatch", "url": "https://ministrywatch.com/feed/", "cat": "accountability"},
    {"name": "Spiritual Sounding Board", "url": "https://spiritualsoundingboard.com/feed/", "cat": "accountability"},
    {"name": "Surviving Church", "url": "https://survivingchurch.org/feed/", "cat": "accountability"},
    {"name": "Abuse Tracker (Bishop Accountability)", "url": "https://www.bishop-accountability.org/category/news-archive/abusetracker/feed/", "cat": "accountability"},
    {"name": "ECA Global", "url": "https://www.ecaglobal.org/feed/", "cat": "accountability"},
    {"name": "SNAP Network", "url": "https://www.snapnetwork.org/rss.xml", "cat": "accountability"},
    {"name": "Religion News Service", "url": "https://religionnews.com/feed/", "cat": "mainstreamreligion"},
    {"name": "The Guardian — Religion", "url": "https://www.theguardian.com/world/religion/rss", "cat": "mainstreamreligion"},
    {"name": "AP News — Religion", "url": "https://rsshub.app/ap/topics/apf-religion", "cat": "mainstreamreligion"},
    {"name": "Christianity Today", "url": "https://www.christianitytoday.com/feed/", "cat": "evangelical"},
    {"name": "Christian Post", "url": "https://www.christianpost.com/rss", "cat": "evangelical"},
    {"name": "Baptist News Global", "url": "https://baptistnews.com/feed/", "cat": "evangelical"},
    {"name": "Charisma News", "url": "https://www.charismanews.com/feed", "cat": "evangelical"},
    {"name": "Christian Headlines", "url": "https://www.christianheadlines.com/rss", "cat": "evangelical"},
    {"name": "Relevant Magazine", "url": "https://relevantmagazine.com/feed/", "cat": "evangelical"},
    {"name": "Catholic News Agency", "url": "https://www.catholicnewsagency.com/feed", "cat": "catholic"},
    {"name": "National Catholic Reporter", "url": "https://www.ncronline.org/rss.xml", "cat": "catholic"},
    {"name": "Crux — Catholic News", "url": "https://cruxnow.com/feed/", "cat": "catholic"},
    {"name": "The Star (MY)", "url": "https://www.thestar.com.my/rss/News/Nation/", "cat": "asia"},
    {"name": "Malay Mail", "url": "https://www.malaymail.com/feed", "cat": "asia"},
    {"name": "Channel NewsAsia", "url": "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml", "cat": "asia"},
    {"name": "Straits Times", "url": "https://www.straitstimes.com/news/singapore/rss.xml", "cat": "asia"},
]

ATOM = "{http://www.w3.org/2005/Atom}"
DC = "{http://purl.org/dc/elements/1.1/}"


def first_text(element: ET.Element, *names: str) -> str:
    for name in names:
        child = element.find(name)
        if child is not None:
            value = "".join(child.itertext()).strip()
            if value:
                return value
    return ""


def clean_text(value: str, limit: int = 180) -> str:
    value = re.sub(r"<[^>]*>", " ", value)
    value = unescape(value)
    return re.sub(r"\s+", " ", value).strip()[:limit]


def normalized_date(value: str) -> str:
    if not value:
        return ""
    try:
        parsed = parsedate_to_datetime(value)
    except (TypeError, ValueError, OverflowError):
        try:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            return ""
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def item_from_element(element: ET.Element, source: dict[str, str]) -> dict[str, str] | None:
    title = clean_text(first_text(element, "title"))
    if not title:
        return None

    if element.tag.endswith("entry"):
        link = ""
        for candidate in element.findall(f"{ATOM}link"):
            href = candidate.get("href", "").strip()
            rel = candidate.get("rel", "alternate")
            if href and rel in ("alternate", ""):
                link = href
                break
        if not link:
            link = first_text(element, f"{ATOM}id")
        date = first_text(element, f"{ATOM}published", f"{ATOM}updated")
    else:
        link = first_text(element, "link")
        date = first_text(element, "pubDate", "published", "updated", f"{DC}date")

    link = unescape(link.strip())
    if not link.startswith("https://"):
        return None

    return {
        "title": title,
        "link": link,
        "date": normalized_date(date),
        "source": source["name"],
        "cat": source["cat"],
    }


def fetch_source(source: dict[str, str]) -> list[dict[str, str]]:
    request = urllib.request.Request(
        source["url"],
        headers={"User-Agent": USER_AGENT, "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml"},
    )
    with urllib.request.urlopen(request, timeout=REQUEST_TIMEOUT) as response:
        content = response.read(3_000_000)
    root = ET.fromstring(content)
    elements = list(root.findall(".//item"))
    if not elements:
        elements = list(root.findall(f".//{ATOM}entry"))
    result = []
    for element in elements[:ITEMS_PER_FEED]:
        item = item_from_element(element, source)
        if item:
            result.append(item)
    return result


def main() -> int:
    all_items: list[dict[str, str]] = []
    updated_sources: list[str] = []
    errors: list[str] = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
        jobs = {executor.submit(fetch_source, source): source for source in SOURCES}
        for future in concurrent.futures.as_completed(jobs):
            source = jobs[future]
            try:
                items = future.result()
                if items:
                    all_items.extend(items)
                    updated_sources.append(source["name"])
                else:
                    errors.append(f"{source['name']}: feed contained no valid items")
            except (urllib.error.URLError, TimeoutError, ET.ParseError, OSError, ValueError) as exc:
                reason = getattr(exc, "reason", exc)
                errors.append(f"{source['name']}: {str(reason)[:180]}")

    all_items.sort(key=lambda item: item["date"], reverse=True)
    # Dedupe identical stories syndicated across publisher feeds.
    unique_items = []
    seen_links = set()
    for item in all_items:
        if item["link"] in seen_links:
            continue
        seen_links.add(item["link"])
        unique_items.append(item)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    payload: dict[str, Any] = {
        "schemaVersion": 1,
        "updatedAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "sourcesUpdated": len(updated_sources),
        "sources": updated_sources,
        "sourceCount": len(SOURCES),
        "itemCount": min(len(unique_items), MAX_ITEMS),
        "items": unique_items[:MAX_ITEMS],
    }
    if not unique_items and OUTPUT.exists():
        print("No source returned valid headlines; preserving the existing snapshot.", file=sys.stderr)
        return 0
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote {payload['itemCount']} unique headlines from {payload['sourcesUpdated']}/{payload['sourceCount']} sources to {OUTPUT.relative_to(ROOT)}")
    for error in errors:
        print(f"Feed warning: {error}", file=sys.stderr)
    if not unique_items:
        print("No source returned valid headlines; created an empty snapshot so the page can show a graceful state.", file=sys.stderr)
    elif not updated_sources:
        print("Unexpected empty source list after parsing headlines.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
