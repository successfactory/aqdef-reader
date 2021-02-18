import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qdasreader",
    version="0.0.1",
    author="successfactory consulting group",
    author_email="office@successfactory.cc",
    description="A reader for Q-DAS ASCII files into Python structures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/successfactory/qdas-reader",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)