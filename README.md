# ZMYM3 as a Context-Specific Dependency in Atypical Teratoid/Rhabdoid Tumor

**Authors:** Jacqueline Li and Daniel Stauber

**Course:** 20.440 Final Project

**Date:** Spring 2026

---

## Project Overview

This repository contains the analysis code for our final project investigating **ZMYM3** as a candidate context-specific therapeutic dependency in Atypical Teratoid/Rhabdoid Tumor (AT/RT), a lethal pediatric brain tumor defined by biallelic loss of *SMARCB1*.

We took a two-stage computational approach:

1. **CRISPR DepMap dependency screening** — We used Chronos-corrected gene-effect scores from the DepMap 26Q1 release (1,208 cell lines × 18,531 genes) to identify genes selectively essential in AT/RT cell lines compared to all other cancer types. Using a consensus framework requiring agreement across Fisher's exact, t-test, and Wilcoxon rank-sum tests (each Benjamini–Hochberg corrected), we identified three high-confidence AT/RT-specific fitness genes: **SMARCD1, ZMYM3, and NABP2**.

2. **Single-nucleus RNA-seq characterization** — We then analyzed snRNA-seq data from seven primary AT/RT patient samples (Paassen et al., 2025; GEO: GSE283842) to characterize ZMYM3 expression across the heterogeneous tumor microenvironment, including the three AT/RT epigenetic subgroups (TYR, SHH, MYC).

Our findings reveal a disconnect between functional dependency and transcript-level expression, reframing ZMYM3 as a **constitutively expressed gene with context-specific functional essentiality** rather than a transcriptionally selective target.

The full project write-up is available in [`docs/Li_Stauber_Final_Project.pdf`](docs/Li_Stauber_Final_Project.pdf).

---

## Repository Structure

```
zmym3-atrt-project/
├── README.md                                   <- This file
├── requirements.txt                            <- Python dependencies
├── .gitignore                                  <- Files excluded from version control
│
├── notebooks/                                  <- Jupyter notebooks (run in order)
│   ├── depmap_analysis/
│   │   ├── 01_depmap_data_loading.ipynb            <- DepMap data loading and merging
│   │   ├── 02_context_specific_gene_identification.ipynb  <- Pan-indication consensus analysis
│   │   └── 03_atrt_zmym3_deep_dive.ipynb           <- AT/RT-focused ZMYM3 characterization
│   └── snRNA-seq/
│       ├── 01_QC.ipynb                             <- snRNA-seq quality control & filtering
│       ├── 02_Normalization_HVG.ipynb              <- Normalization & highly variable gene selection
│       ├── 03_PCA_Harmony_UMAP.ipynb               <- Dimensionality reduction & batch correction
│       ├── 04_Clustering_Annotation.ipynb          <- Leiden clustering & cell-type annotation
│       └── 05_ZMYM3_Expression.ipynb               <- ZMYM3 expression analysis (main result)
│
├── figures/                                    <- Figures extracted from notebooks
│   ├── depmap_analysis/                            <- DepMap consensus, dependency, and co-dependency figures (Figs. 1–3, S1–S2)
│   └── snRNA-seq/
│       ├── 01_QC/                                  <- QC metrics, filtering plots
│       ├── 02_Normalization_HVG/                   <- HVG selection plots
│       ├── 03_PCA_Harmony_UMAP/                    <- PCA elbow, pre/post-Harmony UMAPs
│       ├── 04_Clustering_Annotation/               <- Cluster UMAPs, marker gene plots
│       └── 05_ZMYM3_Expression/                    <- Main paper figures (Figs. 4–6)
│
├── data/                                       <- Data files (not tracked in git; see below)
│   └── README.md                               <- Instructions for downloading raw data
│
└── docs/                                       <- Project write-up and supporting documents
    └── Li_Stauber_Final_Project.pdf
```

---

## Analysis Pipeline

Each analysis stage is a self-contained sequence of notebooks that should be run **in order**, since each notebook writes intermediate output read by the next.

### DepMap analysis (`notebooks/depmap_analysis/`)

| # | Notebook | Inputs | Outputs |
|---|----------|--------|---------|
| 01 | `01_depmap_data_loading.ipynb` | `CRISPRGeneEffect.csv`, `Model.csv` | `gene_effect_annotated.csv`, `01_indication_summary.csv` |
| 02 | `02_context_specific_gene_identification.ipynb` | `gene_effect_annotated.csv` | `all_indication_results.pkl`, `02_consensus_context_specific_genes.csv`, `02_atrt_all_gene_results.csv`, Figs. 1, 2a, S1, FDR specificity |
| 03 | `03_atrt_zmym3_deep_dive.ipynb` | Notebook 2 outputs + `OmicsExpressionTPMLogp1HumanProteinCodingGenes.csv` | `03_ZMYM3_codependencies.csv`, Figs. 2b, 3, S2 |

### snRNA-seq analysis (`notebooks/snRNA-seq/`)

| # | Notebook | Inputs | Outputs |
|---|----------|--------|---------|
| 01 | `01_QC.ipynb` | Raw count matrix from GSE283842 | Filtered AnnData (9,604 nuclei retained) |
| 02 | `02_Normalization_HVG.ipynb` | Filtered AnnData | CP10K-normalized, log1p-transformed AnnData with 2,000 HVGs |
| 03 | `03_PCA_Harmony_UMAP.ipynb` | Normalized AnnData | PCA (30 PCs), Harmony-corrected embedding, UMAP coordinates |
| 04 | `04_Clustering_Annotation.ipynb` | Harmony-corrected AnnData | Leiden clusters (resolution 0.5), cell-type annotations |
| 05 | `05_ZMYM3_Expression.ipynb` | Annotated AnnData | ZMYM3 expression analysis, statistical tests, Figures 4–6 |

---

## Data

A small set of derived analysis tables is included directly in `data/` for convenience:

- `01_indication_summary.csv` — cell line counts per indication (output of Notebook 1)
- `02_consensus_context_specific_genes.csv` — pan-indication consensus gene table (output of Notebook 2)
- `02_atrt_all_gene_results.csv` — full AT/RT per-gene statistics (output of Notebook 2)
- `03_ZMYM3_codependencies.csv` — Pearson correlations of ZMYM3 with all genes (output of Notebook 3)

Large raw source files are **not included** due to size constraints. To reproduce the analysis end-to-end:

### DepMap data (26Q1 release)
- **Source:** [DepMap Portal](https://depmap.org/portal/data_page/?tab=allData)
- **Files needed:**
  - `CRISPRGeneEffect.csv` (Chronos-corrected gene-effect scores)
  - `Model.csv` (cell line metadata with OncotreeSubtype)
  - `OmicsExpressionTPMLogp1HumanProteinCodingGenes.csv` (CCLE bulk expression)
- Place these in `data/`

### snRNA-seq data (Paassen et al., 2025)
- **Source:** [GEO accession GSE283842](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE283842)
- **Description:** 10x Chromium multiome snRNA-seq from 7 AT/RT patient samples (Maxima cohort)
- Download the processed count matrices and metadata, and place them in `data/snrnaseq/`

See [`data/README.md`](data/README.md) for more detailed instructions.

---

## Setup & Reproduction

### Requirements
- Python ≥ 3.10
- Jupyter Lab or Jupyter Notebook
- See `requirements.txt` for the full dependency list

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/zmym3-atrt-project.git
cd zmym3-atrt-project

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter lab
```

### Key packages
- **scanpy** (≥1.10.1) — single-cell analysis framework
- **harmonypy** — batch correction
- **scrublet** — doublet detection (deposited scores used)
- **scipy / statsmodels** — statistical testing (Wilcoxon, Kruskal-Wallis, Fisher's exact, BH-FDR)
- **matplotlib-venn** — Venn diagrams for the consensus framework
- **adjustText** — label placement for the co-dependency volcano plot
- **pandas / numpy** — data manipulation
- **matplotlib / seaborn** — visualization

---

## Statistical Framework (DepMap analysis)

For each cancer indication, every gene is tested for context-specific essentiality (stronger fitness defect in that indication versus all others) using three complementary statistical tests:

| Test | What it measures | Assumptions | FDR cutoff |
|------|------------------|-------------|------------|
| Fisher's exact | Enrichment of dependent cell lines (score ≤ −0.6) | None (exact) | 0.05 |
| Independent t-test | Difference in mean dependency scores | Approximate normality | 0.05 |
| Wilcoxon rank-sum | Distributional shift in scores | None (non-parametric) | 0.05 |

P-values from each test are independently corrected for multiple testing using Benjamini–Hochberg FDR. The top 10 genes per test passing the FDR threshold are retained, and the **intersection across all applicable tests** defines consensus context-specific fitness genes. Indications with fewer than 10 cell lines use only the Fisher and t-test in the consensus (Wilcoxon is dropped for power reasons).

---

## Key Results

- **DepMap consensus screening** identifies ZMYM3, SMARCD1, and NABP2 as AT/RT-specific fitness genes (Figure 1).
- **ZMYM3 dependency** is most pronounced in AT/RT among 167 cancer indications surveyed (Figure 2A); 56.2% of AT/RT cell lines score as dependent vs. 2.9% background.
- **Co-dependency analysis** links ZMYM3 to multiple SWI/SNF subunits (SMARCD1, SMARCC1, ARID1B), supporting a mechanistic relationship between CoREST-mediated repression and residual SWI/SNF function in *SMARCB1*-deficient cells (Figure 3).
- **snRNA-seq analysis** of 9,604 nuclei across 7 patients shows that ZMYM3 is expressed at uniformly **low levels** across both tumor and non-malignant populations (Figures 4–5).
- **No tumor-specific enrichment** is observed; neurons actually express ZMYM3 at higher levels than tumor cells (mean 0.172 vs. 0.102, ratio 0.59×).
- Modest subgroup-level variation: ATRT-TYR shows slightly higher expression than ATRT-MYC and ATRT-SHH (Figure 6), but absolute expression remains <11% of nuclei across all subgroups.

These findings argue that ZMYM3 represents a **non-oncogene addiction** — its constitutive expression becomes selectively indispensable in the *SMARCB1*-deficient context — rather than a transcriptionally selective tumor target.

---

## References

1. Blanco-Carmona, E., Paassen, I., He, J., et al. *Neuro-Oncology* **27**, 3260–3275 (2025). doi: [10.1093/neuonc/noaf179](https://doi.org/10.1093/neuonc/noaf179)
2. Korsunsky, I., et al. *Nature Methods* **16**, 1289–1296 (2019). doi: [10.1038/s41592-019-0619-0](https://doi.org/10.1038/s41592-019-0619-0)
3. Wolf, F.A., Angerer, P., Theis, F.J. *Genome Biology* **19**, 15 (2018). doi: [10.1186/s13059-017-1382-0](https://doi.org/10.1186/s13059-017-1382-0)
4. Meyers, R.M., et al. *Nature Genetics* **49**, 1779–1784 (2017). doi: [10.1038/ng.3984](https://doi.org/10.1038/ng.3984)
5. Behan, F.M., et al. *Nature* **568**, 511–516 (2019). doi: [10.1038/s41586-019-1103-9](https://doi.org/10.1038/s41586-019-1103-9)
6. DepMap, Broad (2026). DepMap 26Q1 Public. [https://depmap.org/](https://depmap.org/)

A full reference list is available in the project write-up.
