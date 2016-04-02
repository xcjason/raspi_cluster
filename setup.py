#!/usr/bin/python
__author__ = 'jason'

from distutils.core import setup

setup(
    name='cluster_proj',
    version='0.1',
    author='Cong Xu',
    packages=['cluster', 'cluster.utils'],
    data_files=['config.yml'],
)
