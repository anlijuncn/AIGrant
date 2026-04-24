#!/bin/sh

set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname "$0")" && pwd)
PDF_DIR="$SCRIPT_DIR/PDF"
CONFIG_FILE="$SCRIPT_DIR/tex_config.yaml"
GENERATED_CONFIG="$SCRIPT_DIR/sections/setup/generated_config.tex"

mkdir -p "$PDF_DIR"

cd "$SCRIPT_DIR"

export BIBINPUTS="$SCRIPT_DIR:$SCRIPT_DIR/sections:$PDF_DIR:"
export BSTINPUTS="$SCRIPT_DIR:$SCRIPT_DIR/sections:"

require_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Missing required command: $1" >&2
    exit 1
  fi
}

cleanup_target() {
  target=$1

  rm -f \
    "$PDF_DIR/$target.aux" \
    "$PDF_DIR/$target.bbl" \
    "$PDF_DIR/$target.blg" \
    "$PDF_DIR/$target.fdb_latexmk" \
    "$PDF_DIR/$target.fls" \
    "$PDF_DIR/$target.log" \
    "$PDF_DIR/$target.nav" \
    "$PDF_DIR/$target.out" \
    "$PDF_DIR/$target.run.xml" \
    "$PDF_DIR/$target.snm" \
    "$PDF_DIR/$target.synctex.gz" \
    "$PDF_DIR/$target.toc"
}

require_cmd python3
require_cmd latexmk

python3 -B "$SCRIPT_DIR/generate_tex_config.py" "$CONFIG_FILE" "$GENERATED_CONFIG"

for target in main abstract timeline budget; do
  cleanup_target "$target"
  rm -f "$PDF_DIR/$target.pdf"

  latexmk \
    -pdf \
    -interaction=nonstopmode \
    -output-directory="$PDF_DIR" \
    "sections/$target.tex"

  cleanup_target "$target"
done
