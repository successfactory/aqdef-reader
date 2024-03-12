# Python module to read DFQ files in the Q-DAS ASCII transfer format
[![PyPI Latest Release](https://img.shields.io/pypi/v/aqdefreader)](https://pypi.org/project/aqdefreader/)
[![Python Package](https://github.com/successfactory/aqdef-reader/actions/workflows/main.yml/badge.svg)](https://github.com/successfactory/aqdef-reader/actions/workflows/main.yml)
[![CodeQL](https://github.com/successfactory/aqdef-reader/actions/workflows/codeql.yml/badge.svg)](https://github.com/successfactory/aqdef-reader/actions/workflows/codeql.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**aqdef-reader** is a Python module designed for reading DFQ files (Q-DAS ASCII transfer format). This package provides data structures to handle elements of the transfer file format, including parts and characteristics. It is capable of reading measured values contained within the DFQ files, integrating these values into the characteristics detailed in the transfer file.

The package `aqdefreader` is developed in accordance with the official [Q-DAS ASCII transfer format manual](https://training.q-das.de/fileadmin/mediamanager/Datenformat_Dokumente/Q-DAS_ASCII-Transfer-Format_ENG_V12_ec.pdf), ensuring compatibility and reliability in processing and interpreting data formatted according to the standards set by Q-DAS GmbH.

## Installation
The source code is currently hosted on GitHub at:
https://github.com/successfactory/aqdef-reader

Binary installers for the latest released version are available at the [Python
Package Index (PyPI)](https://pypi.org/project/aqdefreader/).

```sh
# PyPI
pip install aqdefreader
```

## Dependencies
- [pandas - powerful Python data analysis toolkit](https://pandas.pydata.org/)

## License
[Apache License 2.0](LICENSE)
