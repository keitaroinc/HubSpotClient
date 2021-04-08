#!/usr/bin/env python

"""
Copyright (c) 2016 Keitaro AB

Use of this source code is governed by an MIT license
that can be found in the LICENSE file or at
https://opensource.org/licenses/MIT.
"""

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
        'requests==2.10.0'
    ],
)
