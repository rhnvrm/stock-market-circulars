"""Fetch helpers for hosts whose WAF rejects non-browser TLS fingerprints.

MCX sits behind Akamai, which returns 403 to httpx/requests/curl (JA3 fingerprint).
curl_cffi impersonating Chrome gets through, for both the RSS feeds and the
/docs/default-source/ documents. It is imported lazily so other sources don't need it.
"""

from pathlib import Path
from urllib.parse import urlsplit

IMPERSONATE_HOSTS = ("mcxindia.com",)
IMPERSONATE = "chrome120"


def needs_impersonation(url: str) -> bool:
    host = (urlsplit(url).hostname or "").lower()
    return any(host == h or host.endswith("." + h) for h in IMPERSONATE_HOSTS)


async def fetch_text(url: str, timeout: float) -> str:
    from curl_cffi.requests import AsyncSession

    async with AsyncSession(impersonate=IMPERSONATE) as session:
        response = await session.get(url, timeout=timeout, allow_redirects=True)
        response.raise_for_status()
        return response.text


async def download_file(url: str, path: Path, timeout: float) -> str:
    """Write the body to path and return the Content-Disposition header."""
    from curl_cffi.requests import AsyncSession

    async with AsyncSession(impersonate=IMPERSONATE) as session:
        response = await session.get(url, timeout=timeout, allow_redirects=True)
        response.raise_for_status()
        Path(path).write_bytes(response.content)
        return response.headers.get("content-disposition", "")
