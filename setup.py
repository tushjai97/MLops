from setuptools import find_packages, setup
from typing import List

HYPEN_E = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''This function will return the list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [reqs.replace('\n' , "")for reqs in requirements]
        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)
    return requirements



setup(
    name= "mlporject",
    version='0.0.1',
    author = 'Tushar',
    author_email='tusharjain.260397@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)
