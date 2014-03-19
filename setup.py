#!/usr/bin/env python

from distutils.core import setup

with open('README.md') as file:
    long_description = file.read()

setup(name='swiftscripts',
      version='0.1',
      description='A collection of small scripts that aid '
      'in the operation of swift clusters',
      author='William Kelly',
      author_email='the.william.kelly@gmail.com',
      long_description=long_description,
      url="http://github.com/ludditry/swiftscripts",
      packages=['swiftscripts.utils'],
      scripts=['bin/swiftscripts-drive-check',
               'bin/swiftscripts-drive-audit'])
