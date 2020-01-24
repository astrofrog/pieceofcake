#!/usr/bin/env python

import os
import sys
from distutils.version import LooseVersion

try:
    import setuptools
    assert LooseVersion(setuptools.__version__) >= LooseVersion('30.3')
except (ImportError, AssertionError):
    sys.stderr.write("ERROR: setuptools 30.3 or later is required\n")
    sys.exit(1)

from setuptools import setup

setup(use_scm_version={'write_to': os.path.join('pieceofcake', 'version.py')})
