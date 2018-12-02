#!/usr/bin/python3
from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='MTG Searcher',
    version='0.1.0',
    description='Search MTG Database and get set list.',
    long_description=readme,
    author='Adam Fries',
    author_email='adam.fries92@gmail.com',
    url='https://github.com/adamfries92/',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
