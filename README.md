<div align="center">
    <a href="https://github.com/reges-pit">
        <img src="https://github.com/rges-pit/data-challenge-notebooks/blob/main/rges-pit_logo.png?raw=true" alt="logo" width="300"/>
    </a>
</div>

# Roman Microlensing Data Challenge Notebooks

This repository provides a set of Jupyter notebooks that support the [**Roman Microlensing Data Challenge**](https://rges-pit.org/outreach/), a competition organised by the [Roman Galactic Exoplanet Survey - Project Infrastructure Team (RGES-PIT)](https://rges-pit.org/). The goal of the challenge is to familiarise researchers with the data volume and characteristics expected from the Roman Galactic Bulge Time Domain Survey and encourage new talent to the field of microlensing. The notebooks collect instructions, examples and open-source tools for analysing simulated microlensing lightcurves and identifying false positives. [Contributions](https://github.com/rges-pit/data-challenge-notebooks/blob/main/CONTRIBUTING.md) to the [`Microlensing_Analysis_Tools_colab.ipynb`](https://github.com/rges-pit/data-challenge-notebooks/blob/main/Microlensing_Analysis_Tools_colab.ipynb) notebook <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/Microlensing_Analysis_Tools_colab.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> (or in the form of additional instructional resources or [comments](https://github.com/rges-pit/data-challenge-notebooks/discussions), where a notebook is not appropriate or is intractable) are welcome. 

## Motivation

-   **Comprehensive Tool Listing** - The notebook contains a table of existing open-source microlensing codes (e.g., _MulensModel_, _BAGEL_, _VBMicrolensing_, _pyLIMA_ and others). The RGES-PIT explicitly invites contributors to add their own related packages to build a more comprehensive list; to do so, open a discussion or follow the [contributing guidelines](https://github.com/rges-pit/data-challenge-notebooks/blob/main/CONTRIBUTING.md). By contributing, you ensure your tool is visible to participants on the Roman Research Nexus and to the wider microlensing community.
    
-   **Centralised Platform for Open Resources** - Our aim is to create a single entry point for open-source microlensing applications. The current notebook acts as an [index of available codes](https://github.com/rges-pit/data-challenge-notebooks/blob/main/Microlensing_Analysis_Tools_colab.ipynb#L219-L222), with cross-references to external resources and detailed guidance. The data challenge is intended to act as an entry point to the field, so if you have resources intended for new microlensers, your contributions will make this index more complete. But this notebook is more than a list. It is a centralized source of event fitting examples, ensuring that new students and scientists can find and compare existing methods quickly. It demonstrates Roman-specific examples of open-source tool usage. Including your tools in this notebook positions them as a pillar for all future Roman microlensing analysis.

-   **Expanding the Community** Providing notebooks or scripts that demonstrate the specific challenges of Roman filters and L2 orbit, will help beginner participants build confidence in different modelling approaches, encouraging diversity in workflows and reducing the barrier to entry in the field.

-   **Semi-Realistic Data Challenge, and Explicitly Roman Test Cases** - The data challenge is designed to mirror the _volume_ and _type_ of time-domain data that will be produced by the Roman Galactic Bulge survey. It focuses on microlensing events and known sources of false positives. The simulated data include lightcurves in two filters (`W149` and `Z087`) with known parameters.
    
-   **Future-Proofing Your Tools** - The challenge data will include additional phenomena such as binary sources, parallax, orbital motion and astrometric time series. Contributing now allows you to demonstrate that your software is ready for these complexities and encourages adoption of your tool in a low-stakes environment so that you can receive critical early feedback.

## Repository Contents

-   [`Microlensing_Analysis_Tools_colab.ipynb`](https://github.com/rges-pit/data-challenge-notebooks/blob/main/Microlensing_Analysis_Tools_colab.ipynb) - A tutorial notebook that introduces the microlensing data challenge, lists open-source microlensing codes and explains how to install dependencies. It uses simulated light-curves from Data Challenge 1 to [demonstrate basic fitting and analysis steps](https://github.com/rges-pit/data-challenge-notebooks/blob/main/Microlensing_Analysis_Tools_colab.ipynb#L225-L228), for various well-established packages. This notebook is intended to be included on the Roman Research Nexus (RRN) for access by data challenge participants and those using the platform for future Roman-related data analysis.

-   [`requirements.txt`](https://github.com/rges-pit/data-challenge-notebooks/blob/main/requirements.txt) - python requirements for notebook contents.

-   [`Microlensing_Data_Challenge_Workflow.ipynb`](https://github.com/rges-pit/data-challenge-notebooks/blob/main/Microlensing_Data_Challenge_Workflow.ipynb) - A data challenge specific notebook surrounding data access, RRN access, and submission validation.
    
-   Additional notebooks or scripts contributed by the community are welcome. Examples might include custom lightcurve fitting routines, demonstrations of particular codes, or notebooks that handle the additional data types (astrometric time series, image cut-outs) anticipated for [Data Challenge 2](https://rges-pit.org/outreach/).

## How to Contribute

Researchers developing or maintaining open-source microlensing software are encouraged to contribute in one of the following ways:

1.  **Add your package to the tool index** - If your code is missing from the table of microlensing packages, please submit a pull request with your update of [`Microlensing_Analysis_Tools_colab.ipynb`](https://github.com/rges-pit/data-challenge-notebooks/blob/main/Microlensing_Analysis_Tools_colab.ipynb) or start a [discussion](https://github.com/rges-pit/data-challenge-notebooks/discussions) on the repository to request it be added for you.
    
2.  **Provide a usage example** - Create a section demonstrating how to use your package on the provided lightcurves. Highlight any unique capabilities (e.g. handling binary sources, parallax, or astrometric data). Code examples should be reproducible and include installation instructions.
    
3.  **Extend the analysis** - Contribute notebooks that illustrate best practices for fitting microlensing events, assessing model degeneracies, or estimating physical parameters. Where possible, make use of the known parameter values from Data Challenge 1 to validate your method.
    
4.  **Document learning resources** - If you know of tutorials, workshops or glossaries relevant to microlensing, feel free to add them to the learning resources section. The current notebook already [links to the RGES-PIT minicourse, Microlensing Source and other references](https://github.com/rges-pit/data-challenge-notebooks/blob/main/Microlensing_Analysis_Tools_colab.ipynb#L268-L290).

Before submitting a pull request, please check whether an existing issue or discussion covers your contribution. Contributions should adhere to standard open-source etiquette: explain the purpose of your changes, cite relevant literature where appropriate, and ensure that your code is licensed permissively. See the [contributing guidelines](https://github.com/rges-pit/data-challenge-notebooks/blob/main/CONTRIBUTING.md) for more details. **All contributions to this repository must be pushed before the end of 2025.**

## Syncing Notebooks to Roman Research Nexus

The `nexus_microlensing_data_challenge_workflow.ipynb` notebook is maintained in this repository but also needs to be available in the [Roman Research Nexus (RRN) notebooks repository](https://github.com/spacetelescope/roman_notebooks). To sync the notebook between repositories, use the provided sync script:

```bash
# Dry run to see what would be copied
python sync_to_nexus.py --dry-run

# Actually sync the notebook
python sync_to_nexus.py
```

The script will:
- Copy the notebook to the appropriate location in the `roman_notebooks` repository
- Validate that relative paths in the notebook are correct for the RRN structure
- Copy any associated `requirements.txt` file if present

**Note:** The script assumes `roman_notebooks` is a sibling directory to `data-challenge-notebooks`. After syncing, you'll need to manually commit and push changes in the `roman_notebooks` repository and create a PR.

## Notes on Notebooks and Data

-   You can - the [`Microlensing_Analysis_Tools_colab.ipynb`](https://github.com/rges-pit/data-challenge-notebooks/blob/main/Microlensing_Analysis_Tools_colab.ipynb) notebook just by clicking this button:         <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/Microlensing_Analysis_Tools_colab.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="- In Colab"/></a>

-   Notebooks should be saved in a space you control for editing (e.g. your own GitHub repository or cloud storage) if you wish to keep a permanent record of your progress. Colab does not automatically save notebooks.

-   To save a notebook you work on from Colab, directly into a repo, you must first have [forked](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) a copy of [reges-pit/data-challenge-notebooks](https://github.com/rges-pit/data-challenge-notebooks), so that you "own" it, then grant the required permission to Google. Pushing changes to your forked repo is then as simple as pressing `File > Save`. **It will not autosave to a repo**. You should then make a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) on the rges-pit repository, and explain your changes in the dialog box.
    
-   The tutorials should list their dependencies explicitly (`python≥3.11`, `numpy`, `matplotlib`, `pandas`, `scipy`, `jupyter`, `ipython`, `astropy`, `pathos`); please ensure your examples install any additional packages they require.
    
-   Data used for examples should either come from the provided Data Challenge files or be simulated by your code. Avoid including large binary files in this repository; instead, provide instructions for users to download data from canonical sources.
    

## Citation and Acknowledgement

The notebooks in this repository were originally authored by Amber Malpas, Katarzyna Kruszyńska and Ali Crisp, but rely heavily on the resources provided by the package creators. They are provided by the RGES-PIT to encourage community engagement in preparation for the Roman microlensing survey. If you adapt or build upon these notebooks, please acknowledge the original authors and the RGES-PIT. For researchers using these materials in publications or teaching, a citation to the relevant Roman mission papers and to the tools you use is recommended.
