## Creating a Python Package

### Introduction
After writing some useful Python code you may wish to share this code with other members
of the Python community. Or you may wish to package some useful 
functions together for use within another repository or in a Jupyter Notebook. There 
are many reasons why you might wish to create a Python package.  

In this repository I will explore how to create a simple Python package. I will create
a Python package of the Flask application which was defined previously in my 
`docker_flask_app` repository. 
 
### Creating a Python Package
The structure of this repository is a common structure that is employed with creating 
a Python package. This structure involves an app folder containing the main python 
script which in this case is called `app.py`. It is also required that the app folder
contains a `__init__.py` script.

Next, we will add the `setup.py` script which enables the creation of your Python 
package. The `setup.py` script will have the following general format:

```
# import setuptools
from setuptools import find_packages, setup

# identify the third party packages used by your package
with open("requirements.txt") as stream:
    REQUIREMENTS = stream.read().splitlines()

# define the longer description as the readme 
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
    install_requires=REQUIREMENTS,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
```
In the above Python script one can define the name and version of their Python package in addition
to adding their contact details and a short/long description of their package. 
The long description is defined as the README.md associated with the package repository. 
A url to the git repository associated with the Python package can also be supplied. 
The install_requires argument defines any additional Python packages that are required for 
the building of this package. Finally, the minimum required version of Python can also be defined. 

If uploading your package to pip then it is important to include a LICENSE file to define how this 
package should be used.  

### Building and installation of a Python package
Is is recommended that one create a virtual environment for the development of this 
Python package. Do so using your favorite virtual environment tool. 

After the creation and activation of a virtual environment, install wheel using the following command:

`pip install wheel`

Now install your Python package locally using the command:

`pip install .`

Use the `pip freeze` command to confirm that the Python package has been installed. In 
this case the package name will be defined as the name defined in the setup.py script. 

### Use your package locally
In this section we will explore how to use your Python package locally within a 
Jupyter Notebook. In a Jupyter notebook use the following commands to import your Python 
package:
```
# import my flask app and the json library
from app.app import app
import json
```

It is important to note that in this case the app is named differently than the 
installed package name. Also in this case the we are installing the app Flask class 
instance contained in the app.py script within the app folder. Finally, for 
completeness the command listed below demonstrates how to use the imported Flask app. 

```
# POST a request containing a list of numbers to my flask app 
response = app.test_client().post(
        "/my_sum",
        data=json.dumps({"data": ["1", "2", "3"]}),
        content_type="application/json",
        )

# examine the output
response
```

### Making changes to your Python package
It might occur that the package you created needs to be updated on a regular basis.
It can be a pain to constantly upgrade your package manually. In this case it is 
possible to enable the package to update automatically once changes have been made 
to its code base. 

The command 

`pip install -e /path/to/repo` 

overwrites the directory in the site-packages with a symbolic link to the package 
you wish to make changes to. Thus, any changes made to this package will be 
automatically added and identified. The symbolic link looks at the current files 
in the directory, meaning you can switch branches to see changes or try different 
things. This is a much nicer and simpler method than repeatedly reinstalling the package.

### Conclusion
This repository contains all the details required to create, install and use locally 
your very own Python package. 
