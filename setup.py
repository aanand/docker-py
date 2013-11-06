#!/usr/bin/env python
import os
from setuptools import setup

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

test_requirements = []
setup(
    name="docker-py",
    version='0.2.0-orchard1',
    description="Python client for Docker.",
    packages=['docker'],
    install_requires=['requests', 'six', 'websocket-client'] + test_requirements,
    zip_safe=False,
    test_suite='tests',
    classifiers=['Development Status :: 3 - Alpha',
                 'Environment :: Other Environment',
                 'Intended Audience :: Developers',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities'],
    )
