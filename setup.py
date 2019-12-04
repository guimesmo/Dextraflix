# -*- coding: utf-8 -*-
"""
setup.py script
"""

import io
from collections import OrderedDict
from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding='utf8') as f:
    README = f.read()

setup(
    name='dextraflix',
    version='1.0.0',
    url='http://github.com/guimesmo/dextraflix',
    project_urls=OrderedDict((
        ('Code', 'https://github.com/guimesmo/dextraflix.git'),
        ('Issue tracker', 'https://github.com/guimesmo/dextraflix/issues'),
    )),
    license='BSD-3-Clause',
    author='Dextra Python Guild',
    maintainer='Dextra Python Guild team',
    description='Video sharing service',
    long_description=README,
    packages=["dextraflix", "dextraflix.controllers", "dextraflix.models", "dextraflix.views"],
    include_package_data=True,
    zip_safe=False,
    platforms=[any],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'Flask==1.1.1',
        'Flask-PyMongo==2.3.0',
        'python-dotenv==0.10.3',
        'marshmallow==3.2.2',
        'Flask-RESTful==0.3.7'
    ],
    extras_require={
        "dev": [
            "pytest==4.0.0",
            "pytest-cov==2.6.0"
        ]
    }
)
