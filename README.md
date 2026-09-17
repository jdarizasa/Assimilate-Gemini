[![CI](https://github.com/jdarizasa/Assimilate-Gemini/actions/workflows/blank.yml/badge.svg)](https://github.com/jdarizasa/Assimilate-Gemini/actions/workflows/blank.yml)

# Assimilate-Gemini
This is a repo to create a questio-answer model integrating a gemini model

## Step 1: Configure development environment
* Configure Codespaces or equivalent (devcontainer)
* Create scafold for the structure of the project (Makefile, requirements)
* Optional: set virtualenv and install outside ipython

### Tip
To define the virtual environment for every new terminal use:
```
python -m venv ~/.venv
echo "source ~/.venv/bin/activate" >> ~/.bashrc
source ~/.bashrc
```

## Step 2: Build a library and set the CLI
* Configure the functions on the library
* Configure the API key in secrets, named it GEMINI_API_KEY
* Use click to run the functions from the CLI
* Make a test