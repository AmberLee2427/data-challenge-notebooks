<div align="center">
    <a href="https://github.com/reges-pit">
        <img src="https://github.com/rges-pit/data-challenge-notebooks/blob/main/rges-pit_logo.png?raw=true" alt="logo" width="300"/>
    </a>
</div>

# Roman Microlensing Data Challenge 2026 Notebooks
<hr style="border: 1.5pt solid #a859e4; width: 100%; margin-top: -10px;">

[//]: # (This file needs editing to be data-challenge participant facing first and contributer facing second. Also it's wildly out of date.)

[//]: # (We need a getting started section for environment set up outside of the Nexus, etc. )

This repository provides a set of Jupyter notebooks that support the [**Roman Microlensing Data Challenge 2026**](https://rges-pit.org/outreach/), a competition organised by the [Roman Galactic Exoplanet Survey - Project Infrastructure Team (RGES-PIT)](https://rges-pit.org/). The goal of the challenge is to familiarise researchers with the data volume and characteristics expected from the Roman Galactic Bulge Time Domain Survey, advance existing data analysis and computing practices, and encourage new talent to the field of microlensing.

If you are a data challenge participant, your primary resources are contained in the `AAS Workshop/` and `Extras/` directories. You can find `README.md` files in every directory, to give context to the included content.

## Repository Contents

The contents of this repository populate in many sources:

* **The AAS Workshop silibus** - (`AAS Workshop/`) **canonical notebooks** related to the AAS 247 RMDC26 Workshop
* **Extras** - (`Extra/`) **canonical notebooks** and extra resources for data challenge participants
* RGES-PIT-website-hosted learning resources and data challenge information - (`bin/`) pages built from repository contents and inherited by `rges-pit.github.io`
* Roman-Research-Nexus-hosted (AKA Nexus) content - (`RRN/`) derivatives of appropriate notebooks from this repo, built to meet the STScI style and contributing guidlines

> Relevant content is built into the non-canonical directories through use of transformers in the `scripts` directory according to the `notebook_manifest` (canonical sources is listed under "source_path:"), preserving singular sources of "truth" in the canonical directories. Contributions should not be made to the build directories (`RRN/` and `bin/`) as their contents are emphemeral. See `RRN/README.md` and `bin/ERADME.md` for further details.

### Notebook Content

The notebooks (and related environment files) included in this repo are:

-   [`Microlensing_Tools.ipynb`](https://github.com/rges-pit/data-challenge-notebooks/blob/main/Extra/Microlensing_Tools.ipynb) - A tutorial notebook that lists open-source microlensing codes, provides basic, roman-specific tutorial, and explains how to install dependencies. It uses simulated light-curves from the 2018 WFIRST Data Challenge to demonstrate basic fitting and analysis steps, for various well-established packages. This notebook is intended to be included on the RGES-PIT website and Nexus, for access by data challenge participants and those using the Nexus platform for future Roman-related data analysis.
    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/Extras/Microlensing_Tools.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

-   [`Nexus_Workflow.ipynb`](https://github.com/rges-pit/data-challenge-notebooks/blob/main/AAS_Workshop/Session_A:_Nexus/Nexus_Workflow.ipynb) - A data challenge specific notebook surrounding data access, Nexus use, and submission validation with `microlens-submit`.
    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/AAS_Workshop/Session_A:_Nexus/Nexus_Workflow.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

-   [`Single_Lens_Pipeline.ipynb`](https://github.com/rges-pit/data-challenge-notebooks/blob/main/AAS_Workshop/Session_B:_Single_Lens_&_Pipelines/Single_Lens_Pipeline.ipynb) - A bulk single-lens-fitting tutorial, based on the content of the REU2025 Minicourse, Chapter 5.
    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/AAS_Workshop/Session_B:_Single_Lens_&_Pipelines/Single_Lens_Pipeline.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

-   [`Fitting_Binary_Lenses.ipynb`](https://github.com/rges-pit/data-challenge-notebooks/blob/main/AAS_Workshop/Session_C:_Binary_Lens/Fitting_Binary_Lenses.ipynb) - A bulk single-lens-fitting tutorial, based on the content of the REU2025 Minicourse, Chapter 5.
    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/AAS_Workshop/Session_C:_Binary_Lens/Fitting_Binary_Lenses.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

-   [`Gould_Loeb_Planetary_Event.ipynb`](https://github.com/rges-pit/data-challenge-notebooks/blob/main/Extras/Gould_Loeb_Planetary_Event.ipynb) - A binary lens lightcurve interpreting notebook, based on partial content of the REU2025 Minicourse, Chapter 4.
    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/Extras/Gould_Loeb_Planetary_Event.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

-   [`requirements.txt`](requirements.txt) and [`env.yml`](env.yaml) - universal python requirements for all notebook contents.

    ```bash
    # pip
    pip install -f requirements.txt

    # conda
    conda env create -f env.yml
    conda activate rges-pit-dc
    ```
    
-   Additional notebooks or scripts contributed by the community are extremely welcome. Examples might include custom lightcurve fitting routines, demonstrations of particular codes, or notebooks that handle the additional data types (astrometric time series, image cut-outs) anticipated for RMDC26 and in real Roman data.

## Contributing

These notebooks collect instructions, examples and open-source tools for analysing simulated microlensing lightcurves and identifying false positives. Contributions to existing resources, such as the [`Microlensing_Tools.ipynb`](https://github.com/rges-pit/data-challenge-notebooks/blob/main/Microlensing_Tools.ipynb) notebook,  or in the form of additional instructional resources or [comments](https://github.com/rges-pit/data-challenge-notebooks/discussions) where a notebook is not appropriate or is intractable, are encouraged. You can also submit a suggestion on the RGES-PIT website or raise a GitHub Issue on any relevant rges-pit repo.

### Why Constribute?

-   **Comprehensive Tool Listing** - The notebook contains a table of existing open-source microlensing codes (e.g., _MulensModel_, _BAGEL_, _VBMicrolensing_, _pyLIMA_ and others). The RGES-PIT explicitly invites contributors to add their own related packages to build a more comprehensive list; to do so, open a discussion or follow the [contributing guidelines](https://github.com/rges-pit/data-challenge-notebooks/blob/main/CONTRIBUTING.md). By contributing, you ensure your tool is visible to participants on the Roman Research Nexus and to the wider microlensing community.
    
-   **Centralised Platform for Open Resources** - Our aim is to create a single entry point for open-source microlensing applications. The current notebook acts as an [index of available codes](https://github.com/rges-pit/data-challenge-notebooks/blob/main/Microlensing_Analysis_Tools_colab.ipynb#L219-L222), with cross-references to external resources and detailed guidance. The data challenge is intended to act as an entry point to the field, so if you have resources intended for new microlensers, your contributions will make this index more complete. But this notebook is more than a list. It is a centralized source of event fitting examples, ensuring that new students and scientists can find and compare existing methods quickly. It demonstrates Roman-specific examples of open-source tool usage. Including your tools in this notebook positions them as a pillar for all future Roman microlensing analysis.

-   **Expanding the Community** Providing notebooks or scripts that demonstrate the specific challenges of Roman filters and L2 orbit, will help beginner participants build confidence in different modelling approaches, encouraging diversity in workflows and reducing the barrier to entry in the field.

-   **Semi-Realistic Data Challenge, and Explicitly Roman Test Cases** - The data challenge is designed to mirror the _volume_ and _type_ of time-domain data that will be produced by the Roman Galactic Bulge survey. It focuses on microlensing events and known sources of false positives. The simulated data include lightcurves in two filters (`W149` and `Z087`) with known parameters.
    
-   **Future-Proofing Your Tools** - The challenge data will include additional phenomena such as binary sources, parallax, orbital motion and astrometric time series. Contributing now allows you to demonstrate that your software is ready for these complexities and encourages adoption of your tool in a low-stakes environment so that you can receive critical early feedback.

## How to Contribute

Researchers developing or maintaining open-source microlensing software are encouraged to contribute in one of the following ways:

1.  **Add your package to the tool index** - If your code is missing from the table of microlensing packages, please submit a pull request with your update of [`Microlensing_Tools.ipynb`](https://github.com/rges-pit/data-challenge-notebooks/blob/main/Extras/Microlensing_Tools.ipynb), make a submission on the RGES-PIT website, or start a [discussion](https://github.com/rges-pit/data-challenge-notebooks/discussions) on the repository, to request information be added for you.
    
2.  **Provide a usage example** - Create a section demonstrating how to use your package on the provided lightcurves. Highlight any unique capabilities (e.g. handling binary sources, parallax, or astrometric data). Code examples should be reproducible and include installation instructions.
    
3.  **Extend the analysis** - Contribute notebooks that illustrate best practices for fitting microlensing events, assessing model degeneracies, or estimating physical parameters. Where possible, make use of the known parameter values from Data Challenge 1 to validate your method.
    
4.  **Document learning resources** - If you know of tutorials, workshops or glossaries relevant to microlensing, feel free to add them to the learning resources section. The current notebook already links to the RGES-PIT minicourse, Microlensing Source and other references.

Before submitting a pull request, please check whether an existing issue or discussion covers your contribution. Contributions should adhere to standard open-source etiquette: explain the purpose of your changes, cite relevant literature where appropriate, and ensure that your code is licensed permissively. See the [contributing guidelines](https://github.com/rges-pit/data-challenge-notebooks/blob/main/CONTRIBUTING.md) for more details. **All contributions to this repository must be pushed before the end of 2025 to be on the Nexus or in the AAS Workshop content.**

## Syncing Notebooks to Roman Research Nexus

Syncing notebooks from canonical sources in this repo with the STScI repo for `roman_notebooks` hosted on the Nexus is an automated process. This process is handled by GitHub Actions when a Pull Request is merged to this repo.

The workflow will:
- Copy the notebook to the appropriate location in the `roman_notebooks` repository
- Validate that relative paths in the notebook are correct for the RRN structure
- Correct style and contents for a Nexus specific workflow
- Copy any associated `requirements.txt` file if and `env,.yml`

## Notes on Using and Contributing from Colab

-   Notebooks should be saved in a space you control for editing (e.g. your own GitHub repository or cloud storage) if you wish to keep a permanent record of your progress. Colab does not automatically save notebooks.

-   To save a notebook you work on from Colab, directly into a repo, you must first have [forked](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) a copy of [reges-pit/data-challenge-notebooks](https://github.com/rges-pit/data-challenge-notebooks), so that you "own" it, then grant the required permission to Google. Pushing changes to your forked repo is then as simple as pressing `File > Save`. **It will not autosave to a repo**. You should then make a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) on the rges-pit repository, and explain your changes in the dialog box.
    
-   The tutorials should list their dependencies explicitly (`python≥3.11`, `numpy`, `matplotlib`, `pandas`, `scipy`, `jupyter`, `ipython`, `astropy`, `pathos`); please ensure your examples install any additional packages they require.
    
-   Data used for examples should either come from the provided Data Challenge files or be simulated/retrieved by your code. Avoid including large binary files in this repository; instead, provide instructions for users to download data from canonical sources.


## Citation and Acknowledgement

The notebooks in this repository were originally authored by Amber Malpas, Arjun Murlidhar, Katie Vandorou, Katarzyna Kruszyńska, and Ali Crisp, but rely heavily on the resources provided by the package creators. They are provided by the RGES-PIT to encourage community engagement in preparation for the Roman Galactic Bulge Time Domain Survey. If you adapt or build upon these notebooks, please acknowledge the original authors and the RGES-PIT. For researchers using these materials in publications or teaching, a citation to the relevant Roman mission papers and to the tools you use is recommended.
