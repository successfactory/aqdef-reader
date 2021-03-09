# Python Reader for Advanced Quality Data Exchange Format (AQDEF) ASCII Files
[![PyPI Latest Release](https://img.shields.io/pypi/v/pandas.svg)](https://pypi.org/project/aqdef-reader/)
[![Conda Latest Release](https://anaconda.org/conda-forge/pandas/badges/version.svg)](https://anaconda.org/anaconda/aqdef-reader/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**aqdef-reader** is a Python module to read AQDEF ASCII files via Python. The package comes with data structures to cover the tranfer file format header elements such as parts (Teiletyp) and characteristics (Merkmale). As the ASCII files might already come with measured, values, the reader function can already read these values (Messwerte) and stores them as part of the characteristics described in the transfer file.

The package `aqdefreader` is based on the official 
[Q-DAS ASCII transfer format manual](https://www.q-das.com/fileadmin/mediamanager/Datenformat_Dokumente/Q-DAS_ASCII-Transfer-Format_ENG_V12_ec.pdf) tranfer format released by Q-DAS GmbH.

## Installation
The source code is currently hosted on GitHub at:
https://github.com/successfactory/aqdef-reader

Binary installers for the latest released version are available at the [Python
Package Index (PyPI)](https://pypi.org/project/aqdef-reader) and on [Conda](https://docs.conda.io/en/latest/).

```sh
# or PyPI
pip install aqdef-reader
```

```sh
# conda
conda install aqdef-reader
```

## Dependencies
- [pandas - powerful Python data analysis toolkit](https://pandas.pydata.org/)

## License
[Apache License 2.0](LICENSE)