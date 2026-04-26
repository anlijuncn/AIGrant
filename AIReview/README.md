# Review Instructions

This directory stores reusable reviewer prompts, review templates, and review outputs for proposal-quality checks.

## What Is Here

- [metaReviewer.md](../AIReview/metaReviewer.md): the canonical template for defining a reviewer persona
- `examples/nsfc-reviewers/`: a richer NSFC-oriented reference skill with expert personas, aggregation rules, and prompt design examples
- [R1_Language/R1_reviewer.md](../AIReview/R1_Language/R1_reviewer.md): readability and language reviewer
- [R2_Citation/R2_reviewer.md](../AIReview/R2_Citation/R2_reviewer.md): citation strategy reviewer
- [R3_StateOfTheArt/R3_reviewer.md](../AIReview/R3_StateOfTheArt/R3_reviewer.md): state-of-the-art positioning reviewer
- [R4_Innovation/R4_reviewer.md](../AIReview/R4_Innovation/R4_reviewer.md): innovation reviewer
- [R5_Hypothesis/R5_reviewer.md](../AIReview/R5_Hypothesis/R5_reviewer.md): hypothesis reviewer
- [R6_Methodology/R6_reviewer.md](../AIReview/R6_Methodology/R6_reviewer.md): methodology reviewer
- [R7_ResearchFoundation/R7_reviewer.md](../AIReview/R7_ResearchFoundation/R7_reviewer.md): research foundation and team reviewer
- [R8_Constructive/R8_reviewer.md](../AIReview/R8_Constructive/R8_reviewer.md): constructive revision reviewer
- [R8_Critical/R8_reviewer.md](../AIReview/R8_Critical/R8_reviewer.md): strict comprehensive reviewer
- [R10_Significance/R10_reviewer.md](../AIReview/R10_Significance/R10_reviewer.md): significance and field-impact reviewer
- `Reviews/`: suggested location for generated review outputs
- `Aggregation/`, `Requirements/`: reserved for aggregation rules and grant-specific checklists

## How To Use

1. Put the proposal text under `../Proposal/sections/` and make sure the draft reflects the current version you want reviewed.
2. Pick one reviewer instruction file from `../AIReview/RX_XXX/`.
3. Ask the AI to read both the proposal and the reviewer file, then save the review into `../AIReview/Reviews/`.

Example prompt:

```text
Read ../Proposal/sections and review this proposal using ../AIReview/R4_Innovation/R4_reviewer.md.
Save the output to ../AIReview/Reviews/R4_Innovation_Review.md.
```

## Suggested Workflow

1. Run focused reviews first:
   - `R4_Innovation`
   - `R5_Hypothesis`
   - `R6_Methodology`
2. Run support reviews next:
   - `R7_ResearchFoundation`
   - `R10_Significance`
   - `R2_Citation`
   - `R3_StateOfTheArt`
3. Run language and final-pass reviewers last:
   - `R1_Language`
   - `R8_Critical`
   - `R8_Constructive`
4. Consolidate repeated findings into a short revision plan in `../AIReview/Reviews/`.

## How To Create A New Reviewer

1. Start from [metaReviewer.md](../AIReview/metaReviewer.md).
2. Copy the template into a new reviewer file under the target `R*` directory.
3. Fill in:
   - reviewer identity
   - review dimensions
   - review style
   - output path
4. Keep the issue template and final stage judgement format unchanged so all reviewers produce compatible outputs.

## Notes

- The current repository keeps the directory names exactly as they exist today, including `Aggregation` and `R8_Constructive`.
- [metaReviewer.md](../AIReview/metaReviewer.md) is the canonical reviewer template for this repository.
