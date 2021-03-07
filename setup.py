# import setuptools
from setuptools import find_packages, setup

# identify the third party packages used by your package
with open("requirements.txt") as stream:
    REQUIREMENTS = stream.read().splitlines()

# let the readme define the longer description defined below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# define your python package
setup(
    name="my_flask_app",
    version="0.0.1",
    author="David Quinlan",
    author_email="dq@gmail.com",
    description="Flask application which sums a list of numbers contained in the body "
    "of a POST request",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
