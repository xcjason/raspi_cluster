import socket
import time
import yaml
import logging
from cluster import CONFIG

def get_all_machine_addr():
    res = []
    def recur_get_machine_addr(config):
        if len(config.values()) == 1 and isinstance(config.values[0], str):
            res.append(config.values()[0])
        else:
            for k, v in config.iteritems():
                recur_get_machine_addr(v)
    recur_get_machine_addr(CONFIG)
    return res

if __name__ == '__main__':
    get_all_machine_addr()