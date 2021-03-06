from setuptools import setup, find_packages
import sys, os
from glob import glob


version = '0.1'

setup(name='irccat.client',
    version=version,
    description="Client module for irccat",
    long_description="""\
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='irc irccat',
    author='Justin Azoff',
    author_email='JAzoff@uamail.albany.edu',
    url='',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    scripts=glob('scripts/*'),
    entry_points = {
        'console_scripts': [
            'irccat-send =    irccat.client:main',
        ]
    },
    )
