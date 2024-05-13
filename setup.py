from setuptools import setup, find_packages

setup(
    name = "hempy",
    version = "0.0.1",
    description =,
    author = "Louma Cerrutti/ Arthur Benard/ Sarah El Skakini",
    author_email = "louma.cerrutti@epfl.ch/ arthur.benard@epfl.ch/ sarah.elskakini@epfl.ch",
    licence = "MIT",
    packages = find_packages(),
    install_requires = [
        "numpy >= 1.24.6",
        "rdkit-pypi",
        "pandas",
        "matplotlib"
    ],
    long_description = file: README.md
    classifiers = [
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.11",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows"
    ]
)