Additional content for data challenge participants.

- [`Extras/Microlensing_Tools.ipynb`](Extras/Microlensing_Tools.ipynb) – a tutorial notebook that lists open-source microlensing codes, provides Roman-specific walkthroughs, and explains how to install dependencies. It uses simulated light curves from the 2018 WFIRST Data Challenge to demonstrate basic fitting and analysis steps. The notebook is intended to be embedded on the RGES-PIT website and mirrored on the Nexus.

    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/Extras/Microlensing_Tools.ipynb" target="_blank" rel="noopener"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>

- [`Extras/Gould_Loeb_Planetary_Event.ipynb`](Extras/Gould_Loeb_Planetary_Event.ipynb) – a binary lens light-curve interpretation notebook based on Chapter 4 of the REU2025 minicourse.

    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/Extras/Gould_Loeb_Planetary_Event.ipynb" target="_blank" rel="noopener"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>

- [`requirements.txt`](requirements.txt) and [`env.yml`](env.yml) – universal Python requirements for all notebooks.

    ```bash
    # pip
    pip install -r requirements.txt

    # conda
    conda env create -f env.yml
    conda activate rges-pit-dc
    ```