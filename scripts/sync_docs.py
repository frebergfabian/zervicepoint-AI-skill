#!/usr/bin/env python3
"""Spegla docs.zervicepoint.com lokalt som Markdown och generera ett sidindex.

Användning (från repots rot):

    python scripts/sync_docs.py            # hämta allt, skriv cache + katalog
    python scripts/sync_docs.py --catalog-only   # bygg om katalogen från befintlig cache

Resultat:
  .claude/skills/zervicepoint/docs-cache/<sökväg>.md   fulltext per sida (gitignorerad)
  .claude/skills/zervicepoint/docs-cache/_manifest.json  sida -> titel, url, rubriker
  .claude/skills/zervicepoint/references/docs-catalog.md genererad katalog (versionshanterad)

Leverantörens dokumentation är upphovsrättsskyddad. Fulltextspegeln är en lokal
sökcache och ska inte committas; katalogen innehåller bara titlar, rubriker och länkar.
Endast standardbiblioteket används.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
import time
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

BASE = "https://docs.zervicepoint.com/"
ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / ".claude" / "skills" / "zervicepoint"
CACHE = SKILL / "docs-cache"
CATALOG = SKILL / "references" / "docs-catalog.md"
UA = "docs-index-sync/1.0 (+stdlib urllib)"

SECTION_NAMES = {
    "": "Startsida",
    "about": "Om dokumentationen",
    "intro": "Introduktion",
    "getting-started": "Kom igång",
    "concepts": "Begrepp",
    "system-overview": "Systemöversikt",
    "adminweb": "AdminWeb",
    "userweb": "UserWeb",
    "reference": "Referens (JavaScript, aktiviteter, formulärfält, snippets)",
    "tutorials": "Tutorials",
    "how-to": "How-to (PowerShell, REST, providers m.m.)",
    "plugins": "Plugins",
    "plugins-and-template-services": "Plugins och malltjänster",
    "onboarding": "Molnonboarding och worker",
    "infrastructure": "Infrastruktur och installation",
    "zerflow": "ZerFlow (arbetsflödesmotor)",
    "troubleshooting": "Felsökning",
    "release-notes": "Release notes",
    "downloads": "Nedladdningar",
}


def fetch(url: str, retries: int = 3) -> bytes:
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as exc:  # noqa: BLE001
            if attempt == retries - 1:
                raise
            print(f"  retry {url}: {exc}", file=sys.stderr)
            time.sleep(2 * (attempt + 1))
    raise RuntimeError("unreachable")


def page_list() -> list[str]:
    data = json.loads(fetch(BASE + "search/search_index.json").decode("utf-8"))
    seen: dict[str, None] = {}
    for d in data["docs"]:
        seen.setdefault(d["location"].split("#")[0], None)
    return list(seen)


# ---------------------------------------------------------------- HTML -> Markdown

class MD(HTMLParser):
    """Liten HTML->Markdown-konverterare för MkDocs Material-artiklar."""

    SKIP = {"script", "style", "nav", "svg", "button", "form"}

    def __init__(self, page_url: str):
        super().__init__(convert_charrefs=True)
        self.page_url = page_url
        self.out: list[str] = []
        self.in_article = 0
        self.skip = 0
        self.skip_tag = ""
        self.pre = 0
        self.code_inline = 0
        self.lists: list[list] = []  # [type, counter]
        self.links: list[str | None] = []
        self.table: list[list[str]] | None = None
        self.row: list[str] | None = None
        self.cell: list[str] | None = None
        self.headings: list[tuple[int, str]] = []
        self.hbuf: list[str] | None = None
        self.hlevel = 0
        self.quote = 0
        self.title = ""

    # helpers
    def w(self, s: str):
        if self.cell is not None:
            self.cell.append(s)
        else:
            self.out.append(s)
        if self.hbuf is not None:
            self.hbuf.append(s)

    def nl(self, n: int = 2):
        if self.cell is not None:
            self.cell.append(" ")
            return
        txt = "".join(self.out[-3:])
        have = len(txt) - len(txt.rstrip("\n"))
        if have < n:
            self.out.append("\n" * (n - have))

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "") or ""
        if tag == "article" and "md-content__inner" in cls:
            self.in_article += 1
            return
        if not self.in_article:
            return
        if self.skip:
            if tag == self.skip_tag:
                self.skip += 1
            return
        if tag in self.SKIP or (tag == "a" and "headerlink" in cls):
            self.skip, self.skip_tag = 1, tag
            return
        if self.pre:
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.hlevel = int(tag[1])
            self.nl()
            self.w("#" * self.hlevel + " ")
            self.hbuf = []
        elif tag == "p":
            if "admonition-title" in cls:
                self.nl()
                self.w("**")
                self._admon_title = True
            else:
                self.nl()
        elif tag == "div" and "admonition" in cls:
            self.nl()
            self.quote += 1
            self.nl()
        elif tag == "details":
            self.nl()
            self.quote += 1
            self.nl()
        elif tag == "summary":
            self.w("**")
        elif tag == "blockquote":
            self.quote += 1
            self.nl()
        elif tag == "pre":
            self.pre = 1
            self.nl()
            lang = ""
            m = re.search(r"language-(\w+)", cls)
            if m:
                lang = m.group(1)
            self.w("```" + lang + "\n")
            self._pre_buf: list[str] = []
        elif tag == "code":
            self.code_inline += 1
            self.w("`")
        elif tag in ("strong", "b"):
            self.w("**")
        elif tag in ("em", "i"):
            self.w("*")
        elif tag == "br":
            self.w("  \n" if self.cell is None else " ")
        elif tag == "hr":
            self.nl()
            self.w("---")
            self.nl()
        elif tag in ("ul", "ol"):
            self.lists.append([tag, 0])
            if self.cell is None:
                self.nl(1 if len(self.lists) > 1 else 2)
        elif tag == "li":
            if self.cell is not None:
                self.w(" • ")
                return
            depth = len(self.lists) - 1
            self.nl(1)
            if self.lists and self.lists[-1][0] == "ol":
                self.lists[-1][1] += 1
                bullet = f"{self.lists[-1][1]}. "
            else:
                bullet = "- "
            self.w("  " * max(depth, 0) + bullet)
        elif tag == "a":
            href = a.get("href")
            if href and not href.startswith("#"):
                href = urllib.parse.urljoin(self.page_url, href)
            elif href:
                href = self.page_url + href
            self.links.append(href)
            self.w("[")
        elif tag == "img":
            src = urllib.parse.urljoin(self.page_url, a.get("src", ""))
            alt = (a.get("alt") or "bild").strip()
            self.w(f"![{alt}]({src})")
        elif tag == "table":
            self.table = []
            self.nl()
        elif tag == "tr":
            self.row = []
        elif tag in ("td", "th"):
            self.cell = []

    def handle_endtag(self, tag):
        if tag == "article" and self.in_article:
            self.in_article -= 1
            return
        if not self.in_article:
            return
        if self.skip:
            if tag == self.skip_tag:
                self.skip -= 1
            return
        if self.pre:
            if tag == "pre":
                body = "".join(self._pre_buf).rstrip("\n")
                self.w(body + "\n```")
                self.pre = 0
                self.nl()
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            text = re.sub(r"\s+", " ", "".join(self.hbuf or [])).strip()
            if self.hlevel == 1 and not self.title:
                self.title = text
            self.headings.append((self.hlevel, text))
            self.hbuf = None
            self.nl()
        elif tag == "p":
            if getattr(self, "_admon_title", False):
                self.w("**")
                self._admon_title = False
            self.nl()
        elif tag in ("div",):
            pass
        elif tag == "details" or tag == "blockquote":
            self.quote = max(0, self.quote - 1)
            self.nl()
        elif tag == "summary":
            self.w("**")
            self.nl()
        elif tag == "code":
            self.code_inline = max(0, self.code_inline - 1)
            self.w("`")
        elif tag in ("strong", "b"):
            self.w("**")
        elif tag in ("em", "i"):
            self.w("*")
        elif tag in ("ul", "ol"):
            if self.lists:
                self.lists.pop()
            if self.cell is None:
                self.nl(1 if self.lists else 2)
        elif tag == "a":
            href = self.links.pop() if self.links else None
            self.w(f"]({href})" if href else "]")
        elif tag in ("td", "th"):
            if self.row is not None and self.cell is not None:
                self.row.append(re.sub(r"\s+", " ", "".join(self.cell)).strip().replace("|", "\\|"))
            self.cell = None
        elif tag == "tr":
            if self.table is not None and self.row is not None:
                self.table.append(self.row)
            self.row = None
        elif tag == "table":
            rows = self.table or []
            self.table = None
            if rows:
                width = max(len(r) for r in rows)
                rows = [r + [""] * (width - len(r)) for r in rows]
                self.out.append("| " + " | ".join(rows[0]) + " |\n")
                self.out.append("|" + " --- |" * width + "\n")
                for r in rows[1:]:
                    self.out.append("| " + " | ".join(r) + " |\n")
            self.nl()

    def handle_data(self, data):
        if not self.in_article or self.skip:
            return
        if self.pre:
            self._pre_buf.append(data)
            return
        if self.code_inline:
            self.w(data)
            return
        text = re.sub(r"\s+", " ", data)
        self.w(text)

    def markdown(self) -> str:
        md = "".join(self.out)
        # Städa bara utanför kodblock; kodens indrag ska bevaras.
        parts = re.split(r"(```[^\n]*\n.*?\n```)", md, flags=re.S)
        for i in range(0, len(parts), 2):
            t = re.sub(r"[ \t]+\n", "\n", parts[i])
            t = re.sub(r"\n[ \t]+(?=[^\s\-\d*])", "\n", t)  # blanksteg efter <br>, ej listindrag
            parts[i] = re.sub(r"\n{3,}", "\n\n", t)
        return "".join(parts).strip() + "\n"


import urllib.parse  # noqa: E402  (används i MD)


class AdmonitionAware(MD):
    """Spårar div-djup så att admonitions stängs korrekt."""

    def __init__(self, page_url):
        super().__init__(page_url)
        self.div_stack: list[bool] = []

    def handle_starttag(self, tag, attrs):
        if tag == "div" and self.in_article and not self.skip and not self.pre:
            cls = dict(attrs).get("class", "") or ""
            self.div_stack.append("admonition" in cls)
        super().handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        if tag == "div" and self.in_article and not self.skip and not self.pre and self.div_stack:
            if self.div_stack.pop():
                self.quote = max(0, self.quote - 1)
                self.nl()
        super().handle_endtag(tag)


def convert(html_text: str, url: str) -> tuple[str, str, list[tuple[int, str]]]:
    p = AdmonitionAware(url)
    p.feed(html_text)
    p.close()
    return p.markdown(), p.title, p.headings


# ---------------------------------------------------------------- catalog

def cache_path(loc: str) -> Path:
    loc = loc.strip("/")
    return CACHE / ((loc or "index") + ".md")


def build_catalog(manifest: dict) -> str:
    today = manifest["_meta"]["fetched"]
    groups: dict[str, list] = {}
    for loc, info in manifest["pages"].items():
        sec = loc.split("/")[0] if "/" in loc else ""
        groups.setdefault(sec, []).append((loc, info))
    order = list(SECTION_NAMES)
    keys = sorted(groups, key=lambda s: (order.index(s) if s in order else 99, s))
    lines = [
        "# Katalog över docs.zervicepoint.com",
        "",
        f"Genererad av `scripts/sync_docs.py` {today} från {len(manifest['pages'])} sidor. Redigera inte för hand; kör skriptet igen.",
        "",
        "Varje rad: sidans titel → leverantörens URL → lokal fulltext i `docs-cache/` (finns efter `python scripts/sync_docs.py`). "
        "Raden under en sida listar dess H2/H3-rubriker och fungerar som sökord. Sök med t.ex. `Grep` i `docs-cache/` efter metodnamn eller felkoder.",
        "",
        "## Avsnitt",
        "",
    ]
    for sec in keys:
        name = SECTION_NAMES.get(sec, sec)
        anchor = re.sub(r"[^a-z0-9åäö -]", "", name.lower()).replace(" ", "-")
        lines.append(f"- [{name}](#{anchor}) ({len(groups[sec])})")
    lines.append("")
    for sec in keys:
        name = SECTION_NAMES.get(sec, sec)
        lines += [f"## {name}", ""]
        for loc, info in sorted(groups[sec], key=lambda x: x[0]):
            rel = "../docs-cache/" + cache_path(loc).relative_to(CACHE).as_posix()
            # H2 + H3 som sökord (H3 bär t.ex. metodnamn i JS-referensen och funktioner i release notes)
            heads = [h for lvl, h in info["headings"] if lvl in (2, 3) and h]
            lines.append(f"- **{info['title']}** — [{loc or '/'}]({BASE}{loc}) · [lokal]({rel})")
            if heads:
                cap = 40
                shown = heads[:cap]
                more = f" … (+{len(heads) - cap})" if len(heads) > cap else ""
                lines.append("  - " + " · ".join(shown) + more)
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog-only", action="store_true")
    ap.add_argument("--delay", type=float, default=0.2, help="paus mellan anrop (s)")
    args = ap.parse_args()

    man_path = CACHE / "_manifest.json"
    if args.catalog_only:
        manifest = json.loads(man_path.read_text(encoding="utf-8"))
    else:
        CACHE.mkdir(parents=True, exist_ok=True)
        pages = page_list()
        print(f"{len(pages)} sidor i sökindexet")
        manifest = {"_meta": {"source": BASE, "fetched": dt.date.today().isoformat()}, "pages": {}}
        failed = []
        for i, loc in enumerate(pages, 1):
            url = BASE + loc
            try:
                raw = fetch(url).decode("utf-8", errors="replace")
            except Exception as exc:  # noqa: BLE001
                print(f"[{i}/{len(pages)}] FEL {url}: {exc}", file=sys.stderr)
                failed.append(loc)
                continue
            md, title, heads = convert(raw, url)
            if not title:
                m = re.search(r"<title>(.*?)</title>", raw, re.S)
                title = html.unescape(m.group(1).split(" - ")[0].strip()) if m else loc
            out = cache_path(loc)
            out.parent.mkdir(parents=True, exist_ok=True)
            header = f"<!-- Källa: {url} · hämtad {manifest['_meta']['fetched']} · leverantörens text, lokal cache -->\n\n"
            out.write_text(header + md, encoding="utf-8")
            manifest["pages"][loc] = {"title": title, "url": url, "headings": heads, "chars": len(md)}
            print(f"[{i}/{len(pages)}] {loc or '/'} ({len(md)} tecken)")
            time.sleep(args.delay)
        manifest["_meta"]["failed"] = failed
        man_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    CATALOG.write_text(build_catalog(manifest), encoding="utf-8")
    print(f"Katalog: {CATALOG.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
