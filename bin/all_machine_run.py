import sys
import subprocess
from cluster import CONFIG

if __name__ == '__main__':
    cmd = sys.argv[1]
    all_machine_ips = []
    for ip_addr in CONFIG['machine_list']:
        pass
