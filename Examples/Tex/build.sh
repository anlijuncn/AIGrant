#!/bin/sh

set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname "$0")" && pwd)
LOG_DIR="$SCRIPT_DIR/logs"

mkdir -p "$LOG_DIR"

cd "$SCRIPT_DIR"

rm -f \
  "$LOG_DIR/main.aux" \
  "$LOG_DIR/main.bbl" \
  "$LOG_DIR/main.blg" \
  "$LOG_DIR/main.fdb_latexmk" \
  "$LOG_DIR/main.fls" \
  "$LOG_DIR/main.log" \
  "$LOG_DIR/main.pdf" \
  "$LOG_DIR/main.out" \
  "$LOG_DIR/main.run.xml"

latexmk \
  -pdf \
  -interaction=nonstopmode \
  -output-directory="$LOG_DIR" \
  main.tex

mv "$LOG_DIR/main.pdf" "$SCRIPT_DIR/main.pdf"
