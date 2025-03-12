from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    setup.py file is used to install the required packages for the project.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='ML_Project',
    version='0.0.1',
    description='This is End to End ML project, Generic structure',
    author='kavinesh',
    author_email='kavinesh.work@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)