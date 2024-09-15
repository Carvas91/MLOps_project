from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) ->List[str]:
    '''
    This function will return the requirements list'''
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='MLOps project',
    version='0.0.1',
    author='Carlos Vasconez',
    author_email='carvas91@hotmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)