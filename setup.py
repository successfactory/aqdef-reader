"Setup script for the qdasreader package"

import setuptools
import qdasreader as app

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name=app.__project__,
    version=app.__version__,
    author=app.__author__,
    author_email=app.__author_email__,
    description=app.__doc__,
    long_description=long_description,
    url=app.__url__,
    classifiers=app.__classifiers__,
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
