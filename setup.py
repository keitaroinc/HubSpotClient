#!/usr/bin/env python

"""
Copyright (c) 2016 Keitaro AB

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

https://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
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
        'requests==2.20.0'
    ],
)
