#!/usr/bin/env python
from distutils.core import setup
setup(name='cbtest',
      version='0.0.10',
      author='Peter Claydon',
      author_email='peter.claydon@continuumbridge.com',
      py_modules=['cbtest'],
      install_requires=[
          'Twisted'==16.4.1
      ]
      entry_points={
          'console_scripts': [
              'cbtest = cbtest:main'
           ]
      },
      )
