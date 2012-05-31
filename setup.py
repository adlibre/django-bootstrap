#!/usr/bin/env python

from setuptools import setup

setup(name='django-bootstrap',
    version='0.0.1',
    long_description=open('README.md').read(),
    url='https://github.com/adlibre/django-bootstrap',
    packages=['bootstrap',],
    install_requires=['django',],
    package_data={ 'bootstrap': ['static/*',] },
)
