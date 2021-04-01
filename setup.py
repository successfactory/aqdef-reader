"Setup script for the aqdefreader package"

import setuptools
import aqdefreader as app

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name=app.__project__,
    version=app.__version__,
    author=app.__author__,
    author_email=app.__author_email__,
    description=app.__doc__,
    long_description=("**aqdef-reader** is a Python module to read AQDEF (Q-DAS or qdas) ASCII files via Python. The package "
                      "comes with data structures to cover the tranfer file format header elements such as parts (Teiletyp) "
                      "and characteristics (Merkmale). As the ASCII files might already come with measured, values, the "
                      "reader function can already read these values (Messwerte) and stores them as part of the "
                      "characteristics described in the transfer file."),
    url=app.__url__,
    classifiers=app.__classifiers__,
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
