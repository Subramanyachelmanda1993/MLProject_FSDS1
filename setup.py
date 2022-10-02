from setuptools import setup, find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME = "housing_price_predictor"
VERSION = "0.0.11"
AUTHOR = "Subramanya Chelmanda"
DESCRIPTION = "This is the first Machine Learning"
REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list()->List[str]:
    """
    Decsription: This function is going to return a list of 
    requirements mentioned in the requirements.txt file.

    Return: This function will return a list of libraries 
    from the requirements.txt file.
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove('-e .')

setup(
name = PROJECT_NAME,
version = VERSION,
author = AUTHOR,
description = DESCRIPTION,
packages = find_packages(),
install_requires = get_requirements_list()
)