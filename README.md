# AI for grant writing

A LaTeX grant-writing workflow with an AI-assisted reviewers.

## Overview

This repository helps you organize grant writing into reusable sections, configurable build settings, and reusable review prompts so you can:

1. Draft proposals in modular LaTeX files.
2. Keep references, figures, abstract, timeline, and budget in a predictable layout.
3. Build a main proposal PDF plus standalone attachment PDFs.
4. Run AI-assisted quality checks before submission.

## Intended structure

The directory tree shown below:

```text
CV/                                      # CV templates
Information/                             # Grant call details and requirements
Examples/                                # Example proposals
Proposal/
    figures/                             # Figures and diagrams
    literatures/                         # Supporting papers and references
    PDF/                                 # Compiled PDFs
    sections/                            # Modular LaTeX sections
        abstract.tex                     # Standalone abstract PDF source
        budget.tex                       # Standalone budget PDF source
        main.tex                         # Main LaTeX entry point
        main_<id>_<section>.tex          # Section files
        timeline.tex                     # Standalone timeline / Gantt PDF source
        setup/                           # Shared LaTeX setup files
        references.bib                   # Bibliography
    build.sh                             # Build script to compile the proposal
    generate_tex_config.py               # YAML -> TeX config generator
    tex_config.yaml                      # User-editable metadata and layout settings
Review/                                  # AI review prompts, rubrics, examples, and outputs
    examples/nsfc-reviewers/             # Reference skill and reviewer examples
    R1_Language/                         # Review typos, grammar, and clarity
    R2_Citation/                         # Review for appropriate and comprehensive citations
    R3_StateOfTheArt/                    # Review for state-of-the-art awareness
    R4_Innovation/                       # Review for novelty and impact
    R5_Hypothesis/                       # Review for hypothesis clarity and testability
    R6_Methodology/                      # Review for methodology feasibility and rigor
    R7_ResearchFoundation/               # Review for research foundation and preliminary data
    R8_Critical/                         # Critical review of weaknesses and risks
    R8_Constructive/                     # Constructive review with suggestions for improvement
    R10_Significance/                    # Review for significance and potential impact
    Aggergation/                         # Reserved for aggregated review notes
    Requirements/                        # Reserved for grant-specific review checklists
    Reviews/                             # Final review outputs and iteration notes
    metaReviewer.md                      # Master reviewer template
    README.md                            # Review usage guide
```

## Getting Started

1. Edit [Proposal/tex_config.yaml](./Proposal/tex_config.yaml:1) to set the proposal title, applicant name, affiliation, and layout parameters.
   `Proposal/build.sh` expects `python3`, `latexmk`, and a working LaTeX installation in your shell path.
2. Write or replace content in `Proposal/sections/main_<id>_<section>.tex`.
3. Update [Proposal/sections/references.bib](./Proposal/sections/references.bib:1) with your citations.
4. Build from [Proposal/build.sh](./Proposal/build.sh:1). This produces:
   - `Proposal/PDF/main.pdf`
   - `Proposal/PDF/abstract.pdf`
   - `Proposal/PDF/timeline.pdf`
   - `Proposal/PDF/budget.pdf`
5. Use the reviewer prompts in `AIReview/RX_XXX/` to generate targeted review notes into `AIReview/Reviews/`.
6. Iterate on the proposal until both the writing and the reviewer outputs are in good shape.

## Customization

- Adjust fonts, spacing, title block content, and margins in [Proposal/tex_config.yaml](./Proposal/tex_config.yaml:1).
- Use a YAML block scalar (`|`) for multi-line title fields in `tex_config.yaml` so line breaks become proper TeX title breaks.
- Modify the reviewer instructions under `AIReview/RX_XXX/` to match the evaluation criteria of your target funder.
- Use `AIReview/metaReviewer.md` as the canonical template for defining a reviewer persona.
- Add any additional proposal sections, figures, or reviewer roles as needed.

# Acknowledgements

Thanks to [ChineseResearchLaTeX](https://github.com/huangwb8/ChineseResearchLaTeX) for providing flexible and adaptable for various grant writing needs, and we encourage contributions and improvements from the community.
