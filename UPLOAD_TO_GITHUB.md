# How to Upload This Project to GitHub

This guide walks you through getting the repository onto GitHub as a **private** repo that you can share with your professor. There are two ways to do it — pick whichever you prefer.

---

## Before you start: 3 things to do locally

1. **Unzip the project folder I prepared.** You should see this structure:
   ```
   zmym3-atrt-project/
   ├── README.md
   ├── requirements.txt
   ├── .gitignore
   ├── extract_figures.py
   ├── notebooks/
   ├── figures/
   ├── data/
   └── docs/
   ```

2. **Add your files:**
   - Drop your 5 `.ipynb` notebooks into `notebooks/`. Rename `02_Normalization_HVG_ipynb.ipynb` → `02_Normalization_HVG.ipynb` (cleans up the typo).
   - Drop the project PDF (`Li_Stauber_20_440ProjectFinal__1_.pdf`) into `docs/` and rename it to `Li_Stauber_Final_Project.pdf`.

3. **(Optional) Extract figures from notebooks.** Open a terminal, `cd` into the project folder, and run:
   ```bash
   python extract_figures.py
   ```
   This pulls every embedded image output from your notebooks into the matching `figures/<notebook_name>/` subfolder. Standard library only — no installs needed.

---

## Option A — Use the GitHub web interface (easiest, no terminal)

This is the simplest path if you've never used Git before.

### Step 1 — Create the empty repo on GitHub
1. Go to <https://github.com> and sign in.
2. Click the **+** in the top-right → **New repository**.
3. Settings:
   - **Repository name:** `zmym3-atrt-project` (or whatever you'd like)
   - **Description:** (e.g. *"20.440 Final Project — ZMYM3 dependency in AT/RT"*)
   - **Privacy:** ✅ **Private** (this is what your professor asked for)
   - ❌ Do **not** check "Add a README", "Add .gitignore", or "Add a license" — we already have those.
4. Click **Create repository**.

### Step 2 — Upload your files
1. On the new repo page, click **uploading an existing file** (it's a link in the middle of the page).
2. Drag your entire `zmym3-atrt-project` folder contents into the browser window.
   - **Important:** GitHub's web uploader doesn't preserve empty subfolders, but ours all contain README.md placeholders, so you're safe.
   - **File size limit:** 25 MB per file via the web UI; 100 MB hard limit. Notebooks with embedded figures are usually fine, but if anything fails, use Option B.
3. Scroll down, write a commit message like *"Initial commit — final project files"*, and click **Commit changes**.

### Step 3 — Share with your professor
1. On the repo page, click **Settings** → **Collaborators** (left sidebar).
2. Click **Add people** and enter your professor's GitHub username or email.
3. They'll receive an invitation to access the private repo.

✅ Done!

---

## Option B — Use the terminal (recommended if your repo is large or you want practice)

### Step 0 — Install Git if you don't have it
- **Mac:** Open Terminal and run `git --version`. If prompted, install the developer tools.
- **Windows:** Download [Git for Windows](https://git-scm.com/download/win).
- **Linux:** `sudo apt install git` or your distro's equivalent.

### Step 1 — Create the empty repo on GitHub
Same as Option A, Step 1 above. **Do not** add README/.gitignore/license — leave it empty.

### Step 2 — Initialize and push from your terminal

```bash
# Navigate to the project folder
cd path/to/zmym3-atrt-project

# Initialize a git repository
git init

# Stage all files (the .gitignore will exclude the data/ folder contents automatically)
git add .

# Configure your git identity (only needed once per machine)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Make your first commit
git commit -m "Initial commit — final project files"

# Connect to your GitHub repo (copy the URL from the GitHub page; it looks like:
#   https://github.com/yourusername/zmym3-atrt-project.git )
git branch -M main
git remote add origin https://github.com/yourusername/zmym3-atrt-project.git

# Push everything up
git push -u origin main
```

You'll be prompted for your GitHub username and a **personal access token** (not your password). To create a token: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token → check the `repo` scope.

### Step 3 — Share with your professor
Same as Option A, Step 3 above (Settings → Collaborators → Add people).

---

## What if my professor wants me to update something later?

**Web interface:** Open the repo on GitHub, click any file, click the pencil icon to edit, then commit changes.

**Terminal:** From the project folder:
```bash
git add .                            # stage changes
git commit -m "describe what changed" # save them
git push                              # upload
```

---

## Troubleshooting

**"Repository contains files that are too large."**
GitHub's hard limit is 100 MB per file. If your notebooks are larger than that (rare, but possible with many embedded figures), the cleanest fix is to clear notebook outputs before uploading — in JupyterLab: *Kernel → Restart Kernel and Clear All Outputs*. The figures will be preserved separately in the `figures/` folder if you ran `extract_figures.py`.

**"Remote rejected" / "non-fast-forward" error.**
If you initialized your GitHub repo with a README, .gitignore, or license, you'll need to pull first: `git pull origin main --allow-unrelated-histories`, resolve any conflicts, then push.

**Figures didn't extract.**
Make sure your notebooks have been run with outputs saved. The extractor only finds images that are actually embedded in the `.ipynb` JSON.
