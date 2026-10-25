# Guard the Flock — link audit and proposed repairs

**Audit date:** 2026-10-20  
**Repository revision audited:** `ef56b72537002a53ad2442facb7841589755bb08` (`ef56b72`, `main`); local repairs uncommitted  
**Pages URL:** <https://jamescwk.github.io/guardtheflock/>  
**Prior Netlify URL found in social metadata:** <https://guardtheflock.netlify.app/>

**Repair status:** Local `index.html` repairs are uncommitted. The remainder of this report includes the first audit inventory and the follow-up repair/test record.

## Executive summary

- The live GitHub Pages and Netlify sites both returned HTTP 200, but they were serving an **older HTML build** than the inspected `main` source. They still showed the old Latest News tab; GitHub Pages also lacked the newer discernment section. This is a deployment/source mismatch, not an unreachable root URL.
- The Open Graph image URL `https://guardtheflock.netlify.app/og-cover.png` returns 404 on both hosts. The Open Graph canonical URL also points at Netlify while the README identifies GitHub Pages as the live site.
- Confirmed broken source links included Christianity Today's three `/ct/topics/...` topic links, BBC's old church-abuse topic slug, MinistryWatch `/category/news/`, ProPublica's former religion topic and Gospel of Prosperity series URLs, The Wartburg Watch's `church-discipline-abuse` slug, Straits Times `/tags/church`, CNA `/singapore/church`, and IJM's old `/our-work/trafficking` route.
- Some publishers block automated access (401/403, Cloudflare interstitial, or timeouts). These are **inconclusive**, not confirmed dead links.
- An especially serious destination issue: `cfm.org.my` returned HTTP 200 with page title “KiraLoan - Kira kemampuan loan anda”, which appears unrelated to the Christian Federation of Malaysia. It has been removed from the site until the official domain can be verified.
- This report records the original audit and the repair choices made in `index.html`. It is a link audit, not a fact-check of each story, clinical review of support resources, or legal assessment.

## Repairs made in this pass

| Old target | Current action / recommendation | Verification |
|---|---|---|
| `https://guardtheflock.netlify.app/og-cover.png` | Removed the non-existent `og:image` declaration. | Both Pages and Netlify returned 404 for that file. |
| `og:url` pointing to Netlify | Changed canonical Open Graph URL to `https://jamescwk.github.io/guardtheflock/`. | Pages is the README’s stated live site. |
| Kairos Centre target `kairosresearch.com` | Removed the hyperlink; left an explicit note that the target domain belongs to an unrelated Ohio AI research business and needs verification. | Current destination title/about content was unrelated. |
| CFM `cfm.org.my` | Removed the hyperlink and left a warning pending verification of CFM’s current official site. | Target title was “KiraLoan”, unrelated to CFM. |
| `www.micahasia.com` | Replaced with `https://micahglobal.org`. | Micah Global site and Asia network are live. Verify this is the intended organization/editorial recommendation before treating it as a substitute for the former Micah Asia domain. |
| `www.befrienderskl.org` | Replaced with `https://www.befrienders.org.my`, label changed to Befrienders Malaysia. | `.org.my` resolves; verify exact KL hotline details and operating hours on the destination before relying on them. |
| `www.spiritualabuseresources.com` | Replaced with the previously listed, reachable Religious Trauma Institute site. | Old site TLS/DNS failed; replacement resolves, but it is a different organization and should be described as such. |
| `www.micahasia.com` | Replaced with Micah Global at `https://micahglobal.org`. | Domain/site checked; maintainers should confirm this is the intended successor/network reference. |
| AP hubs | Removed the broken abuse hub and broad trafficking hub. | The religion endpoint itself is live, but it is broad; no longer used in the abuse-specific case links. |
| Broad RNS/CT/AP/NYT/Guardian discovery links | Removed where they were generic, blocked, or not a case-specific reference; retained case-focused publisher links and only labeled broad archives accurately. | Automated blocking was treated as inconclusive, not as a 404. |
| ProPublica link placement | Kept the “Forgive and Forget” series under sexual abuse/global investigations, not finance. | The series is specifically about a church enabling child sexual abuse; not a financial-fraud series. |
| duplicate regional/tag references | Removed duplicate Straits Times entry and removed broad Religion News Service region tag. | Avoids repetition and overly broad non-case discovery links. |
| Christianity Today `/ct/topics/s/sexual-abuse/`, `/ct/topics/f/finances/`, `/ct/topics/p/pastoral-misconduct/` | Replaced with the live general CT News page in the entries that remain, with labels that disclose readers must search for the relevant subject. | Old paths returned 404; `https://www.christianitytoday.com/news/` returned 200. This is broader than a topic archive; better remove if a focused current archive is found. |
| BBC retired church-abuse topic | Replaced with `https://www.bbc.co.uk/search?q=church%20abuse`. | Old slug returned 404; search page returned 200 and produced church-abuse reporting results. Search is dynamic, so review its results periodically. |
| MinistryWatch `/category/news/` | Replaced with `https://ministrywatch.com/category/church/`. | Old path returned 404; Church category returned 200 and is more on-topic. |
| ProPublica religion/Gospel-of-Prosperity URLs | Replaced with live `https://www.propublica.org/series/forgive-and-forget`, specifically described as a series on a church enabling child sexual abusers. | Series page returned 200 and its reporting is directly relevant. A separate financial-fraud replacement was not found in this audit; do not present this abuse series as a finance/fraud resource. |
| IJM `/our-work/trafficking` | Replaced with `https://www.ijm.org/our-work/trafficking-slavery`. | Old URL returned 404; current IJM navigation lists “Trafficking & Slavery” at this route. HEAD got 403 but official page navigation/content established the destination. |
| Wartburg Watch `/category/church-discipline-abuse/` | Replaced with `https://thewartburgwatch.com/category/church-discipline/`. | Old slug returned 404; current category page returned 200 and includes church-discipline content. |
| Straits Times `/tags/church` | Replaced with `https://www.straitstimes.com/tags/churches`; label warns it is general coverage. | Old singular slug returned 404; plural slug returned 200. It is not abuse-specific. |
| CNA `/singapore/church` | Removed because the replacement was a broad search/general section, not a specific, relevant case archive. | Old URL returned 404. CNA search loads but does not give a stable topical archive. |
| Generic The Star `q=church` | Replaced with `q=pastor+abuse` and label says it is a search. | Search endpoint resolves; results are dynamic and need human review. |
| Religion News Service South Korea tag | Removed because the destination was blocked and the displayed link was not a specific abuse/accountability archive. | 403 during checks. Root and some tags may work in a normal browser but were inconclusive here. |
| AP Church Abuse hub | Replaced with `https://apnews.com/religion`, relabeled to AP Religion. | Original hub returned 403/404 depending on client. `/religion` returned a current AP Religion page. It remains broad; click-through targets should be chosen case-by-case. |
| AP human-trafficking hub | Removed to avoid a bot-blocked, broad hub; IJM remains as the specialist trafficking source. | Hub could not be verified and was not essential after IJM repair. |
| The Guardian religion page | Changed to the publisher’s RSS endpoint `https://www.theguardian.com/world/religion/rss`, clearly labeled as Religion reporting. | RSS endpoint returns valid RSS. It remains a broad discovery source; not every item is abuse-related. |
| NYT clergy-abuse topic | Replaced with ProPublica’s specific “Forgive and Forget” church-abuse investigation series. | NYT target was 403/paywall-blocked; ProPublica replacement is directly relevant and reachable. |
| Religion News Service root/tag links | Retained only where the resource is explicitly a reporting source; its crawler response is blocked. | 403 is inconclusive, not evidence of removal. A human should check browser access before further pruning. |

## Link-by-link status of remaining links in current `index.html`

Statuses below were checked with HTTP HEAD/GET or web fetch on 2026-10-20. A 401/403/502 or connection error may be an automated-client restriction. “200” verifies a response, **not** that every article in a search/archive is on-topic.

### Metadata and assets

| Link | Status | Notes |
|---|---|---|
| `https://jamescwk.github.io/guardtheflock/` (`og:url`) | 200 | Canonical project URL; deployed HTML was stale during this audit. |
| Google Fonts stylesheet | 200 | Font stylesheet; system fallback is configured. |
| `og:image` | Removed | No image file existed at old Netlify URL; add a real image file before restoring the tag. |

### Resources

| Link | Status | Notes |
|---|---|---|
| GRACE `https://www.graceresponse.com` | 200 | Relevant church-abuse response/investigation resource. Confirm current scope/availability before asserting referral eligibility. |
| Religion News Service `https://religionnews.com` | 403 | Automated access blocked; destination’s identity/relevance is known, response not verified in this client. |
| Wartburg Watch `https://www.thewartburgwatch.com` | 200 | Relevant commentary/watchdog source; distinguish commentary from formal investigation. |
| Bare Marriage `https://baremarriage.com` | 200 | Relevant to harmful marriage/purity teaching, not a general case archive. |
| Kairos Research Centre | No hyperlink | `kairosresearch.com` is an unrelated AI company; former `.org.my` host did not resolve. Do not restore a link until the Centre provides a verified official domain. |
| NECF `https://necf.org.my` | 200 | Official-looking NECF site; verify its current complaint/ethics process before directing complainants. |
| Micah Global `https://micahglobal.org` | 200 | Live regional network; confirm this is the specific intended organization/resource. |
| CFM | No hyperlink | Former `cfm.org.my` served unrelated loan content. Obtain verified CFM official URL before adding. |

### Sexual abuse and assault

| Link | Status | Notes |
|---|---|---|
| Reuters Southern Baptist investigation | 401 | Likely access/bot restriction; not confirmed dead. |
| AP Religion `https://apnews.com/religion` | 200 via web fetch | Live religion section; broad discovery page, not a case-specific archive. |
| BBC search `https://www.bbc.co.uk/search?q=church%20abuse` | 200 | Search returned directly relevant reports, but results are dynamic. |
| Wartburg Watch sexual-abuse category | 200 | Category loads. |
| Roys Report sexual-abuse category | Resolves/site challenge | Site may challenge automated clients; treat as inconclusive but route appears valid. |

### Financial misconduct

| Link | Status | Notes |
|---|---|---|
| MinistryWatch Church category `https://ministrywatch.com/category/church/` | 200 | Relevant church-focused reporting, though not every post is financial misconduct. |
| Roys Report fraud/financial category | Resolves/site challenge | On-topic path; verify in browser if challenge persists. |
| ProPublica “Forgive and Forget” series | 200 | Directly relevant church-abuse investigation; **not a financial-fraud series**. Remove from finance card or relabel/move it to abuse/institutional accountability. No confirmed ProPublica finance replacement identified. |

### Trafficking and forced labour

| Link | Status | Notes |
|---|---|---|
| IJM Trafficking & Slavery `https://www.ijm.org/our-work/trafficking-slavery` | Cloudflare 403 but official navigation confirms route | Correct current focus area; bot response is inconclusive. |

### Deaths/criminal negligence, coercive control, regional and global resources

| Link | Status | Notes |
|---|---|---|
| Guardian Religion RSS | 200 | Valid RSS but broad; readers may encounter general religion news. Label it discovery/reporting archive, not a set of verified abuse cases. |
| Wartburg Watch Church Discipline | 200 | Relevant category archive. |
| Roys Report Spiritual Abuse | Resolves/site challenge | Relevant path; browser may require verification. |
| Church Clarity | 200 | Policy-transparency project, not a case-reporting/news archive. Its current label appropriately calls it a transparency project. |
| Straits Times Churches tag | 200 | Valid plural tag; general church news, not abuse-specific. Label says general coverage. |
| CNA Singapore landing | 200 | General Singapore news, not abuse-specific. It was retained only as regional coverage; consider removing to avoid implying it is a case archive. |
| The Star search `pastor abuse` | 200 | Search endpoint works; dynamic relevance varies. |
| Malay Mail search `church abuse` | GET returned a search page; HEAD often 403 | Search results are noisy; a query does not guarantee abuse-related results. |
| BBC search `church abuse` | 200 | Dynamic search; directly relevant hits observed. |
| Roys Report home | Resolves/site challenge | On-topic investigative publisher. |
| Wartburg Watch home | 200 | Live site. |
| ProPublica “Forgive and Forget” series | 200 | Highly relevant church-enabled child-abuse investigation series. |
| ProPublica Criminal Justice topic | 200 | Broad archive; removed as an extra generic destination. |
| NYT clergy sex-abuse topic | 403/paywall block | Not confirmed dead; individual access may require subscription. Consider removal from “available sources” if readers cannot access it. |

### Support and crisis contacts

| Link | Status | Notes |
|---|---|---|
| Befrienders Malaysia `https://www.befrienders.org.my` | 200 with verification interstitial | Domain resolves. Confirm hotline number and hours against the official contact page. |
| MIASA `https://www.miasa.org.my` | 200 with verification interstitial | Domain resolves; verify helpline details. |
| AWAM `https://www.awam.org.my` | 200 | Domain resolves; verify current service details/hours. |
| SPRM `https://www.sprm.gov.my` | 200 | Domain resolves; verify contact method. |
| SOS `https://www.sos.org.sg` | 200 | Domain resolves; verify current hotline number/hours. |
| GRACE | 200 | See Resources notes. |
| Religious Trauma Institute | 200 | Site resolves; validate therapist directory and claims before relying on it. |
| Psychology Today therapist finder | 502 | Transient/bot response; not confirmed dead. |
| Spiritual Abuse Resources | Removed from link | Previous domain failed TLS/DNS checks; replacement is a different organization (RTI) and now displayed under its actual name. |

## Deployment and whole-site behavior

- The published root and current repository source disagree. Published GitHub Pages and Netlify return 200 but still expose the old Latest News tab; they will need a successful publish from current `main` to match the latest source. No separate internal HTML pages are linked from the current source; tabs are JavaScript-driven.
- Direct external anchor count in the audited repository source: 49 occurrences, 48 unique URLs before this repair pass. Remaining blocked hosts require a manual browser review.
- The audit validates link reachability/relevance at the destination level only. It does not independently verify legal claims, each support hotline’s current status, or every article’s factual claims.

## Follow-up recommendations

1. Remove the ProPublica abuse series from the Financial Fraud card; its subject is church sexual-abuse handling, not financial fraud.
2. Decide whether broad Straits Times/CNA/The Star/Malay Mail search links belong on the Regional Coverage panel; they are not curated case archives and can surface unrelated news.
3. Ask the actual organizations for current verified URLs for Kairos Research Centre and Christian Federation of Malaysia before restoring links.
4. Human-test Reuters/AP/NYT/RNS/IJM/support-service pages in an ordinary browser; automated 401/403 responses alone are inconclusive.
5. Confirm GitHub Pages is publishing the intended `main` branch after the site's latest source push.

## Repair pass on current `main` source (2026-10-20)

The link fixes were applied to the local `index.html`; they are **not yet in the published site**. Changes made:

- Removed the dead `og-cover.png` reference and changed `og:url` to the GitHub Pages canonical URL.
- Replaced the dead BBC topic link with BBC search; the dead MinistryWatch news category with `/category/church/`; the old IJM trafficking path with `/our-work/trafficking-slavery`; the dead Wartburg Watch slug with `/category/church-discipline/`; and the ProPublica dead religion/prosperity links with its live `Forgive and Forget` church-abuse series.
- Removed AP and RNS links that were broad or blocked in automated checks. Replaced CT dead topic archives with the live general CT News page only where retained, and labeled it as a broad page/search.
- Removed CFM's loan-site link and Kairos's unrelated AI-company domain. Removed CNA's generic Singapore link. Replaced former Micah Asia target with Micah Global and Befrienders KL target with Befrienders Malaysia; these are organization/destination changes and should be confirmed by the maintainer. Religious Trauma Institute is linked under its own name, not as a replacement label for Spiritual Abuse Resources.
- Changed ProPublica abuse series placement out of the Finance card into general investigations; MinistryWatch is labeled broadly as Church coverage. Kept the NYT link out because it was blocked/paywalled and not verified accessible.
- Added a note clarifying the site has no formal publisher affiliation.

- Removed general AP hubs from the specific case lists. AP’s live `/religion` page is broad and remains available by navigating AP directly, but is not presented as a curated church-abuse archive here.
- Removed generic financial/religion/news sources from the case cards where their topic coverage was broad and no precise abuse/financial-misconduct category could be validated.
- Removed NYT’s broad clergy-abuse page from the global case list because automated checks were blocked and a reliable current direct archive could not be confirmed.
- The Reporter card still retains Reuters as a high-value investigation destination; it returned 401 here, so the link is marked subscription/access-limited rather than dead.

Verification after repair: local inline JavaScript syntax passed. New BBC search, CT News, MinistryWatch Church category, ProPublica Forgive and Forget, Wartburg Watch Church Discipline, Straits Times Churches, CNA search, The Star search, Micah Global, Befrienders Malaysia, and Religious Trauma Institute destinations responded 200. IJM's replacement focus page returned a Cloudflare 403 in this runtime but was found in official IJM navigation. A 200 search page is not evidence all its results are relevant. GitHub Pages still serves the stale pre-repair page until these changes are pushed and the deployment completes. Please confirm the organization changes and crisis-contact information in a normal browser before relying on them.
