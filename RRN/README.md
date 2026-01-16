<div align="center">
    <a href="https://github.com/rges-pit">
        <img src="https://github.com/rges-pit/data-challenge-notebooks/blob/main/rges-pit_logo.png?raw=true" alt="logo" width="300"/>
    </a>
</div>

## Roman Research Nexus Notebook Copies

Notebooks in this directory are managed by GitHub workflow `.github/workflows/publish.yml`. 

See notebooks_manifest for canonical source file: `source_path:`.

### Notebook Outputs

This repo produces two different *derived* notebook builds:

- `RRN/build/`
    - **Purpose:** Nexus-ready artifacts meant to be exported to the dedicated
        `rges-pit/nexus-notebooks` repository.
    - **Behavior:** Keeps Nexus-only cells (e.g. kernel activation helpers) because
        those are part of the Nexus user experience.

- `RRN/ci_build/`
    - **Purpose:** “Portable” artifacts that are runnable in a standard Jupyter
        kernel (GitHub Actions / Colab-style environments).
    - **Behavior:** Removes Nexus-only activation cells (e.g. `%source kernel-activate ...`).

### Manual Notebook CI (Portable Artifacts)

This repository includes a manual (workflow-dispatch) CI job that rebuilds and
executes the portable notebooks under `RRN/ci_build/`.

- Workflow: `.github/workflows/manual-notebook-ci.yml`
- Profiles:
    - **fast**: skips cells tagged `slow` or `ci-skip`
    - **full**: skips only `ci-skip`

Notes:
- The workflow deletes `RRN/ci_build/` before rebuilding to avoid executing stale
    artifacts.
- Cell tags can be edited in the notebook UI (cell metadata tags).

### Manual Nexus Execution Check (Run On Nexus)

CI cannot reliably execute Nexus-only notebooks because the Nexus platform
provides custom magics and a managed kernel environment.

Instead, the `nexus-notebooks` export includes a small runner script that you
can execute directly on the Roman Research Nexus *after cloning*
`rges-pit/nexus-notebooks`.

From a Nexus terminal:

```bash
git clone https://github.com/rges-pit/nexus-notebooks.git
cd nexus-notebooks

# Run all notebooks using the Nexus kernel; skip the activation helper cells.
python scripts/execute_notebooks_ci.py \
    --glob "notebooks/**/*.ipynb" \
    --kernel-name rges-pit-dc \
    --skip-tags nexus-only \
    --timeout 1800
```
