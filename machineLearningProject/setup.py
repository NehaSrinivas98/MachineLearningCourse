# this is the config file that tells python how to use our project
from setuptools import find_packages, setup
def get_requirements(file_path:str)->list[str]:
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if '-e.' in requirements:
            requirements.remove('-e.')

setup(
    name='ml-project',
    version='0.1.0',
    author='Neha',
    author_email='neha@example.com',
    packages=find_packages(),  # It will look for a src file and build it to use it anywhere
    install_requires=get_requirements('requirements.txt'),
)