#!/usr/bin/env python
from setuptools import setup

setup(
    name='hubspot',
    version='0.1.0',
    description="Simple python wrapper around HubSpot's APIs",
    long_description=open('README.rst').read(),
    author='Petar Efnushev',
    author_email='petar.efnushev@keitaro.info',
    url='https://bitbucket.org/keitaroinc/hubspotapi',
    download_url='',
    license='LICENSE.txt',
    packages=['hubspotapi'],
    install_requires=[
        'requests==2.20.0'
    ],
)
