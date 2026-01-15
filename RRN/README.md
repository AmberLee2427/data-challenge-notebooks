<div align="center">
    <a href="https://github.com/rges-pit">
        <img src="https://github.com/rges-pit/data-challenge-notebooks/blob/main/rges-pit_logo.png?raw=true" alt="logo" width="300"/>
    </a>
</div>

## Roman Research Nexus Notebook Copies

Notebooks in this directory are managed by GitHub workflow `.github/workflows/publish.yml`. 

See notebooks_manifest for canonical source file: `source_path:`.

### Manual Notebook CI (Build Artifacts)

This repository includes a manual (workflow-dispatch) CI job that rebuilds the
Nexus-ready notebook artifacts in `RRN/build/` and then executes them.

- Workflow: `.github/workflows/manual-notebook-ci.yml`
- Profiles:
    - **fast**: skips cells tagged `slow` or `ci-skip`
    - **full**: skips only `ci-skip`

Notes:
- The workflow deletes `RRN/build/` before rebuilding to avoid executing stale
    notebooks (for example, notebooks marked `nexus_support: false` in the
    manifest).
- Cell tags can be edited in the notebook UI (cell metadata tags).
