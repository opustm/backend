# Opus Team API

![Website Status](https://img.shields.io/website?url=https%3A%2F%2Fapi.opusteam.us)

[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/opusteam/frontend/blob/master/LICENSE)

[![Generic badge](https://img.shields.io/badge/Python-v3.9-blue.svg)](https://shields.io/)

## About

This is the Opus REST API which serves the Opus Frontend. It currently contains documentation and endpoints for users, teams, requests, events, announcements, JWT, Django Admin.

Available at [https://opusteam.us](https://opusteam.us).


## Dependencies
* Python v3.9
* Pipenv 2020.11.5
* PostgreSQL 13.2
* All Python Modules under `./Pipfile.lock`

## Contributing

### Setup

* Install Python
* Install Pipenv `pip install pipenv`
* Install PostgreSQL for your system [here](https://www.postgresql.org/download/)
* Alternatively you can install it on MacOS using Homebrew:

```zsh
brew install psql
```

* On Debian/Ubuntu use `apt-get`

```
sudo apt-get install psql
```
* Using Pipenv install the other dependencies
```zsh

pipenv install
pipenv install --dev

```
* For MacOS users, install `psycopg2-binary`

```
pip install psycopg-2 binary
```
### Installing Additional Packages

* Start the Python virtual environment and use `pipenv` for package installations
```
pipenv shell
pipenv install <package-name>
```


* Clone the repository `git clone git@github.com:Instaline/Instaline-Markdown.git`
* Activate the virtual environment `pipenv shell`
* Install Dependencies `pipenv install`
* Run the CLI `python3 parse.py`


## License

MIT. 