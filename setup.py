#!/usr/bin/env python

from distutils.core import setup

setup(
	name='pythonwhat',
	version='2.1.1',
	packages=['pythonwhat', 'pythonwhat.test_funcs'],
	requires=["ast", "re", "markdown2"]
)
