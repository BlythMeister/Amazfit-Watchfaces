#!/usr/bin/env python3

from __future__ import annotations

import html
import re
import shutil
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
DOCS_PATH = ROOT / "docs"
DEVICES_PATH = DOCS_PATH / "devices"
INDEX_PATH = DOCS_PATH / "index.md"
HEADER_PATH = DOCS_PATH / "_includes" / "header.html"

SERIES_RE = re.compile(r"^###\s+(.+?)\s*$")
DEVICE_RE = re.compile(r"^####\s+(.+?)\s*$")
TABLE_ROW_RE = re.compile(
    r"^\|\s*\[(?P<design>.+?)\]\((?P<src>[^)]+)\)\s*\|\s*(?P<version>[^|]+?)\s*\|\s*(?P<description>.+?)\s*\|\s*(?P<preview><img.+?>)\s*\|\s*(?P<installation>.+?)\s*\|\s*$"
)
SEARCH_ID_RE = re.compile(r"Search\s+`([^`]+)`")
SIDELOAD_RE = re.compile(r"\((https?://[^)]+)\)")
ALT_RE = re.compile(r'alt="([^"]+)"')


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def parse_readme() -> list[dict]:
    lines = README_PATH.read_text(encoding="utf-8").splitlines()
    in_watchfaces = False
    current_series: dict | None = None
    current_device: dict | None = None
    series_data: list[dict] = []

    for line in lines:
        stripped = line.strip()

        if stripped == "## Watchfaces":
            in_watchfaces = True
            continue

        if in_watchfaces and stripped.startswith("## ") and stripped != "## Watchfaces":
            break

        if not in_watchfaces:
            continue

        series_match = SERIES_RE.match(stripped)
        if series_match:
            current_series = {"name": series_match.group(1), "devices": []}
            series_data.append(current_series)
            current_device = None
            continue

        device_match = DEVICE_RE.match(stripped)
        if device_match and current_series is not None:
            device_name = device_match.group(1)
            current_device = {
                "name": device_name,
                "slug": slugify(device_name),
                "faces": [],
            }
            current_series["devices"].append(current_device)
            continue

        row_match = TABLE_ROW_RE.match(stripped)
        if row_match and current_device is not None:
            installation = row_match.group("installation")
            search_id_match = SEARCH_ID_RE.search(installation)
            sideload_match = SIDELOAD_RE.search(installation)
            alt_match = ALT_RE.search(row_match.group("preview"))

            if search_id_match is None or sideload_match is None:
                raise ValueError(f"Unable to parse installation column for row: {stripped}")

            src_dir = unquote(row_match.group("src")).strip("/")
            current_device["faces"].append(
                {
                    "design": row_match.group("design").strip(),
                    "description": row_match.group("description").strip(),
                    "src_dir": src_dir,
                    "image": f"{Path(src_dir).name.replace(' ', '')}.gif",
                    "alt": alt_match.group(1).strip() if alt_match else "Watchface animated preview",
                    "official_id": search_id_match.group(1).strip(),
                    "sideload_url": sideload_match.group(1).strip(),
                }
            )

    return series_data


def render_device_page(device: dict) -> str:
    lines = [
        "---",
        f"title: {device['name']}",
        f'description: "Amazfit {device["name"]} Watchfaces"',
        "---",
        "",
        f"## {device['name']}",
    ]

    for face in device["faces"]:
        lines.extend(
            [
                "",
                f"### {face['design']}",
                "",
                "<table>",
                "  <tr>",
                "    <td class=\"watch-img\">",
                f'      <img src="/images/{face["image"]}" alt="{html.escape(face["alt"], quote=True)}">',
                "    </td>",
                "    <td class=\"watch-desc\">",
                f"      <p>{html.escape(face['description'])}</p>",
                "      <p>",
                f"        <strong>Official:</strong> Search <code>{html.escape(face['official_id'])}</code> on Zepp watch face store<br/>",
                f'        <strong>Sideload:</strong> <a href="{html.escape(face["sideload_url"], quote=True)}">amazfitwatchfaces.com</a>',
                "      </p>",
                "    </td>",
                "  </tr>",
                "</table>",
            ]
        )

    return "\n".join(lines) + "\n"


def render_index(series_data: list[dict]) -> str:
    lines = [
        "---",
        "title: Home",
        'description: "Amazfit Watchfaces"',
        "---",
        "",
        "A collection of custom watchfaces for Amazfit devices.",
        "",
        "## Installation",
        "",
        "Each face can be installed via a sideload from [amazfitwatchfaces.com](https://amazfitwatchfaces.com) or by searching the ID number in the Zepp watchface store within the Zepp app.",
        "",
        "## Devices",
        "",
    ]

    for series in series_data:
        lines.append(f"### {series['name']}")
        lines.append("")
        for device in series["devices"]:
            lines.append(f"* [{device['name']}](devices/{device['slug']})")
        lines.append("")

    return "\n".join(lines)


def render_header(series_data: list[dict]) -> str:
    desktop_series_blocks: list[str] = []
    mobile_series_blocks: list[str] = []

    for series in series_data:
        dropdown_lines = [
            '        <li class="dropdown" role="presentation">',
            '            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">',
            f"                {series['name']} <span class=\"caret\"></span>",
            "            </a>",
            '            <ul class="dropdown-menu">',
        ]
        for device in series["devices"]:
            dropdown_lines.append(
                f'                <li><a href="{{{{ site.url }}}}/devices/{device["slug"]}">{device["name"]}</a></li>'
            )
        dropdown_lines.extend([
            "            </ul>",
            "        </li>",
        ])
        desktop_series_blocks.append("\n".join(dropdown_lines))

        mobile_lines = [
            "                <li role=\"separator\" class=\"divider\"></li>",
            f'                <li class="dropdown-header">{series["name"]}</li>',
        ]
        for device in series["devices"]:
            mobile_lines.append(
                f'                <li><a href="{{{{ site.url }}}}/devices/{device["slug"]}">{device["name"]}</a></li>'
            )
        mobile_series_blocks.append("\n".join(mobile_lines))

    return "\n".join(
        [
            '<div class="col-lg-12">',
            "    <h1>",
            "        Amazfit Watchface By Chris",
            "    </h1>",
            "</div>",
            '<div class="col-lg-12 nav">',
            "    <!-- Desktop Navigation -->",
            '    <ul class="nav nav-pills nav-justified hidden-xs">',
            '        <li role="presentation"><a href="{{ site.url }}/">Home</a></li>',
            "",
            *desktop_series_blocks,
            "",
            '        <li role="presentation"><a href="{{ site.url }}/donations-mailing-list">Donations &amp; Mailing List</a></li>',
            '        <li role="presentation"><a href="{{ site.url }}/help">Help</a></li>',
            "    </ul>",
            "",
            "    <!-- Mobile Navigation -->",
            '    <ul class="nav nav-pills nav-justified hidden-sm hidden-md hidden-lg">',
            '        <li class="dropdown">',
            '            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Navigation <span class="caret"></span></a>',
            '            <ul class="dropdown-menu dropdown-menu-justified">',
            '                <li role="presentation"><a href="{{ site.url }}/">Home</a></li>',
            "",
            *mobile_series_blocks,
            "",
            '                <li role="separator" class="divider"></li>',
            '                <li role="presentation"><a href="{{ site.url }}/donations-mailing-list">Donations &amp; Mailing List</a></li>',
            '                <li role="presentation"><a href="{{ site.url }}/help">Help</a></li>',
            "            </ul>",
            "        </li>",
            "    </ul>",
            "</div>",
            "",
        ]
    )


def sync_preview_images(series_data: list[dict]) -> None:
    images_dir = DOCS_PATH / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    expected_paths: set[Path] = set()

    for series in series_data:
        for device in series["devices"]:
            for face in device["faces"]:
                source = ROOT / face["src_dir"] / "Preview.gif"
                if not source.exists():
                    raise FileNotFoundError(f"Missing Preview.gif for {face['src_dir']}")
                output_path = images_dir / face["image"]
                shutil.copyfile(source, output_path)
                expected_paths.add(output_path)

    for existing in images_dir.glob("*.gif"):
        if existing not in expected_paths:
            existing.unlink()


def sync_device_pages(series_data: list[dict]) -> None:
    DEVICES_PATH.mkdir(parents=True, exist_ok=True)
    expected_slugs: set[str] = set()

    for series in series_data:
        for device in series["devices"]:
            expected_slugs.add(device["slug"])
            device_dir = DEVICES_PATH / device["slug"]
            device_dir.mkdir(parents=True, exist_ok=True)
            (device_dir / "index.md").write_text(render_device_page(device), encoding="utf-8")

    for existing_dir in DEVICES_PATH.iterdir():
        if existing_dir.is_dir() and existing_dir.name not in expected_slugs:
            shutil.rmtree(existing_dir)


def main() -> None:
    series_data = parse_readme()
    sync_preview_images(series_data)
    sync_device_pages(series_data)
    INDEX_PATH.write_text(render_index(series_data), encoding="utf-8")
    HEADER_PATH.write_text(render_header(series_data), encoding="utf-8")


if __name__ == "__main__":
    main()
