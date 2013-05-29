#!/usr/bin/env python

# Copyright (c) 2013 David Holm <dholmster@gmail.com>
# This file is part of SimpleGUITk - https://github.com/dholm/simpleguitk
# See the file 'COPYING' for copying permission.

import os

try:
    import setuptools
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

from setuptools import setup
from version import __version__


long_description = open(os.path.join(os.path.dirname(__file__),
                                     'README.rst')).read()

setup(name='SimpleGUITk',
      packages=['simpleguitk',
                'simpleplot'],
      install_requires=['Pillow>=2.0.0',
                        'pygame>=1.9.0'],
      version=__version__,
      description='A wrapper for the CodeSkulptor SimpleGUI API using TkInter',
      author='David Holm',
      author_email='dholmster@gmail.com',
      url='http://github.com/dholm/simpleguitk/',
      download_url=('https://github.com/dholm/simpleguitk/archive/v%s.zip' %
                    __version__),
      license='BSD',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: MacOS X',
          'Environment :: Win32 (MS Windows)',
          'Environment :: X11 Applications',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Topic :: Games/Entertainment',
          'Topic :: Multimedia :: Graphics',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: User Interfaces',
          'Topic :: Software Development :: Widget Sets'],
      long_description=long_description)
