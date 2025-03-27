# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "manticoresearch"
VERSION = "7.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.14.1",
    "swagger-ui-bundle==0.0.9",
    "aiohttp_jinja2==1.5.0",
]

setup(
    name=NAME,
    version=VERSION,
    description="Manticore Search Client",
    author_email="info@manticoresearch.com",
    url="",
    keywords=["OpenAPI", "Manticore Search Client"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['manticoresearch=manticoresearch.__main__:main']},
    long_description="""\
    Сlient for Manticore Search. 
    """
)

