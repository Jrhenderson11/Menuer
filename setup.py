from setuptools import setup, find_packages
from os import path
from io import open

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='menuer',
    version='0.1',
    description='Custom command line menu library', 
    packages=find_packages(),
    install_requires=[]
)
