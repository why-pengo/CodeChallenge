# Getting started

## Github link

[Github repo](https://github.com/why-pengo/CodeChallenge)

## To run this code

This project uses the [poetry](https://python-poetry.org/docs/) package and virtual environment manager for Python.

To install poetry:

```bash
pip install --user poetry
```

To setup the virtual environment and install dependencies:

```bash
poetry install
```

To run the program:

```bash
poetry run python main.py text/moby-dick.txt
```

Alternative way to run the program is inside the virtual environment:

```bash
poetry shell
python main.py --help
python main.py text/moby-dick.txt
```

To get cli help:

```bash
poetry run python main.py --help
```

## Bugs

Currently, very hacky workaround to some strange text encoding of punctuation.

# Some Packages used and links to the documentation:

* [Click](https://click.palletsprojects.com/en/8.1.x/#) Command Line Interface Creation Kit
* [NLTK](https://www.nltk.org/install.html) Natural Language Processing



