# Extras

Additional content for data challenge participants.

## Download

Download the complete notebook archive from Zenodo: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17806271.svg)](https://doi.org/10.5281/zenodo.17806271)

Direct download: [rges-pit/data-challenge-notebooks-v0.1.0.zip](https://zenodo.org/records/17806271/files/rges-pit/data-challenge-notebooks-v0.1.0.zip?download=1)

## Notebooks

- [`Microlensing_Tools.ipynb`](Microlensing_Tools.ipynb) – a tutorial notebook that lists open-source microlensing codes, provides Roman-specific walkthroughs, and explains how to install dependencies. It uses simulated light curves from the 2018 WFIRST Data Challenge to demonstrate basic fitting and analysis steps. The notebook is intended to be embedded on the RGES-PIT website and mirrored on the Nexus.

    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/Extras/Microlensing_Tools.ipynb" target="_blank" rel="noopener"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>

- [`Gould_Loeb_Planetary_Event.ipynb`](Gould_Loeb_Planetary_Event.ipynb) – a binary lens light-curve interpretation notebook based on Chapter 4 of the REU2025 minicourse.

    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/Extras/Gould_Loeb_Planetary_Event.ipynb" target="_blank" rel="noopener"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>

- [`nbi_roman_simulations.ipynb`](nbi_roman_simulations.ipynb) – **Neural Posterior Estimation for Roman Microlensing**. A tutorial on Neural Bayesian Inference (NBI) for rapid parameter estimation of Roman microlensing events using simulation-based inference. This notebook demonstrates how to train amortized neural posterior estimators for fast, scalable Bayesian inference on synthetic PSPL light curves. Topics covered include:
  - Configuring normalizing flows and ResNet-GRU featurizers
  - Training amortized neural posterior estimators
  - Performing rapid inference on new light curves
  - Understanding when to use NPE vs traditional MCMC

    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/Extras/nbi_roman_simulations.ipynb" target="_blank" rel="noopener"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>

---

## Requirements

- [`requirements.txt`](requirements.txt) and [`env.yml`](env.yml) – universal Python requirements for all notebooks.

    ```bash
    # pip
    pip install -r requirements.txt

    # conda
    conda env create -f env.yml
    conda activate rges-pit-dc
    ```

### Additional Requirements for NBI Notebook

For the Neural Bayesian Inference notebook, you'll also need:

```bash
pip install nbi
```