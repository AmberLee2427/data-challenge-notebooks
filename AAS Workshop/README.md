<div align="center">
    <a href="https://github.com/rges-pit">
        <img src="https://github.com/rges-pit/data-challenge-notebooks/blob/main/rges-pit_logo.png?raw=true" alt="logo" width="300"/>
    </a>
</div>

# AAS Workshop Content

The Roman Microlensing Data Challenge 2026 (RMDC26) AAS Workshop is a hands-on, full-day session designed to get participants—from newcomers to seasoned microlensing researchers—set up and productive with the Roman Research Nexus and the core open-source tools used in the Roman Microlensing Data Challenge. We’ll walk through Nexus access and environment setup, introduce essential microlensing concepts and modeling workflows, explore single- and binary-lens fitting (including grid searches and practical strategies for degeneracies and higher-order effects), and show how to organize, validate, and package results for submission using microlens-submit.

This page is a persistent resource to assist you with the AAS Workshop content and RMDC26 troubleshooting, outside of the actual workshop context. Our intention is that those who were not able to attend the workshop will be able to refer to this content and receive the same guidance in a different format.


## Contents

* [Session Outlines](#session-outlines) - what is covered in each session of the workshop.
* [Notebooks](#notebooks) - list of learning resource and reference material notebooks created to assist participants with the data challenge.
    - [Running These Notebooks](#running-these-notebooks) - general instructions on the various ways to run the data challenge notebooks.
* [Windows WSL for Problematic Environment Construction](#windows-wsl-for-problematic-environment-construction)
* [Additional Resources](#additional-resources) - local environment troubleshooting resources
* [Quick Reference Commands](#quick-reference-commands)
* [Citation](#citation)
* [Support](#support)


## Session Outlines

### [A. Introduction to the Nexus](https://rges-pit.org/data-challenge/aas-workshop/1-nexus/)

> 9:00 am – 10:30 am

* Nexus account setup, access, and environment activation
* Using Nexus notebooks, teams, and microlensing tools
* Data access, submissions, package installation, VSCode integration
* Support via Slack and channel canvas

### [B. Single Lenses and Pipelines](https://rges-pit.org/data-challenge/aas-workshop/2-single-lenses/)

> 11:00 am – 12:30 pm

* Microlensing basics and terminology with Dr. Scott Gaudi
* Mini modeling challenge - single lens fitting, priors, parallelization, L2 observer, anomaly detection
* Resources and alternative data access

### [C. Binary Lenses](https://rges-pit.org/data-challenge/aas-workshop/3-binary-lenses/)

> 1:30 pm – 3:00 pm

* Binary-lens modeling and fitting strategies
* Methods: uninformed guess, grid search, informed guess
* Parallelization, degeneracies, stochastic likelihood, higher-order effects

### [D. Information Session and Q&A](https://rges-pit.org/data-challenge/aas-workshop/4-info/)

> 3:30 pm – end

* Open Q&A on microlensing and the Data Challenge
* Details on RGES-PIT website, Slack, sign-up, tiers, data, rules, evaluation, publication, dates, and contact info


## Notebooks

- [`AAS Workshop/Session A: Nexus/Nexus_Workflow.ipynb`](AAS%20Workshop/Session%20A:%20Nexus/Nexus_Workflow.ipynb) – a data-challenge-specific walkthrough covering data access, Nexus tooling, and submission validation with `microlens-submit`. This notebook is designed for the Roman Research Nexus kernel and is not intended to run on Colab.

- [`AAS Workshop/Session B: Single Lens & Pipelines/Single_Lens_Pipeline.ipynb`](AAS%20Workshop/Session%20B:%20Single%20Lens%20%26%20Pipelines/Single_Lens_Pipeline.ipynb) – a bulk single-lens fitting tutorial, refreshed for the AAS workshop.

    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/AAS%20Workshop/Session%20B:%20Single%20Lens%20%26%20Pipelines/Single_Lens_Pipeline.ipynb" target="_blank" rel="noopener"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

 - [`AAS Workshop/Session C: Binary Lens/Fitting_Binary_Lenses.ipynb`](AAS%20Workshop/Session%20C:%20Binary%20Lens/Fitting_Binary_Lenses.ipynb) – a binary-lens modeling notebook that demonstrates multiple fitting strategies and exercise blocks.

    <a href="https://colab.research.google.com/github/rges-pit/data-challenge-notebooks/blob/main/AAS%20Workshop/Session%20C:%20Binary%20Lens/Fitting_Binary_Lenses.ipynb" target="_blank" rel="noopener"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

- [`requirements.txt`](requirements.txt) and [`env.yml`](env.yml) – universal Python requirements for all notebooks.

    ```bash
    # pip
    pip install -r requirements.txt

    # conda
    conda env create -f env.yml
    conda activate rges-pit-dc
    ```

### Running These Notebooks

The notebooks in this repo can all be run in Colab sessions (except `AAS Workshop/Session A: Nexus/Nexus_Workflow.ipynb`, which is exclusively designed for a Nexus environment). Colab is our recommended fallback option if you encounter environment difficulties **and/or** Nexus account difficulties during the workshop.

If you instead choose to run the notebooks locally, you will need to first set up the environment.

1. **Download an Environment File**

* [`env.yaml`](https://raw.githubusercontent.com/rges-pit/data-challenge-notebooks/refs/heads/main/env.yml) - for Conda install.
* [`requirements.txt`](https://raw.githubusercontent.com/rges-pit/data-challenge-notebooks/refs/heads/main/requirements.txt) - for Pip install.

Included in these environment files are the dependencies for the notebooks and packages we anticipate you may need for the data challenge.

2. **Verify Package Handler Installation**
**Option 1: Install via pip**
```bash
pip --version
```

**Option 2: Install via conda-forge**
```bash
conda --version
```

You should see output like: `conda 24.x.x` or similar.

3. **Configure Conda (Optional, Recommended, and Conda-Only)**
```bash
# Disable auto-activation of base environment
conda config --set auto_activate_base false

# Add conda-forge channel
conda config --add channels conda-forge
conda config --set channel_priority strict
```

4. **Install the Dependencies**
**Option 1: Install via pip**
```bash
# Install the package
pip install -r requirements.txt
```

This will add the dependencies to your base environment.

**Option 2: Install via conda-forge**
```bash
# Create the environment
conda env create -f env.yml
```

Running the above line in a terminal (Anaconda Prompt on Windows) will create a virtual conda environment called `rges-pit-dc`, which has the required packages installed.

5. **Activate your environment (Conda only)**
```bash
# Install from conda-forge
conda activate rges-pit-dc
```

6. **Run locally or Local Runtime**

From here you have two options.

**Option 1: Run locally**
You can open the notebook running
```bash
jupyter notebook
```
from a parent folder to your locally saved version of this notebook and navigating to the notebook in your browser. You may need to select `rges-pit-dc` as your kernel before running the notebook.

**Option 2: Local Runtime**
Alternatively, you can create a local "Runtime" for your Colab notebook by following [these instructions](https://research.google.com/colaboratory/local-runtimes.html).
```bash
jupyter notebook --NotebookApp.allow_origin='https://colab.research.google.com' --port=8888 --no-browser
```

> ⚠️ We don't generally recommend that you do this with notebooks that you didn't write as it gives them access to your local machine.


## Windows WSL for Problematic Environment Construction

If you are running a Windows machine, you may find that you are having issues running some of the packages in these notebooks. These are common, usually known, issues. You can create a more stable environment by using WSL (Windows Subsystem for Linux). 

### Prerequisites
- Windows 10 version 2004 or higher (Build 19041 or higher), or Windows 11
- Administrator privileges

### Installation Steps

#### 1. Enable WSL
Open PowerShell as Administrator and run:
```powershell
wsl --install
```

This command will:
- Enable the required optional components
- Download the latest Linux kernel
- Set WSL 2 as the default
- Install Ubuntu (default distribution)

#### 2. Restart Your Computer
After installation completes, restart your computer.

#### 3. Install a Linux Distribution
After restart, you'll need to install a Linux distribution:

**Option A: Install via Microsoft Store**
1. Open Microsoft Store
2. Search for "Ubuntu"
3. Install "Ubuntu 22.04 LTS" or "Ubuntu" (latest version)
4. Click "Open" or launch Ubuntu from the Start menu

**Option B: Install via Command Line**
```powershell
wsl --install -d Ubuntu
```

#### 4. Set Up Your Linux User
When Ubuntu launches for the first time, it will complete the installation (this may take a few minutes). Then you'll be prompted to create your UNIX username and password.

#### 5. Verify WSL 2 Installation
```powershell
wsl --list --verbose
```

You should see your Ubuntu installation with VERSION 2.

#### 6. Update WSL (Optional but Recommended)
```powershell
wsl --update
```

### Alternative: Manual Installation

If the `wsl --install` command doesn't work, follow these manual steps:

1. **Enable WSL Feature**
```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

2. **Enable Virtual Machine Platform**
```powershell
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

3. **Restart your computer**

4. **Download and Install WSL2 Linux Kernel Update**
   - Download from: https://aka.ms/wsl2kernel
   - Run the installer

5. **Set WSL 2 as Default**
```powershell
wsl --set-default-version 2
```

6. **Install Ubuntu from Microsoft Store**
   - Open Microsoft Store
   - Search for "Ubuntu"
   - Install Ubuntu 22.04 LTS (recommended)

### Basic WSL Commands

```powershell
# List installed distributions
wsl --list --verbose

# Set default distribution
wsl --set-default Ubuntu

# Shutdown WSL
wsl --shutdown

# Access WSL from Windows
wsl

# Access Windows files from WSL
cd /mnt/c/Users/YourUsername
```

### Install Miniconda in WSL

1. **Open WSL Terminal**
```powershell
wsl
```

2. **Update System Packages**
```bash
sudo apt update && sudo apt upgrade -y
```

3. **Download Miniconda**
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

4. **Install Miniconda**
```bash
bash Miniconda3-latest-Linux-x86_64.sh
```

Follow the prompts:
- Press Enter to review the license
- Type `yes` to accept the license
- Press Enter to confirm installation location (default: `~/miniconda3`)
- **Type `yes` to initialize Miniconda** (This is crucial!)

5. **Restart Your Shell**

After installation, you need to restart your shell or close and reopen the WSL terminal:

```bash
# Option 1: Close and reopen WSL terminal, then verify
conda --version

# Option 2: If you don't want to close the terminal, manually source bashrc
source ~/.bashrc

# If conda is still not found, manually add to PATH
export PATH="$HOME/miniconda3/bin:$PATH"

# Then verify
conda --version
```

**If `conda: command not found` persists:**

Check if Miniconda was installed correctly:
```bash
# Check if miniconda3 directory exists
ls -la ~/miniconda3

# If it exists, manually initialize conda
~/miniconda3/bin/conda init bash

# Then restart your shell or run
source ~/.bashrc

# If it wasn't installed correctly, repeat the installation steps with the -u option.
Miniconda3-latest-Linux-x86_64.sh -u
```

### VS Code Remote WSL Setup

#### Install VS Code on Windows

1. Download VS Code from https://code.visualstudio.com/
2. Run the installer
3. **Important:** During installation, check "Add to PATH"

#### Install Remote - WSL Extension

1. Open VS Code on Windows
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "Remote - WSL"
4. Install the extension by Microsoft

#### Connect to WSL

**Method 1: From VS Code**
1. Open VS Code
2. Press `Ctrl+Shift+P` to open Command Palette
3. Type "WSL: Connect to WSL"
4. Select your WSL distribution

**Method 2: From WSL Terminal**
```bash
# Navigate to your project directory in WSL
cd ~/projects/your-project

# Open VS Code
code .
```

**Method 3: From Windows Terminal**
```powershell
wsl code .
```

#### Recommended VS Code Extensions for WSL

Install these extensions in WSL (they'll prompt you to install in WSL when you connect):

- **Python** - Python language support
- **Pylance** - Python language server
- **Jupyter** - Jupyter notebook support
- **GitLens** - Enhanced Git capabilities
- **Git Graph** - Visualize Git history
- **Remote - WSL** - Already installed

To install extensions in WSL:
1. Connect to WSL in VS Code
2. Go to Extensions
3. Look for extensions with "Install in WSL: Ubuntu" button
4. Click to install

### Tips for Working with WSL in VS Code

- **Terminal:** VS Code will automatically use your WSL bash terminal
- **File Access:** Access Windows files at `/mnt/c/`, `/mnt/d/`, etc.
- **Performance:** Keep project files in WSL filesystem (e.g., `~/projects/`) for better performance
- **Settings Sync:** Your VS Code settings sync between Windows and WSL


## GitHub SSH Configuration

### Generate SSH Key

1. **Open WSL Terminal**
```bash
wsl
```

2. **Generate SSH Key Pair**
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Press Enter to accept the default file location, then enter a passphrase (optional but recommended).

3. **Start SSH Agent**
```bash
eval "$(ssh-agent -s)"
```

4. **Add SSH Key to Agent**
```bash
ssh-add ~/.ssh/id_ed25519
```

### Add SSH Key to GitHub

1. **Copy SSH Public Key**
```bash
cat ~/.ssh/id_ed25519.pub
```

2. **Add to GitHub**
   - Go to https://github.com/settings/keys
   - Click "New SSH key"
   - Paste your public key
   - Give it a descriptive title (e.g., "WSL Ubuntu")
   - Click "Add SSH key"

3. **Test SSH Connection**
```bash
ssh -T git@github.com
```

You should see: "Hi username! You've successfully authenticated..."

### Configure Git

```bash
# Set your identity
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"

# Set default branch name
git config --global init.defaultBranch main

# Set default editor (optional)
git config --global core.editor "nano"

# Enable credential caching
git config --global credential.helper cache
```

### Fork and Clone Repositories

**Fork a Repository:**
1. Navigate to the repository on GitHub
2. Click the "Fork" button in the top right
3. Select your account as the destination

**Clone Your Fork:**
```bash
# Clone using SSH
git clone git@github.com:YOUR_USERNAME/repository-name.git

# Navigate into the repository
cd repository-name

# Add upstream remote (to sync with original repo)
git remote add upstream git@github.com:ORIGINAL_OWNER/repository-name.git

# Verify remotes
git remote -v
```

**Sync Your Fork:**
```bash
# Fetch upstream changes
git fetch upstream

# Merge upstream changes into your main branch
git checkout main
git merge upstream/main

# Push updates to your fork
git push origin main
```


## Troubleshooting

### WSL Issues

**WSL won't start:**
```powershell
wsl --shutdown
wsl
```

**Check WSL version:**
```powershell
wsl --list --verbose
```

**Convert WSL 1 to WSL 2:**
```powershell
wsl --set-version Ubuntu 2
```

### Git/SSH Issues

**Permission denied (publickey):**
- Ensure SSH key is added to ssh-agent: `ssh-add ~/.ssh/id_ed25519`
- Verify key is added to GitHub: Check https://github.com/settings/keys

**Git credential issues:**
```bash
git config --global credential.helper cache
```

### VS Code Issues

**Extensions not working in WSL:**
- Make sure to install extensions specifically in WSL
- Look for "Install in WSL: Ubuntu" button

**Slow performance:**
- Keep project files in WSL filesystem (`~/projects/`)
- Avoid accessing files in `/mnt/c/` when possible

### Conda Issues

**Conda command not found:**
```bash
source ~/.bashrc
# Or
export PATH="$HOME/miniconda3/bin:$PATH"
```

**Environment conflicts:**
```bash
conda clean --all
conda update conda
```


## Additional Resources

- [WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- [Miniconda Documentation](https://docs.conda.io/en/latest/miniconda.html)
- [GitHub SSH Documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [VS Code Remote Development](https://code.visualstudio.com/docs/remote/wsl)
- [Git Documentation](https://git-scm.com/doc)
- [microlens-submit Documentation](https://microlens-submit.readthedocs.io/en/latest/)
- [Submission Manual Format](https://microlens-submit.readthedocs.io/en/latest/submission_manual.html)


## Quick Reference Commands

### WSL
```powershell
wsl                          # Enter WSL
wsl --shutdown              # Shutdown WSL
wsl --list --verbose        # List distributions
```

### Conda
```bash
conda activate microlensing  # Activate environment
conda deactivate            # Deactivate environment
conda env list              # List environments
conda list                  # List installed packages
```

### Git
```bash
git status                  # Check status
git add .                   # Stage all changes
git commit -m "message"     # Commit changes
git push origin branch      # Push to remote
git pull upstream main      # Pull from upstream
```

### VS Code
```bash
code .                      # Open current directory
code filename.py            # Open specific file
```

### microlens-submit CLI
```bash
microlens-submit init --team-name "Team Name" --tier "advanced"
microlens-submit add-solution <event> <model> --param key=value
microlens-submit list-solutions <event>
microlens-submit validate-solution <solution_id>
microlens-submit deactivate <solution_id>
microlens-submit export <output.zip>
```


## Citation

If you use **microlens-submit** in your research, please cite:

```
Malpas, A. (2025). microlens-submit. Zenodo. https://doi.org/10.5281/zenodo.17459752
```

**BibTeX:**
```bibtex
@software{malpas_2025_17468488,
  author       = {Malpas, Amber},
  title        = {microlens-submit},
  month        = oct,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {v0.16.3},
  doi          = {10.5281/zenodo.17468488},
  url          = {https://doi.org/10.5281/zenodo.17468488},
}
```

If you use our notebooks in your project, please cite:

```
Malpas, A. (2025) et al. Roman Microlensing Data Challenge 2026 Notebooks. Zenodo. https://doi.org/10.5281/zenodo.XXXXXXXX
```

**BibTeX:**
```bibtex
@software{malpas_2025_17468488,
  author       = {Malpas, Amber},
  title        = {Roman Microlensing Data Challenge 2026 Notebooks},
  month        = dec,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {v0.16.3},
  doi          = {10.5281/zenodo.17468488},
  url          = {https://doi.org/10.5281/zenodo.XXXXXXXX},
}
```


## Support

If you encounter issues during setup or while working on the challenge, please:
1. Check the troubleshooting section above
2. Review the additional resources
3. Consult the [microlens-submit documentation](https://microlens-submit.readthedocs.io/en/latest/)
4. Open an issue on the relevant challenge repository.
5. Contact the challenge organizers through the challenge Slack workspace.
6. Ask for help anonymously through the [RGES-PIT website](https://rges-pit.org/data-challenge/help/)

Good luck with the Roman Microlensing Data Challenge 2026!