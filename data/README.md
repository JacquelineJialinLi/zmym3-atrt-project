# Data Files

This directory holds the raw and processed data used by the analysis
notebooks. None of these files are tracked in version control due to size
constraints. Download the source files from the locations below and place
them here before running the notebooks.

## DepMap analysis

Download from the [DepMap Portal](https://depmap.org/portal/data_page/?tab=allData) (26Q1 release):

- `CRISPRGeneEffect.csv` — Chronos-corrected gene-effect scores (~250 MB)
- `Model.csv` — Cell line metadata with OncotreeSubtype annotations
- `OmicsExpressionTPMLogp1HumanProteinCodingGenes.csv` — CCLE bulk RNA-seq (log2 TPM+1)

Place these directly in the `data/` directory.

The notebooks also write the following derived files here when run. The four marked **[tracked]** are small enough to be checked into the repository, so you can inspect the analysis outputs without re-running the full pipeline.

- `gene_effect_annotated.csv` — gene-effect matrix with merged cancer annotations (Notebook 1)
- `01_indication_summary.csv` — cell line counts per indication (Notebook 1) **[tracked]**
- `all_indication_results.pkl` — pickled per-indication test results (Notebook 2)
- `02_consensus_context_specific_genes.csv` — pan-indication summary table (Notebook 2) **[tracked]**
- `02_atrt_all_gene_results.csv` — full AT/RT per-gene statistics (Notebook 2) **[tracked]**
- `03_ZMYM3_codependencies.csv` — Pearson correlations of ZMYM3 with all genes (Notebook 3) **[tracked]**

## snRNA-seq analysis

Download from [GEO accession GSE283842](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE283842):

- Processed count matrices and cell-level metadata from the seven AT/RT patient samples (Paassen et al., 2025)

Place these in `data/snrnaseq/`.

The notebooks also write derived AnnData files (`.h5ad`) here as the
pipeline progresses through QC → normalization → embedding → clustering.
