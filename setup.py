#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='evernote',
      version='1.20',
      author='Evernote Corporation',
      author_email='en-support@evernote.com',
      url='http://www.evernote.com/about/developer/api/',
      description='Evernote Web Service API SDK',
      packages= find_packages('src'),
      package_dir = {'': 'src'},
      classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
     ],
)
