<div align="center">
    <a href="https://github.com/reges-pit">
        <img src="https://github.com/rges-pit/data-challenge-notebooks/blob/main/rges-pit_logo.png?raw=true" alt="logo" width="300"/>
    </a>
</div>

# To Do

## Repository Management
- [x] workflow auto PRs to `rges-pit.github.io`
- [x] workflow restyling and copying scripts to make notebooks sync accross sources
- [ ] make repo constributing guide mimic RRN style guide, so as to minimize nexus post-processing
- [ ] add nexus instruction to contributing guide
- [ ] add automation specific instruction to the contributing guide
- [x] Zenodo link
  - [x] request OAuth Permission
- [x] citations automations
- [x] `CITATIONS.cff`
- [x] make root `README.md` more participant aware
- [x] fix microlens-submit feedstock and move 0.16.4 back to being a conda dependency

## AAS
- [x] Colab links for environment failure backup
- [x] sync AAS Workshop website content with this repo as the canonical source
- [x] detailed sesion READMEs

## Nexus Integration
- [x] create dedicated public GitHub repo for Nexus (export-only)
  - `reges-pit/nexus-notebooks`
- [x] add global `refdata_dependencies.yaml` (match `spacetelescope/roman_notebooks` format)
- [x] decide notebook discovery regexes (paths/substrings STScI wrangler should scan)
  - `notebooks/*.ipynb`
- [-] organize notebooks in directories where each dir has its own `requirements.txt`
- [x] add optional top-level `environment.yml` (mamba spec for non-pip / low-level deps only)
- [-] move any per-notebook helper `.py` into the same notebook directories
   - they are downloaded in cells
- [-] if using shared modules, create a top-level shared dir + symlink into each notebook dir that imports it
- [x] update automation: publish/update the Nexus repo from `RRN/export_submodule/` (no PRs to `roman_notebooks`)
- [x] send STScI the repo URL + chosen regex list + any notes on expected execution order.

## Nexus
- [x] check data import
- [x] check enviroment functions as specified
- [x] supply STScI a yaml for the `rges-pit-dc` kernel (or replace with `environment.yml` + per-dir `requirements.txt`)
- [x] ask STScI about review timelines
- [x] ask STScI about notebook series instead of standalone per folder
- [-] edit the tools notebook to match the Colab/RRN freindly style
- [ ] add Citations sections in all notebooks (is this already done?)
- [x] delete the `roman_notebooks` PR + fork
- [ ] test that the notebooks run using the provided yaml
- [ ] tag long cells to avoid in quick tests

## Microlensing Tools Notebook
- [ ] table formatting
- [ ] add BAGLE
- [ ] nexus data streaming cell
- [ ] `df_bl` creation and processing
- [ ] title formating
- [ ] proof read
- [ ] test run on all sections

## Gould Loeb
- [ ] edit preamble to match Microlensing Tools
- [ ] proof read
- [ ] test run
- [ ] check data import functions
- [ ] Add to nexus export list

## Website
- [ ] remove mention of workshop sign-up
- [ ] update with real data links
- [x] change PR from fork to PR from branch
- [ ] add source-file comments in to website artifacts
- [x] delete website fork (dc-copy)