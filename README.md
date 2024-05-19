# Project-2024
Group project for practical programming by Arthur Yves Noël Benard/ Louma Cerutti/ Sarah El Skakini:

The aim of our project was to create a function package to study chemical molecules.
More specifically, it can be used to identify chemical properties from the CAS number of the molecule, to determine similarities between two molecules using the Jaccard and Tanimoto index, to visualize molecules in 2 and 3 dimensions, and to study in graphs and tables the values collected from a survey on the use of these molecules. 

- test_visualization to fix and do
- delete every other branches

# Installation 

To install and use our package, go to the terminal and use the following commands:

`pip install hempy`

Avant cela verifier que la bonne version python soit déjà installer, qui doit être de ... :

`python --version`

Faire de même pour les versions de numpy, qui doit être de 1.24....??:

`python -c "import numpy; print(numpy.__version__)"`

Check that the following librarians are also installed:

"rdkit-pypi", "pandas", "matplotlib" par la commande : `pip install [name of librarians]`


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
