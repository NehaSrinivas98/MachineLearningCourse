from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->list[str]:
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if '-e.' in requirements:
            requirements.remove('-e.') 

setup(
    name='network_security',
    version='0.1.0',
    packages=find_packages(), #looks for __init__.py and includes those directories as packages
    install_requires=get_requirements('requirements.txt'),
)