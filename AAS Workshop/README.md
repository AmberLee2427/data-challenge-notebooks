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