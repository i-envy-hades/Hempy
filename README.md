# Project-2024
Group project for practical programming/ Arthur Yves Noël Benard/ Louma Cerutti/ Sarah El Skakini

- test_visualization to fix and do
- when functions added and done, create dist file with "python setup.py sdist"
- now delete every other no package's branches  ? 

`code pip install`

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
