"A reader for Advanced Quality Data Exchange Format ASCII files into Python structures"

from .part import Part
from .characteristic import Characteristic
from .measurement import Measurement
from .file import DfqFile
from .operations import (
    read_dfq_file,
    create_characteristic_dataframe,
    create_column_dataframe,
)

__all__ = [
    "Part",
    "Characteristic",
    "Measurement",
    "DfqFile",
    "read_dfq_file",
    "create_characteristic_dataframe",
    "create_column_dataframe",
]


__project__ = "aqdefreader"
__version__ = "develop"
__author__ = "successfactory consulting group"
__author_email__ = "office@successfactory.cc"
__url__ = "https://github.com/successfactory/aqdef-reader"

__classifiers__ = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
]
