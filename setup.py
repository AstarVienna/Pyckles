#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Learn more: https://github.com/kennethreitz/setup.py
"""Pyckles"""


from setuptools import setup, find_packages

with open('README.md') as f:
    __readme__ = f.read()

with open('LICENSE') as f:
    __license__ = f.read()

setup(
    name='pyckles',
    version='0.1',
    description="Simple interface to the Pickles 1998 stellar spectra catalogue",
    long_description=__readme__,
    long_description_content_type='text/markdown',
    author='Kieran Leschinski',
    author_email='kieran.leschinski@univie.ac.at',
    url='https://github.com/astronomyk/Pyckles',
    license="GNU General Public License",
    include_package_data=True,
    packages=find_packages(exclude=('tests', 'data')),
    install_requires=['numpy>=1.16', 'astropy', 'matplotlib', 'synphot']
    )
