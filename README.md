<div align="center">
    <a href="https://github.com/reges-pit">
        <img src="https://github.com/rges-pit/data-challenge-notebooks/blob/main/rges-pit_logo.png?raw=true" alt="logo" width="300"/>
    </a>
</div>

# Roman Microlensing Data Challenge 2026 Notebooks

This repository provides a set of Jupyter notebooks that support the [**Roman Microlensing Data Challenge 2026**](https://rges-pit.org/outreach/), a competition organized by the [Roman Galactic Exoplanet Survey – Project Infrastructure Team (RGES-PIT)](https://rges-pit.org/). The goal of the challenge is to familiarize researchers with the data volume and characteristics expected from the Roman Galactic Bulge Time Domain Survey, advance existing data analysis and computing practices, and encourage new talent to the field of microlensing.

If you are a data challenge participant, your primary resources live in the `AAS Workshop/` and `Extras/` directories. Each directory ships with `README.md` context plus Colab buttons where a remote runtime is supported.

## Data Challenge Sign Up

[![qrcode_sign_ip_form.png](qrcode_sign_up_form.png)](https://forms.gle/reQCDN6S27V7QFEx9)

## Repository Contents

The contents of this repository feed multiple destinations:

* **AAS Workshop syllabus** (`AAS Workshop/`) – canonical notebooks and documentation for the AAS 247 RMDC26 workshop sessions (A–D).
* **Extras** (`Extras/`) – additional canonical notebooks and helper material for data-challenge participants.
* **Website-ready pages** (`bin/`) – Markdown fragments that are transformed into `rges-pit.github.io` pages via `scripts/page_transformer.py`.
* **Roman Research Nexus derivatives** (`RRN/`) – Nexus-specific builds of the canonical notebooks that satisfy the STScI contributing guidelines.

> Derived content is generated from the canonical directories via transformers in `scripts/` using the `notebooks_manifest.yml` manifest. Contributions should not be made directly to `RRN/build/` or `bin/` because those directories are regenerated artifacts. See `RRN/README.md` and the documentation within `bin/` for details.

### Notebook Content

The notebooks (and related environment files) included in this repo are:

- [`Extras/Microlensing_Tools.ipynb`](Extras/Microlensing_Tools.ipynb) – a tutorial notebook that lists open-source microlensing codes, provides Roman-specific walkthroughs, and explains how to install dependencies. It uses simulated light curves from the 2018 WFIRST Data Challenge to demonstrate basic fitting and analysis steps. The notebook is intended to be embedded on the RGES-PIT website and mirrored on the Nexus.

    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/Extras/Microlensing_Tools.ipynb" target="_blank" rel="noopener"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

- [`AAS Workshop/Session A: Nexus/Nexus_Workflow.ipynb`](AAS%20Workshop/Session%20A:%20Nexus/Nexus_Workflow.ipynb) – a data-challenge-specific walkthrough covering data access, Nexus tooling, and submission validation with `microlens-submit`. This notebook is designed for the Roman Research Nexus kernel and is not intended to run on Colab.

- [`AAS Workshop/Session B: Single Lens & Pipelines/Single_Lens_Pipeline.ipynb`](AAS%20Workshop/Session%20B:%20Single%20Lens%20%26%20Pipelines/Single_Lens_Pipeline.ipynb) – a bulk single-lens fitting tutorial, refreshed for the AAS workshop.

    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/AAS%20Workshop/Session%20B:%20Single%20Lens%20%26%20Pipelines/Single_Lens_Pipeline.ipynb" target="_blank" rel="noopener"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

- [`AAS Workshop/Session C: Binary Lens/Fitting_Binary_Lenses.ipynb`](AAS%20Workshop/Session%20C:%20Binary%20Lens/Fitting_Binary_Lenses.ipynb) – a binary-lens modeling notebook that demonstrates multiple fitting strategies and exercise blocks.

    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/AAS%20Workshop/Session%20C:%20Binary%20Lens/Fitting_Binary_Lenses.ipynb" target="_blank" rel="noopener"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

- [`Extras/Gould_Loeb_Planetary_Event.ipynb`](Extras/Gould_Loeb_Planetary_Event.ipynb) – a binary lens light-curve interpretation notebook based on Chapter 4 of the REU2025 minicourse.

    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/Extras/Gould_Loeb_Planetary_Event.ipynb" target="_blank" rel="noopener"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

- [`requirements.txt`](requirements.txt) and [`env.yml`](env.yml) – universal Python requirements for all notebooks.

    ```bash
    # pip
    pip install -r requirements.txt

    # conda
    conda env create -f env.yml
    conda activate rges-pit-dc
    ```

- Additional notebooks or scripts contributed by the community are extremely welcome. Examples include custom light-curve fitting routines, demonstrations of particular codes, or workflows that cover additional data types (astrometric time series, image cut-outs, etc.) anticipated for RMDC26 and future Roman data.

## Contributing

These notebooks collect instructions, examples, and open-source tools for analyzing simulated microlensing light curves and identifying false positives. Contributions to existing resources—such as [`Extras/Microlensing_Tools.ipynb`](https://github.com/rges-pit/data-challenge-notebooks/blob/main/Extras/Microlensing_Tools.ipynb)—or in the form of new instructional resources (or [discussions](https://github.com/rges-pit/data-challenge-notebooks/discussions) when a notebook is not appropriate) are encouraged. You can also [submit a suggestion](https://rges-pit.org/submit/) on the RGES-PIT website or raise a GitHub issue on any relevant `rges-pit` repository.

### Why Contribute?

- **Comprehensive Tool Listing** – The notebook contains a table of open-source microlensing codes (e.g., _MulensModel_, _BAGEL_, _VBMicrolensing_, _pyLIMA_). The RGES-PIT explicitly invites contributors to add their own related packages to build a more comprehensive list; to do so, open a discussion or follow the [contributing guidelines](https://github.com/rges-pit/data-challenge-notebooks/blob/main/CONTRIBUTING.md). By contributing, you ensure your tool is visible to participants on the Roman Research Nexus and to the wider microlensing community.

 - **Centralized Platform for Open Resources** – Our aim is to create a single entry point for open-source microlensing applications. The tools notebook acts as an index of available codes, with cross-references to external resources and detailed guidance. The data challenge is intended to act as an entry point to the field; adding your resources helps new microlensing researchers compare existing methods quickly. Including your tools positions them as a pillar for future Roman microlensing analysis.

- **Expanding the Community** – Providing notebooks or scripts that demonstrate the specific challenges of Roman filters and the L2 orbit will help beginner participants build confidence in different modelling approaches, encouraging diversity in workflows and reducing the barrier to entry.

- **Semi-Realistic Data Challenge and Roman Test Cases** – The challenge mirrors the _volume_ and _type_ of time-domain data that will be produced by the Roman Galactic Bulge survey. It focuses on microlensing events and known sources of false positives. The simulated data include light curves in two filters (`W149` and `Z087`) with known parameters.

- **Future-Proofing Your Tools** – The challenge data include additional phenomena such as binary sources, parallax, orbital motion, and astrometric time series. Contributing now allows you to demonstrate that your software is ready for these complexities and encourages adoption of your tool in a low-stakes environment so that you can receive early feedback.

## How to Contribute

Researchers developing or maintaining open-source microlensing software are encouraged to contribute in one of the following ways:

1. **Add your package to the tool index** – If your code is missing from the table of microlensing packages, please submit a pull request that updates [`Extras/Microlensing_Tools.ipynb`](https://github.com/rges-pit/data-challenge-notebooks/blob/main/Extras/Microlensing_Tools.ipynb), make a [submission](https://rges-pit.org/submit/) on the RGES-PIT website, or start a [discussion](https://github.com/rges-pit/data-challenge-notebooks/discussions) asking us to add it for you.

2. **Provide a usage example** – Create a section demonstrating how to use your package on the provided light curves. Highlight unique capabilities (e.g., handling binary sources, parallax, or astrometric data). Code examples should be reproducible and include installation instructions.

3. **Extend the analysis** – Contribute notebooks that illustrate best practices for fitting microlensing events, assessing model degeneracies, or estimating physical parameters. Where possible, use the known parameter values from Data Challenge 1 to validate your method.

4. **Document learning resources** – If you know of tutorials, workshops, or glossaries relevant to microlensing, add them to the learning resources section. The tools notebook already links to the RGES-PIT minicourse, Microlensing Source, and other references.

Before submitting a pull request, please check whether an existing issue or discussion covers your contribution. Contributions should follow standard open-source etiquette: explain the purpose of your changes, cite relevant literature where appropriate, and ensure that your code is permissively licensed. See the [contributing guidelines](https://github.com/rges-pit/data-challenge-notebooks/blob/main/CONTRIBUTING.md) for more details. **All contributions to this repository must be pushed before the end of 2025 to be included on the Nexus or in the AAS Workshop content.**

## Syncing Notebooks to the Roman Research Nexus

Syncing notebooks from canonical sources in this repo with the STScI `roman_notebooks` repository is an automated process handled by GitHub Actions when a pull request is merged.

The workflow will:
- Copy the notebook to the appropriate location in the `roman_notebooks` repository.
- Validate that relative paths in the notebook are correct for the RRN structure.
- Correct style and contents to satisfy Nexus-specific requirements.
- Copy any associated `requirements.txt` or `env.yml` files.

## Notes on Using and Contributing from Colab

- Notebooks should be saved in a space you control (e.g., your own GitHub repository or cloud storage) if you wish to keep a permanent record of your progress. Colab does not automatically save notebooks.

- To save a notebook you edited in Colab directly into a repo, you must first [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) a copy of [rges-pit/data-challenge-notebooks](https://github.com/rges-pit/data-challenge-notebooks), grant the required permission to Google, and then use `File → Save`. **It will not autosave to a repo.** Afterward, make a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) back to `rges-pit/data-challenge-notebooks` and explain your changes.

- Tutorials should list their dependencies explicitly (`python>=3.11`, `numpy`, `matplotlib`, `pandas`, `scipy`, `jupyter`, `ipython`, `astropy`, `pathos`); please ensure your examples install any additional packages they require.

- Data used for examples should either come from the provided Data Challenge files or be simulated/retrieved by your code. Avoid including large binary files in this repository; instead, provide instructions for users to download data from canonical sources.

## Citation and Acknowledgement

The notebooks in this repository were originally authored by Amber Malpas, Arjun Murlidhar, Katie Vandorou, Katarzyna Kruszyńska, and Ali Crisp, and rely heavily on the work of the package creators. They are provided by the RGES-PIT to encourage community engagement in preparation for the Roman Galactic Bulge Time Domain Survey. If you adapt or build upon these notebooks, please acknowledge the original authors and the RGES-PIT. For researchers using these materials in publications or teaching, a citation to the relevant Roman mission papers and to the tools you use is recommended.

<!-- APA Citation Start -->>
```apa
Malpas, A., Murlidhar, A., Vandorou, K., Kruszyńska, K., & Crisp, A. (2025). Roman Microlensing Data Challenge 2026 Notebooks (v0.1.0). Zenodo. https://doi.org/10.5281/zenodo.17806271
```
<!-- APA Citation End -->>

<!-- BibTeX Citation Start -->>
```bibtex
@software{malpas_2025_17806271,
  author       = {Malpas, Amber and
                  Murlidhar, Arjun and
                  Vandorou, Katie and
                  Kruszyńska, Katarzyna and
                  Crisp, Ali},
  title        = {Roman Microlensing Data Challenge 2026 Notebooks},
  month        = dec,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {v0.1.0},
  doi          = {10.5281/zenodo.17806271},
  url          = {https://doi.org/10.5281/zenodo.17806271},
  swhid        = {swh:1:dir:944eee044fd33e3f1c375c2287de9f0bd4351bda
                   ;origin=https://doi.org/10.5281/zenodo.17806270;vi
                   sit=swh:1:snp:46d2545c1ca9fb19d83be68a053e33953bf2
                   1e06;anchor=swh:1:rel:fd53e0f8d52ea95bb26e9c133c7b
                   4974eda8a6a9;path=rges-pit-data-challenge-
                   notebooks-9097c1b
                  },
}
```
<!-- BibTeX Citation Start -->>
