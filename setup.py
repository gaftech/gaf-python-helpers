# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = __import__('gafhelpers').__version__

setup(
    name = "gaf-python-helpers",
    version = version,
    author = 'Gabriel Fournier',
    author_email = 'gabriel@gaftech.fr',
    url = 'http://github.com/gaftech/gaf-python-helpers',
    packages = find_packages(),
)
