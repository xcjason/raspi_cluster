#!/usr/bin/python
__author__ = 'jason'

from distutils.core import setup
from socket import gethostname

hostname = gethostname()

host = 'jason' if hostname == 'ubuntu' else 'pi'
host_dir = '/home/{0}/bin/'.format(host)

setup(
    name='cluster',
    version='0.1',
    author='Cong Xu',
    packages=('cluster', 'cluster.utils'),
    scripts=('bin/cluster_cli.py', 'bin/cluster', 'bin/consumer_cli.py', 'bin/producer_cli.py'),
    data_files=[(host_dir, ['cluster_config.yml']), ],
)
