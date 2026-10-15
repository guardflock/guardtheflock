# Latest News operations

The Latest News tab displays a static JSON snapshot generated from configured public RSS/Atom sources. This avoids depending on browser-side CORS proxy services.

## Automatic update

`.github/workflows/update-news.yml` runs on a four-hour UTC schedule. It can also be started manually in GitHub: **Actions → Update latest news snapshot → Run workflow**. On changes, it commits `data/news.json` using the workflow's built-in `GITHUB_TOKEN`.

For the automatic commit to work, Actions must be enabled and repository settings must allow the workflow token to write repository contents. No personal token or other secret is required.

## Sources and categories

The source registry is the `SOURCES` list in `scripts/update_news.py`. Each source has a display name, feed URL, and category. Supported category values are:

- `accountability`
- `mainstreamreligion`
- `evangelical`
- `catholic`
- `asia`

Each run attempts feeds independently. A publisher timeout, access denial, or malformed feed is recorded as a warning; other publishers can still update. Headlines are limited per source and overall, deduplicated by HTTPS article URL, normalized, and written to `data/news.json`.

If all publishers fail and a previous snapshot exists, the script preserves it. The page displays the snapshot's update time and an error message if neither the local JSON nor the GitHub raw fallback can be read.

## Run and validate locally

Requires Python 3 only:

```sh
python scripts/update_news.py
python -m py_compile scripts/update_news.py
```

The fetch results can differ between a developer machine and GitHub's runner because publisher access policies vary. Check the workflow logs for `Feed warning` lines when a publisher is absent. Validate the JSON is well-formed and contains `items` before relying on it. Do not work around a publisher's access restrictions with undocumented or credentialed scraping.

## Troubleshooting

- **Workflow did not run:** check Actions are enabled; scheduled runs may be delayed by GitHub.
- **Commit rejected:** check workflow token permissions include contents write and branch rules allow the Actions bot to push.
- **Some sources missing:** inspect individual `Feed warning` messages; feed URLs and publisher policies can change.
- **News tab says unavailable:** verify `data/news.json` is deployed at the Pages site path and contains valid JSON. Confirm the Pages deployment includes the generated file.
- **No snapshot exists yet:** manually run the workflow or run the Python script locally, then publish the resulting JSON.
