<div align="center">
    <a href="https://github.com/reges-pit">
        <img src="https://github.com/rges-pit/data-challenge-notebooks/blob/main/rges-pit_logo.png?raw=true" alt="logo" width="300"/>
    </a>
</div>

# AAS Workshop Content

## Outline

## Notebooks

- [`AAS Workshop/Session A: Nexus/Nexus_Workflow.ipynb`](AAS%20Workshop/Session%20A:%20Nexus/Nexus_Workflow.ipynb) – a data-challenge-specific walkthrough covering data access, Nexus tooling, and submission validation with `microlens-submit`. This notebook is designed for the Roman Research Nexus kernel and is not intended to run on Colab.

- [`AAS Workshop/Session B: Single Lens & Pipelines/Single_Lens_Pipeline.ipynb`](AAS%20Workshop/Session%20B:%20Single%20Lens%20%26%20Pipelines/Single_Lens_Pipeline.ipynb) – a bulk single-lens fitting tutorial, refreshed for the AAS workshop.

    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/AAS%20Workshop/Session%20B:%20Single%20Lens%20%26%20Pipelines/Single_Lens_Pipeline.ipynb" target="_blank" rel="noopener"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

- [`AAS Workshop/Session C: Binary Lens/Fitting_Binary_Lenses.ipynb`](AAS%20Workshop/Session%20C:%20Binary%20Lens/Fitting_Binary_Lenses.ipynb) – a binary-lens modelling notebook that demonstrates multiple fitting strategies and exercise blocks.

    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/AAS%20Workshop/Session%20C:%20Binary%20Lens/Fitting_Binary_Lenses.ipynb" target="_blank" rel="noopener"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

- [`requirements.txt`](requirements.txt) and [`env.yml`](env.yml) – universal Python requirements for all notebooks.

    ```bash
    # pip
    pip install -r requirements.txt

    # conda
    conda env create -f env.yml
    conda activate rges-pit-dc
    ```

## Running These Notebooks

The notebooks in this repo can all be run on Colab sessions (except `/Users/malpas.1/Code/data-challenge-notebooks/AAS Workshop/Session A: Nexus/a_rmdc26_workflow.ipynb`, which is exclusive design for a Nexus environment) and this is a recommended fallback, if you encounter environment difficulties **and** Nexus account difficulties during the workshop. 

```bash
conda env create -f env.yml
```

Running the above line in a terminal (Anaconda Prompt on Windows) will create a virtual conda environment called `rges-pit-dc`, which has the required packages installed.

You can activate the environment with:

```bash
conda activate rges-pit-dc
```

From here you have two options

1. You can open the notebook running
```bash
jupyter notebook
```
from a parent folder to your locally saved version of this notebook and navigating to the notebook in your browser. You may need to select `rges-pit-dc` as your kernel before running the notebook.

2. Alternatly, you can create a local "Runtime" for your Colab notebook by following [these instructions](https://www.google.com/url?q=https%3A%2F%2Fresearch.google.com%2Fcolaboratory%2Flocal-runtimes.html).
```bash
jupyter notebook --NotebookApp.allow_origin='https://colab.research.google.com' --port=8888 --no-browser
```

  ⚠️ We don't generally recommend that you do this with notebooks that you didn't write as it gives them access to your local machine.