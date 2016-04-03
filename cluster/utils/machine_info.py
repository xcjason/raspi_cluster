from cluster import CONFIG
import re
from socket import gethostname

IP_ADDR_PATTERN = "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"


def get_all_machine_addr():
    res = []

    def recur_get_machine_addr(config):
        if isinstance(config, str) and re.match(IP_ADDR_PATTERN, config):
            res.append(config)
        elif isinstance(config, dict):
            for k, v in config.iteritems():
                recur_get_machine_addr(v)
    recur_get_machine_addr(CONFIG)
    return res


def get_host_dir():
    hostname = gethostname()
    host = 'jason' if hostname == 'ubuntu' else 'pi'
    return '/home/{0}/'.format(host)

if __name__ == '__main__':
    print get_all_machine_addr()