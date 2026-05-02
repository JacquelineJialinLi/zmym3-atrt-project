# DepMap Analysis Figures

Figures from the CRISPR DepMap dependency screening portion of the project. The DepMap analysis was conducted separately from the snRNA-seq notebooks.

Typical contents:
- **Figure 1** — Venn diagram of consensus dependency analysis for AT/RT (ZMYM3, SMARCD1, NABP2 in triple intersection)
- **Figure 2A** — Box plot of ZMYM3 gene-effect (Chronos) scores across all 167 cancer indications
- **Figure 2B** — Box plot of ZMYM3 expression (CCLE log2[TPM+1]) across indications
- **Figure 3** — Volcano plot of ZMYM3 co-dependencies across DepMap cell lines, highlighting SWI/SNF (SMARCD1, SMARCC1, ARID1B) and CoREST (ZMYM4, HMG20B, KDM1A) members
- **Figure S1** — Pan-cancer validation Venn diagrams (melanoma, GBM IDH-WT, OCSCC, lung adenocarcinoma, colon adenocarcinoma, pancreatic adenocarcinoma)
- **Figure S2** — Density plot of ZMYM3 dependency scores across all cell lines, with AT/RT lines highlighted

**Key findings:**
- 16 rhabdoid cell lines (merged from 3 OncotreeSubtype categories) vs. 1,192 background lines
- Three consensus genes: SMARCD1 (87.5% dependent), ZMYM3 (56.2%), NABP2 (50.0%)
- AT/RT shows the most negative median ZMYM3 dependency score across all 167 indications
- ZMYM3 co-dependency: strongest with SMARCD1 (r = 0.208, p = 9.87 × 10⁻¹²)

If you have the source notebook(s) for the DepMap analysis, place them in `notebooks/` alongside the snRNA-seq pipeline.
