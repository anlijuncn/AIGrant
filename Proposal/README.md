# Proposal writing

This directory contains the grant proposal template, build script, user-editable
configuration, section files, figures, and compiled PDFs.

## Directory Layout

- `tex_config.yaml`: proposal metadata and layout settings
- `build.sh`: compiles all proposal PDFs
- `generate_tex_config.py`: converts YAML settings into TeX macros
- `sections/main.tex`: main proposal entry point
- `sections/abstract.tex`: standalone abstract PDF
- `sections/timeline.tex`: standalone timeline PDF
- `sections/budget.tex`: standalone budget PDF
- `sections/main_<id>_<section>.tex`: modular main proposal sections
- `sections/references.bib`: bibliography database
- `figures/`: reusable figure files
- `PDF/`: generated PDFs

## Requirements

`build.sh` expects these tools in your shell path:

- `python3`
- `latexmk`
- a working LaTeX installation

## Build

From this directory, run:

```sh
./build.sh
```

This regenerates the TeX config and builds:

- `PDF/main.pdf`
- `PDF/abstract.pdf`
- `PDF/timeline.pdf`
- `PDF/budget.pdf`

The script also removes generated LaTeX aux/log files after each build.

## Update Configuration

Edit `tex_config.yaml` to change:

- applicant name and affiliation
- proposal title and attachment titles
- font size and paper size
- line spacing
- margins
- section and title spacing
- bibliography style

Example:

```yaml
metadata:
  applicant_name: "Jane Doe"
  affiliation: "Example University"
  proposal_title: |
    Mechanism-Guided Biomarker Discovery
    for Precision Therapy

document:
  font_size: "11pt"

layout:
  line_spacing: "0.98"
  margin_left: "1.5cm"
  margin_right: "1.5cm"

bibliography:
  style: "unsrtnat"
```

Use the YAML block scalar `|` for multi-line titles. Each line becomes a TeX line
break in the generated title.

After changing `tex_config.yaml`, rerun `./build.sh`.

## Edit Proposal Content

The main narrative is assembled in `sections/main.tex` by including files such as:

- `sections/main_01_background.tex`
- `sections/main_02_preliminary_work.tex`
- `sections/main_03_aim.tex`

To update the proposal:

1. Edit the existing `main_<id>_<section>.tex` files.
2. Add new section files if needed.
3. Include any new file from `sections/main.tex` in the correct order.

Keep `abstract.tex`, `timeline.tex`, and `budget.tex` separate if they should stay
as standalone attachments.

## Insert Figures

There are two common patterns.

### Option 1: Reusable TeX/TikZ figure

Put a figure source file under `figures/`, for example `figures/my_diagram.tex`,
then include it from a section:

```tex
\begin{figure}[t]
  \centering
  \input{figures/my_diagram}
  \caption{Workflow overview.}
  \label{fig:workflow}
\end{figure}
```

This is how the demo figure is included in `sections/main_01_background.tex`.

### Option 2: External image file

If you have a PNG, JPG, or PDF figure under `figures/`, use `\includegraphics`:

```tex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.85\linewidth]{figures/my_plot}
  \caption{Representative result.}
  \label{fig:result}
\end{figure}
```

Notes:

- keep figure filenames simple and stable
- always add `\caption{...}` and `\label{...}`
- refer to figures in text with `\cref{fig:workflow}` or `\ref{fig:workflow}`

## Insert Citations

Add BibTeX entries to `sections/references.bib`, for example:

```bibtex
@article{smith2026example,
  author  = {Smith, Alex and Lee, Jordan},
  title   = {Example Study Title},
  journal = {Journal of Examples},
  year    = {2026},
  volume  = {12},
  number  = {3},
  pages   = {100--112}
}
```

Then cite that key in your section files:

```tex
This approach builds on prior work.\citep{smith2026example}
```

Common citation commands with the current template:

- `\citep{key}`: parenthetical citation
- `\citet{key}`: textual citation

After adding or changing references, rerun `./build.sh`.

## Common Workflow

1. Update metadata and spacing in `tex_config.yaml`.
2. Draft or revise `sections/main_<id>_<section>.tex`.
3. Add figures under `figures/`.
4. Add BibTeX entries to `sections/references.bib`.
5. Run `./build.sh`.
6. Check the PDFs under `PDF/`.

## Troubleshooting

- If `./build.sh` says `Missing required command`, install the missing tool and run again.
- If a title line break renders incorrectly, switch that YAML field to the `|` multiline format.
- If citations show as undefined, make sure the BibTeX key in the `.tex` file matches the key in `sections/references.bib`.
- If a figure does not appear, check the file path under `figures/` and confirm the figure file is included from the correct section.
