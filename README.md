# Guard the Flock

**A free, public educational resource on spiritual abuse**—what it is, how to recognise it, and where to find support and further reading.

🌐 **Live site:** [jamescwk.github.io/guardtheflock](https://jamescwk.github.io/guardtheflock)

## Current version

**v7.4.0** — the focused news feed prioritizes specialist accountability publishers and displays publisher-provided bylines. See [Versioning](#versioning) and the [changelog](CHANGELOG.md).

## What the site covers

- **What Is Spiritual Abuse?** — a definition and common forms
- **Warning Signs** — nine patterns to help readers identify concerning behaviour
- **How to Respond** — guidance for people affected and for leaders or witnesses
- **Resources** — books, organisations, and journalism from Malaysia, Asia, and globally
- **Documented Cases** — links to independent reporting, with distinctions between allegations, convictions, and settlements
- **Latest News** — focused reporting on spiritual/sexual abuse, church financial misconduct, and institutional accountability, prioritizing The Roys Report and other specialist sites; publisher-provided authors are shown when available. General news is excluded.
- **Get Help** — support contacts for Malaysia, Singapore, and globally
- **FAQ** — including guidance for cell-group leaders and pastoral workers

## Important scope and editorial notes

This site is educational material, not a complaints platform. It does **not** name, rate, or maintain a database of individual churches, pastors, or leaders. Headlines and case links are provided by independent publishers. A reported allegation is not a finding of guilt; a settlement is not necessarily an admission of wrongdoing. Please read the linked publisher's reporting and verify time-sensitive support contacts before relying on them.

## Latest News: how it works

The browser no longer fetches publisher feeds through public CORS proxies. A GitHub Actions workflow runs every four hours, and can also be started manually from **Actions → Update latest news snapshot → Run workflow**. It fetches the configured public RSS/Atom feeds, keeps only stories that match both a church/faith-community context and a substantive abuse, misconduct, financial fraud, or accountability topic, and writes a bounded snapshot to `data/news.json`. General religion and world news are intentionally excluded. Repeated URLs and near-identical descriptions of the same incident from one publisher are deduplicated, while distinct follow-up reporting is retained. Sources are displayed in their configured priority order, led by The Roys Report; publisher-provided authors are included when available. The static site reads that same-origin JSON file; if it cannot be loaded, it shows a clear unavailable message and keeps the separately linked resources available.

The workflow needs no API keys or repository secrets. It uses the repository's `GITHUB_TOKEN` with `contents: write` to commit a changed snapshot. Ensure GitHub Actions are enabled and the repository's workflow token has permission to write contents. Scheduled runs use GitHub's UTC schedule and can be delayed by GitHub during high load. Individual publisher feeds may be unavailable, rate-limited, or change format; the generator continues when a feed fails and reports that feed as a workflow warning. If all feeds fail, it preserves the prior snapshot rather than replacing good data with an empty file.

Run the generator locally with Python 3:

```sh
python scripts/update_news.py
```

It uses only the Python standard library. To add or remove a source, edit the `SOURCES` list in `scripts/update_news.py`; keep it focused on church accountability or abuse reporting. Tune `CONTEXT_TERMS`, `TOPIC_TERMS`, and `EXCLUSION_TERMS` conservatively, then run the generator and validate the resulting JSON. Categories are `sexual-abuse`, `spiritual-abuse`, `financial-misconduct`, and `institutional-accountability`. Feed availability varies by runtime and geography, so local failures do not necessarily indicate the GitHub runner will see the same result.

## Development and deployment

This is a static site hosted with GitHub Pages. The main page is `index.html`; there is no frontend build step or package install. Open `index.html` in a browser for a visual check. The news tab works locally when `data/news.json` is present; direct `file://` URLs may restrict JSON fetches, so use a local static HTTP server when testing that tab. GitHub Pages serves the JSON over HTTP after it has been pushed and deployed.

## Versioning

The project uses [Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`.

- **MAJOR**: incompatible changes to the site's public structure or content/data contract.
- **MINOR**: backward-compatible features or substantial new sections.
- **PATCH**: backward-compatible fixes, corrections, and maintenance.

The version is documented in `VERSION` and changes are recorded in `CHANGELOG.md`. Version labels are repository release metadata; they do not alter the static page's runtime. Tag releases as `vX.Y.Z` when publishing a GitHub Release.

## Wiki

The repository wiki is maintained separately by GitHub and is not included in a normal clone. See [`docs/wiki/`](docs/wiki/) for the maintained wiki source pages, including the home/overview, news feed operations, and support/resources guidance. When the wiki pages change, publish their contents to the GitHub Wiki if that feature is enabled for the repository.

## Contributing

Contributions are welcome, especially:

- Additional, verified support contacts for other countries
- Corrections to phone numbers, availability, or URLs
- Additional reputable books and organisations
- Translations into Bahasa Malaysia or Mandarin
- Fixes to the feed generator or accessible page behaviour

Please open an Issue or Pull Request. Do not submit private survivor information or unverified allegations about identifiable individuals.

## License

MIT License — free to use, adapt, and share with attribution. See [`LICENSE`](LICENSE).

## Credits

Built by [James CWK](https://github.com/jamescwk) with assistance from Claude (Anthropic). Content is sourced from published books, established organisations, and journalism. News articles remain the property and responsibility of their publishers.
