# This file is responsible in creating our ML application as a Package, we can even deploy our package in PyPi, from there anybody can do installation and use it.

from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # inside requirements.txt, the line will be get readed

        # when line will be get readed, it will also add "\n", so to remove that...
        requirements = [req.replace("\n", "") for req in requirements]
        
    return requirements
    
setup(
    name = "ML_Project",
    version = "0.0.1",
    author = "Jaimin Jariwala",
    author_email = "jaiminjariwala5@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)