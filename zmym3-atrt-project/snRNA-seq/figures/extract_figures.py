"""
extract_figures.py
==================
Utility script that extracts embedded image outputs (PNG, JPEG, SVG) from
Jupyter notebooks into the corresponding subfolders under `figures/`.

Usage
-----
    python extract_figures.py

Mapping convention
------------------
Each notebook in `notebooks/` is mapped to a subfolder in `figures/` whose
name is the notebook's basename without extension. For example:
    notebooks/01_QC.ipynb        -> figures/01_QC/
    notebooks/05_ZMYM3_Expression.ipynb -> figures/05_ZMYM3_Expression/

Figures are saved as `<notebook_name>_cell<NN>_out<MM>.<ext>`.

Requirements
------------
Standard library only (json, base64, os, pathlib).
"""

from __future__ import annotations

import base64
import json
from pathlib import Path

# --- configuration ----------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent
NOTEBOOK_DIR = REPO_ROOT / "notebooks"
FIGURE_DIR = REPO_ROOT / "figures"

# Map notebook stem -> subfolder under figures/. If a notebook isn't listed,
# a folder matching its stem will be created automatically.
EXPLICIT_MAP: dict[str, str] = {
    "01_QC": "01_QC",
    "02_Normalization_HVG_ipynb": "02_Normalization_HVG",  # handles odd filename
    "02_Normalization_HVG": "02_Normalization_HVG",
    "03_PCA_Harmony_UMAP": "03_PCA_Harmony_UMAP",
    "04_Clustering_Annotation": "04_Clustering_Annotation",
    "05_ZMYM3_Expression": "05_ZMYM3_Expression",
}

MIME_TO_EXT = {
    "image/png": "png",
    "image/jpeg": "jpg",
    "image/jpg": "jpg",
    "image/gif": "gif",
    "image/svg+xml": "svg",
}

# --- core logic -------------------------------------------------------------


def extract_from_notebook(nb_path: Path, out_dir: Path) -> int:
    """Extract image outputs from a single notebook. Returns count saved."""
    out_dir.mkdir(parents=True, exist_ok=True)
    saved = 0

    with nb_path.open("r", encoding="utf-8") as f:
        nb = json.load(f)

    stem = nb_path.stem
    for cell_idx, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        for out_idx, output in enumerate(cell.get("outputs", [])):
            data = output.get("data", {})
            for mime, ext in MIME_TO_EXT.items():
                if mime not in data:
                    continue

                fname = f"{stem}_cell{cell_idx:02d}_out{out_idx:02d}.{ext}"
                fpath = out_dir / fname

                payload = data[mime]
                if mime == "image/svg+xml":
                    # SVG is stored as a list of strings (or a single string)
                    text = "".join(payload) if isinstance(payload, list) else payload
                    fpath.write_text(text, encoding="utf-8")
                else:
                    # PNG/JPEG are base64-encoded
                    img_bytes = base64.b64decode(payload)
                    fpath.write_bytes(img_bytes)

                saved += 1
                print(f"  -> saved {fpath.relative_to(REPO_ROOT)}")
                break  # one image per output cell

    return saved


def main() -> None:
    if not NOTEBOOK_DIR.is_dir():
        raise SystemExit(f"Could not find {NOTEBOOK_DIR}")

    notebooks = sorted(NOTEBOOK_DIR.glob("*.ipynb"))
    if not notebooks:
        print(f"No notebooks found in {NOTEBOOK_DIR}. "
              "Add your .ipynb files there and re-run.")
        return

    total = 0
    for nb in notebooks:
        subfolder_name = EXPLICIT_MAP.get(nb.stem, nb.stem)
        out_dir = FIGURE_DIR / subfolder_name
        print(f"\n[{nb.name}] -> figures/{subfolder_name}/")
        n = extract_from_notebook(nb, out_dir)
        print(f"  ({n} image{'s' if n != 1 else ''} saved)")
        total += n

    print(f"\nDone. {total} image{'s' if total != 1 else ''} extracted across "
          f"{len(notebooks)} notebook{'s' if len(notebooks) != 1 else ''}.")


if __name__ == "__main__":
    main()
