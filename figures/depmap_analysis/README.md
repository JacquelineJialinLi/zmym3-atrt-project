# DepMap Analysis Figures

This folder contains all figures produced by the DepMap-analysis notebooks
(`notebooks/depmap_analysis/`). Each figure is saved in both PDF and PNG format.

## Main figures

| File | Notebook | Description |
|------|----------|-------------|
| `fig1_venn_atrt.{pdf,png}` | 02 | Venn diagram of the three statistical tests (Fisher's exact, t-test, Wilcoxon) for the AT/RT indication. The three-way intersection lists the consensus context-specific fitness genes — SMARCD1, ZMYM3, and NABP2. |
| `fig2a_ZMYM3_dep.{pdf,png}` | 02 | Boxplot of ZMYM3 gene-effect (Chronos) scores across every cancer indication with ≥ 4 cell lines. AT/RT (highlighted red) shows the most negative median score, indicating the strongest dependency. |
| `fig2b_ZMYM3_expression.{pdf,png}` | 03 | Boxplot of ZMYM3 bulk RNA-seq expression (log2[TPM+1]) across the same indications, drawn from CCLE. Used to test whether the AT/RT dependency is explained by elevated transcript expression — it is not. |
| `fig3_ZMYM3_codep_volcano.{pdf,png}` | 03 | Volcano plot of Pearson correlations between ZMYM3 and every other gene's dependency profile across all DepMap cell lines. Significant SWI/SNF and CoREST members (SMARCD1, SMARCC1, ARID1B, ZMYM4, HMG20B, KDM1A) are labeled. |

## Supplementary figures

| File | Notebook | Description |
|------|----------|-------------|
| `figS1_venn_multi.{pdf,png}` | 02 | Multi-panel Venn diagrams for additional indications that yielded consensus hits, demonstrating that the three-test framework recovers established positive controls (e.g., BRAF in melanoma, KRAS in PDAC). |
| `figS2_ZMYM3_atrt_scores.{pdf,png}` | 03 | Histogram of ZMYM3 gene-effect scores for all non-AT/RT cell lines, with individual AT/RT cell lines overlaid as vertical lines. Visualizes where each AT/RT line falls within the global distribution. |

## Extra (not in the manuscript)

| File | Notebook | Description |
|------|----------|-------------|
| `fig_extra_ZMYM3_specificity_fdr.{pdf,png}` | 02 | Histogram of BH-corrected FDR values from the pairwise specificity test (AT/RT vs. each other indication, one-sided Wilcoxon). Visualizes how broadly AT/RT outranks other indications in ZMYM3 dependency. |
