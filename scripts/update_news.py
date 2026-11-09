#!/usr/bin/env python3
"""Refresh docs/news.html with one current Google News RSS headline per category."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NEWS_PAGE = ROOT / "docs" / "news.html"
RSS_BASE = "https://news.google.com/rss/search?hl=en-US&gl=US&ceid=US:en&q="
CATEGORIES = (
    ("Democrats", "DEMOCRATS", "Politics", "Democratic Party announcement OR Democrats significant event"),
    ("Republicans", "REPUBLICANS", "Politics", "Republican Party announcement OR Republicans significant event"),
    ("Department of Justice", "DOJ", "Government", "Department of Justice DOJ news"),
    ("Department of Defense", "DOD", "Government", "Department of Defense Pentagon news"),
    ("Immigration and Customs Enforcement", "ICE", "Government", "ICE immigration enforcement news"),
    ("Impeachment", "IMPEACHMENT", "Politics", "impeachment news United States"),
    ("Oil prices", "OIL PRICES", "Energy", "oil prices crude oil market news"),
    ("Iran", "IRAN", "World", "Iran news"),
)


def fetch_xml(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "deptofwarcrimes-news-updater/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def source_and_title(title: str) -> tuple[str, str]:
    headline, separator, source = title.rpartition(" - ")
    return (source if separator else "Google News", headline if separator else title)


def first_item(category: str, label: str, category_type: str, query: str) -> dict[str, object]:
    rss_url = RSS_BASE + urllib.parse.quote_plus(query)
    root = ET.fromstring(fetch_xml(rss_url))
    item = root.find("./channel/item")
    if item is None:
        raise RuntimeError(f"No Google News RSS items for {category}")
    raw_title = (item.findtext("title") or "").strip()
    source_name, headline = source_and_title(raw_title)
    source_url = (item.findtext("link") or rss_url).strip()
    published = parsedate_to_datetime(item.findtext("pubDate") or "").astimezone(UTC)
    return {
        "category": category_type,
        "label": label,
        "date": published.strftime("%b %d, %Y").upper(),
        "title": headline,
        "summary": f"Latest {category.lower()} headline surfaced by Google News from {source_name}.",
        "source": source_url,
        "sourceName": source_name,
        "secondary": {"label": f"Google News · {label.title()}", "url": rss_url},
        "platforms": [{"name": f"Google News · {category}", "url": rss_url}],
    }


def replace_once(document: str, pattern: str, replacement: str) -> str:
    updated, count = re.subn(pattern, replacement, document, count=1, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError(f"Expected one match for {pattern!r}, found {count}")
    return updated


def update_page(stories: list[dict[str, object]], now: datetime) -> bool:
    document = NEWS_PAGE.read_text(encoding="utf-8")
    for index, story in enumerate(stories, start=1):
        story["id"] = index
    # Keep article text from ever terminating the surrounding script element.
    data = json.dumps(stories, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    timestamp = now.strftime("%b %d, %Y · %H:%M UTC").upper()
    document = replace_once(
        document,
        r'(<script type="application/json" id="story-data">).*?(</script>)',
        lambda match: f"{match.group(1)}\n{data}\n{match.group(2)}",
    )
    document = replace_once(
        document,
        r'(<small id="snapshot-date">).*?(</small>)',
        lambda match: f"{match.group(1)}{timestamp}{match.group(2)}",
    )
    new_document = document
    if new_document != NEWS_PAGE.read_text(encoding="utf-8"):
        NEWS_PAGE.write_text(new_document, encoding="utf-8")
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fetch and validate feeds without editing the page.")
    args = parser.parse_args()
    try:
        stories = [first_item(*definition) for definition in CATEGORIES]
        if args.check:
            print(f"Validated {len(stories)} headline feeds.")
            return 0
        changed = update_page(stories, datetime.now(UTC))
    except Exception as error:
        print(f"News update failed: {error}", file=sys.stderr)
        return 1
    print(f"Updated {NEWS_PAGE.relative_to(ROOT)} with {len(stories)} headlines." if changed else "No headline changes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
