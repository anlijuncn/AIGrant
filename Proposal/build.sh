#!/bin/sh

set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname "$0")" && pwd)
PDF_DIR="$SCRIPT_DIR/PDF"

mkdir -p "$PDF_DIR"

cd "$SCRIPT_DIR"

export BIBINPUTS="$SCRIPT_DIR:$SCRIPT_DIR/sections:$PDF_DIR:"
export BSTINPUTS="$SCRIPT_DIR:$SCRIPT_DIR/sections:"

for target in main timeline budget; do
  rm -f \
    "$PDF_DIR/$target.aux" \
    "$PDF_DIR/$target.bbl" \
    "$PDF_DIR/$target.blg" \
    "$PDF_DIR/$target.fdb_latexmk" \
    "$PDF_DIR/$target.fls" \
    "$PDF_DIR/$target.log" \
    "$PDF_DIR/$target.pdf" \
    "$PDF_DIR/$target.out" \
    "$PDF_DIR/$target.run.xml"

  latexmk \
    -pdf \
    -interaction=nonstopmode \
    -output-directory="$PDF_DIR" \
    "sections/$target.tex"

  rm -f \
    "$PDF_DIR/$target.aux" \
    "$PDF_DIR/$target.bbl" \
    "$PDF_DIR/$target.blg" \
    "$PDF_DIR/$target.fdb_latexmk" \
    "$PDF_DIR/$target.fls" \
    "$PDF_DIR/$target.log" \
    "$PDF_DIR/$target.out" \
    "$PDF_DIR/$target.run.xml"
done
