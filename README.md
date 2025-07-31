## Roman Microlensing Data Challenge Notebooks

This repository provides a set of Jupyter notebooks that support the **Roman Microlensing Data Challenge**, an exercise organised by the Roman Galactic Exoplanet Survey – Project Infrastructure Team (RGES‑PIT). The goal of the challenge is to familiarise researchers with the data volume and characteristics expected from the Roman Galactic Bulge Time Domain Survey. The notebooks collect instructions, examples and open‑source tools for analysing simulated microlensing light‑curves and identifying false positives.

## Motivation

-   **Semi‑realistic data challenge** – The data challenge is designed to mirror the _volume_ and _type_ of time‑domain data that will be produced by the Roman Galactic Bulge survey[GitHub](https://github.com/AmberLee2427/data-challenge-notebooks/blob/main/analysis_tutorial_colab.ipynb#L211-L219). It focuses on microlensing events and known sources of false positives and uses light‑curves from the first microlensing data challenge as test data[GitHub](https://github.com/AmberLee2427/data-challenge-notebooks/blob/main/analysis_tutorial_colab.ipynb#L225-L228). Contributing analysis examples or tools here allows your methods to be tested on realistic scenarios before mission data arrive.
    
-   **Centralised, open resource** – Our aim is to create a single entry point for open‑source microlensing applications. The current notebook acts as an index of available codes, with cross‑references to external resources and detailed guidance[GitHub](https://github.com/AmberLee2427/data-challenge-notebooks/blob/main/analysis_tutorial_colab.ipynb#L219-L222). Additional contributions will make this index more complete and ensure that new students and scientists can find and compare existing methods quickly.
    
-   **Comprehensive tool listing** – The notebook contains a table of existing open‑source microlensing codes (e.g., _MulensModel_, _BAGEL_, _VBMicrolensing_, _pyLIMA_ and others). The authors explicitly invite contributors to add their own packages to build a more comprehensive list; the notebook suggests opening a discussion or following the contributing guidelines[GitHub](https://github.com/AmberLee2427/data-challenge-notebooks/blob/main/analysis_tutorial_colab.ipynb#L260-L266). By contributing, you ensure your tool is visible to participants on the Roman Research Nexus and to the wider microlensing community.
    
-   **Reproducibility, collaboration, and Explicitly Roman Content** – Sharing your code and workflows in an open notebook facilitates reproducibility and peer review. The simulated data include light‑curves in two filters (`W149` and `Z087`) with known parameters[GitHub](https://github.com/AmberLee2427/data-challenge-notebooks/blob/main/analysis_tutorial_colab.ipynb#L225-L228). Providing notebooks or scripts that demonstrate the specific use case that is Roman filter's and L2-orbit, will help others identify edge cases and build confidence in different modelling approaches.
    
-   **Future‑proofing your tools** – The challenge highlights that future data will include additional phenomena such as binary sources, parallax, orbital motion and astrometric time series[GitHub](https://github.com/AmberLee2427/data-challenge-notebooks/blob/main/analysis_tutorial_colab.ipynb#L241-L245). Contributing now allows you to demonstrate that your software is ready for these complexities and to receive feedback from early adopters.
    

## Repository contents

-   `analysis_tutorial_colab.ipynb` – A tutorial notebook (to be renamed) that introduces the microlensing data challenge, lists open‑source microlensing codes and explains how to install dependencies. It uses simulated light‑curves from Data Challenge 1 to demonstrate basic fitting and analysis steps[GitHub](https://github.com/AmberLee2427/data-challenge-notebooks/blob/main/analysis_tutorial_colab.ipynb#L211-L219)[GitHub](https://github.com/AmberLee2427/data-challenge-notebooks/blob/main/analysis_tutorial_colab.ipynb#L225-L228).
    
-   Additional notebooks or scripts contributed by the community are welcome. Examples might include custom light‑curve fitting routines, demonstrations of particular codes, or notebooks that handle the additional data types (astrometric time series, image cut‑outs) anticipated for Data Challenge 2[GitHub](https://github.com/AmberLee2427/data-challenge-notebooks/blob/main/analysis_tutorial_colab.ipynb#L241-L245).
    

## How to contribute

Researchers developing or maintaining open‑source microlensing software are encouraged to contribute in one of the following ways:

1.  **Add your package to the tool index** – If your code is missing from the table of microlensing packages, please submit a pull request updating the relevant notebook or start a discussion on the repository[GitHub](https://github.com/rges-pit/data-challenge-notebooks/blob/main/analysis_tutorial_colab.ipynb#L260-L266). Include a brief description, maintenance status and link to the code.
    
2.  **Provide a usage example** – Create a notebook demonstrating how to use your package on the provided light‑curves. Highlight any unique capabilities (e.g. handling binary sources, parallax, or astrometric data). Code examples should be reproducible and include installation instructions.
    
3.  **Extend the analysis** – Contribute notebooks that illustrate best practices for fitting microlensing events, assessing model degeneracies, or estimating physical parameters. Where possible, make use of the known parameter values from Data Challenge 1 to validate your method[GitHub](https://github.com/rges-pit/data-challenge-notebooks/blob/main/analysis_tutorial_colab.ipynb#L225-L228).
    
4.  **Document learning resources** – If you know of tutorials, workshops or glossaries relevant to microlensing, feel free to add them to the learning resources section. The current notebook already links to the RGES‑PIT minicourse, Microlensing Source and other references[GitHub](https://github.com/rges-pit/data-challenge-notebooks/blob/main/analysis_tutorial_colab.ipynb#L268-L290).
    

Before submitting a pull request, please check whether an existing issue or discussion covers your contribution. Contributions should adhere to standard open‑source etiquette: explain the purpose of your changes, cite relevant literature where appropriate, and ensure that your code is licensed permissively.

## A Note on Notebooks and Data

-   Notebooks should be saved in a space you control (e.g. your own GitHub repository or cloud storage) if you wish to keep a permanent record of your progress. Colab does not automatically save notebooks[GitHub](https://github.com/reges-pit/data-challenge-notebooks/blob/main/analysis_tutorial_colab.ipynb#L25-L32).

-   To save a notebook you work on from colab, directly into a repo, you must first have forked a copy of reges-pit/data-challenge-notebooks, so that you own it, then grant the required permission to google. Pushing changes to your forked repo is then as simple as pressing `File > Save`. **It will not autosave to a repo**. You should then make a [pull request]([https://www.youtube.com/watch?v=nCKdihvneS0](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)) on the rges-pit repository, and explain you changes in the dialoge box.
    
-   The tutorials should list their dependencies explicitly (`python≥3.11`, `numpy`, `matplotlib`, `pandas`, `scipy`, `jupyter`, `ipython`, `astropy`, `pathos`)[GitHub](https://github.com/rges-pit/data-challenge-notebooks/blob/main/analysis_tutorial_colab.ipynb#L25-L44); please ensure your examples install any additional packages they require.
    
-   Data used for examples should either come from the provided Data Challenge files or be simulated by your code. Avoid including large binary files in this repository; instead, provide instructions for users to download data from canonical sources.
    

## Citation and Acknowledgement

The notebooks in this repository were originally authored by Amber Malpas, Katarzyna Kruszyńska and Ali Crisp, but rely heavily on the resources provided by the package creators. They are provided by the RGES‑PIT to encourage community engagement in preparation for the Roman microlensing survey[GitHub](https://github.com/rges-pit/data-challenge-notebooks/blob/main/analysis_tutorial_colab.ipynb#L211-L219). If you adapt or build upon these notebooks, please acknowledge the original authors and the RGES‑PIT. For researchers using these materials in publications or teaching, a citation to the relevant Roman mission papers and to the tools you use is recommended.
