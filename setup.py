#!/usr/bin/env python
from distutils.core import setup
setup(name='cbtest',
      version='0.0.21',
      author='Peter Claydon',
      author_email='peter.claydon@continuumbridge.com',
      packages=['testdir'],
      install_requires=[
          'Twisted'
      ],
      entry_points={
          'console_scripts': [
              'cbtest = cbtest:main'
           ]
      },
      )
