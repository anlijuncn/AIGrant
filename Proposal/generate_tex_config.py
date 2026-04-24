#!/usr/bin/env python3
"""Generate TeX config macros from tex_config.yaml."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except Exception:  # pragma: no cover - optional dependency
    yaml = None


DEFAULTS = {
    "metadata": {
        "applicant_name": "Your Name",
        "affiliation": "Your Institution",
        "project_short_title": "Demo Grant Template",
        "proposal_title": "Demo Proposal Title:\nCompact Grant Narrative Template",
        "abstract_title": "Project Abstract",
        "timeline_title": "Project Timeline",
        "budget_title": "Budget Summary",
    },
    "document": {
        "font_size": "11pt",
        "paper_size": "a4paper",
    },
    "layout": {
        "title_top_vspace": "-2.2em",
        "main_title_bottom_vspace": "-6em",
        "standalone_title_bottom_vspace": "-4.5em",
        "line_spacing": "0.98",
        "paragraph_indent": "0pt",
        "paragraph_skip": "3pt",
        "margin_left": "1.7cm",
        "margin_right": "1.7cm",
        "margin_top": "2.0cm",
        "margin_bottom": "2.0cm",
        "headheight": "14pt",
        "headsep": "8pt",
        "footskip": "14pt",
        "caption_skip": "3pt",
        "textfloat_sep": "8pt plus 1pt minus 1pt",
        "float_sep": "6pt plus 1pt minus 1pt",
        "intext_sep": "6pt plus 1pt minus 1pt",
        "section_before_space": "5pt plus 1pt minus 1pt",
        "section_after_space": "2pt",
        "subsection_before_space": "4pt plus 1pt minus 1pt",
        "subsection_after_space": "2pt",
        "subsubsection_before_space": "3pt plus 1pt minus 1pt",
        "subsubsection_after_space": "1pt",
        "header_rule_width": "0.3pt",
        "footer_rule_width": "0pt",
    },
    "bibliography": {
        "style": "unsrtnat",
    },
}


MACRO_MAP = [
    ("DocumentFontSize", "document", "font_size"),
    ("PaperSize", "document", "paper_size"),
    ("ApplicantName", "metadata", "applicant_name"),
    ("ApplicantAffiliation", "metadata", "affiliation"),
    ("ProjectShortTitle", "metadata", "project_short_title"),
    ("ProposalTitle", "metadata", "proposal_title"),
    ("AbstractTitle", "metadata", "abstract_title"),
    ("TimelineTitle", "metadata", "timeline_title"),
    ("BudgetTitle", "metadata", "budget_title"),
    ("TitleTopVSpace", "layout", "title_top_vspace"),
    ("MainTitleBottomVSpace", "layout", "main_title_bottom_vspace"),
    ("StandaloneTitleBottomVSpace", "layout", "standalone_title_bottom_vspace"),
    ("LineStretchValue", "layout", "line_spacing"),
    ("ParagraphIndent", "layout", "paragraph_indent"),
    ("ParagraphSkip", "layout", "paragraph_skip"),
    ("MarginLeft", "layout", "margin_left"),
    ("MarginRight", "layout", "margin_right"),
    ("MarginTop", "layout", "margin_top"),
    ("MarginBottom", "layout", "margin_bottom"),
    ("HeadHeight", "layout", "headheight"),
    ("HeadSep", "layout", "headsep"),
    ("FootSkip", "layout", "footskip"),
    ("CaptionSkip", "layout", "caption_skip"),
    ("TextFloatSep", "layout", "textfloat_sep"),
    ("FloatSep", "layout", "float_sep"),
    ("InTextSep", "layout", "intext_sep"),
    ("SectionBeforeSpace", "layout", "section_before_space"),
    ("SectionAfterSpace", "layout", "section_after_space"),
    ("SubsectionBeforeSpace", "layout", "subsection_before_space"),
    ("SubsectionAfterSpace", "layout", "subsection_after_space"),
    ("SubsubsectionBeforeSpace", "layout", "subsubsection_before_space"),
    ("SubsubsectionAfterSpace", "layout", "subsubsection_after_space"),
    ("HeaderRuleWidth", "layout", "header_rule_width"),
    ("FooterRuleWidth", "layout", "footer_rule_width"),
    ("BibliographyStyle", "bibliography", "style"),
]


def stringify(value: object) -> str:
    text = str(value)
    text = text.replace("\r\n", "\n").rstrip("\n")
    return text.replace("\n", "\\\\")


def load_yaml_with_ruby(path: Path) -> dict:
    ruby = shutil.which("ruby")
    if ruby is None:
        raise SystemExit(
            "Unable to parse tex_config.yaml: neither PyYAML nor Ruby with the "
            "standard YAML library is available."
        )

    ruby_program = """
require "json"
require "yaml"
data = Psych.safe_load(File.read(ARGV[0]), aliases: true)
STDOUT.write(JSON.dump(data || {}))
"""

    try:
        result = subprocess.run(
            [ruby, "-e", ruby_program, str(path)],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as exc:
        message = exc.stderr.strip() or exc.stdout.strip() or str(exc)
        raise SystemExit(f"Invalid YAML in {path}: {message}") from exc

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Failed to decode YAML parser output for {path}: {exc}") from exc

    if data is None:
        return {}
    if not isinstance(data, dict):
        raise SystemExit(f"Top-level YAML object in {path} must be a mapping.")
    return data


def load_yaml(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"Missing config file: {path}")

    if yaml is None:
        return load_yaml_with_ruby(path)

    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise SystemExit(f"Invalid YAML in {path}: {exc}") from exc

    if data is None:
        return {}
    if not isinstance(data, dict):
        raise SystemExit(f"Top-level YAML object in {path} must be a mapping.")
    return data


def get_value(data: dict, section: str, key: str) -> str:
    section_data = data.get(section, {})
    if not isinstance(section_data, dict):
        section_data = {}

    value = section_data.get(key, DEFAULTS[section][key])
    return stringify(value)


def build_tex(data: dict) -> str:
    font_size = get_value(data, "document", "font_size")
    paper_size = get_value(data, "document", "paper_size")

    lines = [
        "% Auto-generated from tex_config.yaml by generate_tex_config.py.",
        "% Edit tex_config.yaml instead of this file.",
        f"\\PassOptionsToClass{{{font_size},{paper_size}}}{{article}}",
    ]

    for macro, section, key in MACRO_MAP:
        lines.append(f"\\providecommand{{\\{macro}}}{{{get_value(data, section, key)}}}")

    lines.append("")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("Usage: generate_tex_config.py <tex_config.yaml> <generated_config.tex>", file=sys.stderr)
        return 1

    config_path = Path(argv[1])
    output_path = Path(argv[2])

    output_path.write_text(build_tex(load_yaml(config_path)), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
