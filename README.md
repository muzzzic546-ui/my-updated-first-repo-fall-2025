
# My First Repo!

Learning and practicing version control

## Setup

Clone the repo to download it from GitHub. Perhaps onto the Desktop.

Navigate to the repo using the command line.

```sh
cd ~/Desktop/my-updated-first-repo-fall-2025
```

### Virtual Environment
Create a virtual environment:

```sh
conda create -n my-updated-first-env-fall-2025 python=3.13
```

Activate the virtual environment:

```sh
conda activate my-updated-first-env-fall-2025
```

### Packages
Install package dependencies:

```sh
pip install -r requirements.txt
```

### Secret Credentials

For the stocks dashboard, you will need to acquire a "premium" [AlphaVantage](https://www.alphavantage.co/) API key (from the prof) and supply it as an environment variable. Create a local ".env" file and place inside contents like the following:

```sh
# this is the ".env" file...

# replace "demo" with your premium key:
ALPHAVANTAGE_API_KEY="demo"
```

Also, for the stocks tests to work on GitHub Actions, you will need to set a repository secret named `ALPHAVANTAGE_API_KEY` via the repository's settings on GitHub.


## Usage

Example script:

```sh
python app/my_script.py
```

Game of rock, paper, scissors:

```sh
python app/rps.py

# alternative "modular style" command:
python -m app.rps
```

Stocks dashboard: 

```sh
python -m app.stocks
```


## Testing

Run tests:

```sh
pytest
```