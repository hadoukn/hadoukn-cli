# hadoukncli/setup.py
import os
from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

entry_points = """
    [console_scripts]
    hadoukn = hadoukncli:run_command
"""

setup(name='hadoukncli',
      version='0.1',
      description='hadoukncli',
      long_description=README,
      packages=find_packages(),
      test_suite='hadoukncli.tests',
      entry_points=entry_points)
