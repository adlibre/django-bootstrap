#!/usr/bin/env python

from setuptools import setup

setup(name='django-bootstrap',
    zip_safe = False,
    version='0.0.2',
    long_description=open('README.md').read(),
    url='https://github.com/adlibre/django-bootstrap',
    packages=['bootstrap',],
    install_requires=['django',],
    package_data={ 'bootstrap': ['static/css/*', 'static/js/*', 'static/img/*'] },
)
