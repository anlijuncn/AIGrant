# GrantTemplate

A LaTeX grant-writing template with an AI-assisted review workflow.

## Overview

GrantTemplate helps you organize grant writing into reusable sections, supporting files, and review artifacts so you can:

1. Draft proposals in modular LaTeX files.
2. Keep references, figures, timeline, and budget in a predictable layout.
3. Run AI-assisted quality checks before submission.

## Intended structure

The directory tree shown below:

```text
CV/                                  # CV templates
Information/                         # Grant call details and requirements
Examples/                            # Example proposals
Proposal/
    figures/                         # Figures and diagrams
    literatures/                     # Supporting papers and references
    PDF/                             # Compiled PDFs and logs
    sections/                        # Modular LaTeX sections
        abstract.tex                     # Abstract section
        budget.tex                       # Budget section
        main.tex                         # Main LaTeX entry point
        main_<id>_<section>.tex          # Section files
        timeline.tex                     # Timeline / Gantt section
        references.bib                   # Bibliography
    build.sh                         # Build script to compile the proposal
Review/                              # AI review prompts, rubrics, and outputs
    GrantRequirements/                   # Checklists based on grant call criteria
    R1_Language/                         # Review typos, grammar, and clarity
    R2_Citation/                         # Review for appropriate and comprehensive citations
    R3_StateOfTheArt/                    # Review for state-of-the-art awareness
    R4_Innovation/                       # Review for novelty and impact
    R5_Methodology/                      # Review for methodology feasibility and rigor
    R6_ResearchFoundation/               # Review for research foundation and preliminary data
    R7_Critical/                         # Critical review of weaknesses and risks
    R8_Constructive/                     # Constructive review with suggestions for improvement
    R9_Significance/                     # Review for significance and potential impact
    Aggregation/                         # Aggregated review outputs and iteration notes
    Reviews/                             # Final review outputs and iteration notes
    config.yaml                          # Configuration for AI review workflow
```

## Getting Started

1. Read and modify all `instructions.md` files to fit the specific grant call you are targeting.
2. Add your proposal text into `grant/proposal/*.tex` files.
3. Keep citations in `grant/proposal/references.bib`.
4. Build from `grant/proposal/main.tex`.
5. Use the `grant/review/` directory to store AI review prompts, outputs, and iteration notes as you refine your proposal.
6. Iterate on the proposal based on AI feedback until you have a polished final version ready for submission.

## Customization

- Modify the LaTeX templates in `grant/proposal/` to match the formatting requirements of your target grant.
- Update the AI review prompts in `grant/review/` to align with the specific evaluation criteria of the grant call.
- Add any additional sections or supporting files as needed to strengthen your proposal

# Acknowledgements

Thanks to https://github.com/huangwb8/ChineseResearchLaTeX for providing flexible and adaptable for various grant writing needs, and we encourage contributions and improvements from the community.
