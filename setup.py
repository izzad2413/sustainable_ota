from setuptools import find_packages,setup   # These functions are used for packaging and distributing Python projects.
from typing import List   # It's used to specify the type of a variable or function argument,
                          # indicating that we will be working with lists of strings in this script.

HYPEN_E_DOT='-e .'   # define a constant variable
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    from file_path (string data)
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='mlproject', # change your project name
version='0.0.1',
author='Izzad', # author name
author_email='nazmirulizzadnassir@gmail.com', # author email
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)