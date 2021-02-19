"A reader for Q-DAS ASCII files into Python structures"

from .part import QDasPart
from .attribute import QDasAttribute
from .measurement import QDasMeasurement
from .file import QDasFile
from .operations import read_qdas_file, create_attribute_dataframe, create_column_dataframe

__all__ = ["QDasPart", "QDasAttribute", "QDasMeasurement", "QDasFile",
           "read_qdas_file", "create_attribute_dataframe", "create_column_dataframe"]


__project__ = "qdasreader"
__version__ = "develop"
__author__ = "successfactory consulting group"
__author_email__ = "office@successfactory.cc"
__url__ = "https://github.com/successfactory/qdas-reader"

__classifiers__ = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
]
