from gettext import install
from setuptools import setup
from typing import List

#Declaring variables for setup functions
PROJECT_NAME = "housing_price_predictor"
VERSION = "0.0.1"
AUTHOR = "Subramanya Chelmanda"
DESCRIPTION = "This is the first Machine Learning"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list()->List[str]:
    """
    Decsription: This function is going to return a list of requirements 
    mentioned in the requirements.txt file.

    Return: This function will return a list of libraries from the 
    requirements.txt file.
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()



setup(
name = PROJECT_NAME,
version = VERSION,
author = AUTHOR,
description = DESCRIPTION,
packages = PACKAGES,
install_requires = get_requirements_list()

)


# if __name__=="__main__":
#     print(get_requirements_list())