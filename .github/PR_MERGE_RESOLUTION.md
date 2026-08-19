# Merge resolution note

I resolved the merge conflict in `scripts/rss_fetcher.py` and committed the merged result to this branch. Summary of what I did:

- Kept main's logging, structure, and flow while applying the security changes from the feature branch.
- Added imports: `socket`, `urllib.parse`, `ipaddress`.
- Added `is_safe_url(url)` which:
  - Parses the URL and requires `http`/`https`.
  - Resolves the hostname and rejects any resolved IP that is not public (`ip.is_global`).
- Rewrote `fetch_article(url)` to:
  - Manually follow redirects up to `max_redirects` (default 5).
  - Validate each redirect target with `is_safe_url` before fetching.
  - Use requests with `allow_redirects=False` and only fetch after URL validation.
  - Return an empty string on validation/fetch errors.
- Added a unit test file `scripts/test_rss_fetcher.py` covering safe/unsafe URL checks (mocking DNS is recommended for CI).

Notes and caveats:
- DNS resolution currently uses the system resolver (`socket.getaddrinfo`). For stronger guarantees, consider using a trusted DNS resolver or an allowlist of feed domains.
- `ip.is_global` is a reasonable default but review RFC ranges and your policy for link-local or shared address spaces.
- Tests currently perform real DNS lookups; consider mocking `socket.getaddrinfo` in CI to avoid flakiness.

This file was added to ensure the PR includes an explicit merge-resolution note.
