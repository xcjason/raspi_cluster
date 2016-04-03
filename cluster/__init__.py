import yaml
import os
from socket import gethostname

hostname = gethostname()
host = 'jason' if hostname == 'ubuntu' else 'pi'
host_dir = '/home/{0}/bin/'.format(host)
with open(os.path.join(host_dir, 'cluster_config.yml')) as config_file:
    CONFIG = yaml.load(config_file)
