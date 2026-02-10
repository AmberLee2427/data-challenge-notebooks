# Extras

Additional content for data challenge participants.

## Notebooks

- [`Extras/Microlensing_Tools.ipynb`](Extras/Microlensing_Tools.ipynb) – A tutorial notebook that lists open-source microlensing codes, provides Roman-specific walkthroughs, and explains how to install dependencies. It uses simulated light curves from the 2018 WFIRST Data Challenge to demonstrate basic fitting and analysis steps. The notebook is intended to be embedded on the RGES-PIT website and mirrored on the Nexus.

    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/Extras/Microlensing_Tools.ipynb" target="_blank" rel="noopener"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>

- [`Extras/Gould_Loeb_Planetary_Event.ipynb`](Extras/Gould_Loeb_Planetary_Event.ipynb) – A binarylens lightcurve interpretation notebook based on Chapter 4 of the REU2025 minicourse.

    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/Extras/Gould_Loeb_Planetary_Event.ipynb" target="_blank" rel="noopener"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>

- [`NBI_Roman_Simulations.ipynb`](NBI_Roman_Simulations.ipynb) – **Neural Posterior Estimation for Roman Microlensing**. A tutorial on Neural Bayesian Inference (NBI) for rapid parameter estimation of Roman microlensing events using simulation-based inference. This notebook demonstrates how to train amortized neural posterior estimators for fast, scalable Bayesian inference on synthetic PSPL light curves. Topics covered include:
  - Configuring normalizing flows and ResNet-GRU featurizers
  - Training amortized neural posterior estimators
  - Performing rapid inference on new light curves
  - Understanding when to use NPE vs traditional MCMC

    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/Extras/NBI_Roman_Simulations.ipynb" target="_blank" rel="noopener"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>


## Requirements

- [`requirements.txt`](requirements.txt) and [`env.yml`](env.yml) – universal Python requirements for all notebooks.

    ```bash
    # pip
    pip install -r requirements.txt

    # conda
    conda env create -f env.yml
    conda activate rges-pit-dc
    ```
