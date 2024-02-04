"""Module providing python wrapper to Golden Cheetah data"""
__title__ = 'CheetahPy'
__author__ = 'RyanAugust'
__license__ = 'MIT'
__copyright__ = 'Copyright 2023'

import os
with open(os.path.join('src/cheetahpy', 'VERSION')) as version_file:
    __version__ = version_file.read().strip()

from .cheetahpy import CheetahPy_API
from .local_opendata import opendata_dataset

CheetahPy = CheetahPy_API()

__all__ = [
    'CheetahPy',
    'opendata_dataset'
]
