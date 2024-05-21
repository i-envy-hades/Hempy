# Project-2024
## Group project for practical programming by Arthur Yves Noël Benard/ Louma Cerutti/ Sarah El Skakini:

The aim of our project was to create a function package to study chemical molecules.
More specifically, it can be used to identify chemical properties from the CAS number of the molecule, to determine similarities between two molecules using the Jaccard and Tanimoto index, to visualize molecules in 2 and 3 dimensions, and to study in graphs and tables the values collected from a survey on the use of these molecules. 


# Installation 

## Python:
First check that the correct python version is already installed, which must be 3.10. :`python --version`

If not, update it: `python3 -m pip install --upgrade pip`

If python is not installed :

Rendez-vous sur le site officiel de Python à l'adresse (https://www.python.org) .
Allez dans la section "Downloads" et téléchargez l'installateur pour macOS.
Ouvrez le fichier .pkg téléchargé et suivez les instructions à l'écran pour installer Python.

## Librarians using:
Install the following librarians:

"numpy" with the command : :  `pip install numpy`

"rdkit" with the command : :  `pip install rdkit-pypi`

"sklearn.metrics" with the command : : `pip install scikit-learn`

"nglview" with the command : : `pip install nglview`

"pandas" with the command :  `pip install pandas`

"requests" with the command : `pip install requests`

"Beautiful Soup" with the command : `pip install beautifulsoup4`

"IPython" with the command : `pip install ipython`

"matplotlib" with the command : : `pip install matplotlib `

## Our package:

To install and use our package, go to the terminal and use the following commands:
`pip install git+https://github.com/i-envy-hades/Project-2024.git`
## manque commande pour installation exterieure ?? avoir notre URL github 

# References:

Chemdraw and Pubchem (smiles)

# copier-liac

[Copier](https://github.com/copier-org/copier) template for pure Python libraries.

_As simple as possible. No magic._

Adapted from [copier-pylib](https://github.com/astrojuanlu/copier-pylib) and [snekpack](https://github.com/cthoyt/cookiecutter-snekpack).

## Features

- [Hatch] for packaging.
- [pytest] for testing.
- [tox] for automation of test runners and other stuff.
- [Sphinx] for documentation
- [GitHub Actions] for continuous integration

If you want more automated checks, look at https://github.com/schwallergroup/copier-liac.
- [mypy] for type checks.
- [ruff] for style checks and automatic Python code formatting.
- [pre-commit] for optional automation of style checks.

## Usage

Install `copier`:

```
pip install copier
```

Generate a Python package:

```
copier copy gh:schwallergroup/copier-liac-minimal path/to/destination
```

## License

[MIT License](LICENSE)

[copier]: https://github.com/copier-org/copier/
[Hatch]: https://hatch.pypa.io/
[pytest]: https://docs.pytest.org/
[Sphinx]: http://www.sphinx-doc.org/
[tox]: https://tox.readthedocs.io/
