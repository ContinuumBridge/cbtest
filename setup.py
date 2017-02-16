#!/usr/bin/env python
from distutils.core import setup
setup(name='cbtest',
      version='0.0.6',
      author='Peter Claydon',
      author_email='peter.claydon@continuumbridge.com',
      py_modules=['cbtest'],
      entry_points={
          'console_scripts': [
              'cbtest = cbtest:main'
           ]
      },
      )
