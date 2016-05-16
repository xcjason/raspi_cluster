#!/usr/bin/python
import sys
import subprocess
import multiprocessing
from cluster.utils.machine_info import get_all_machine_addr, get_host_dir


def shut_down(args):
    assert len(args['args']) == 0
    ip = args['ip']
    cmd = "ssh pi@{ip}; sudo shutdown -h now;".format(ip)
    return subprocess.call(cmd, shell=True)


def deploy_proj(args):
    assert len(args['args']) == 1
    ip = args['ip']
    proj_name = args['args'][0]
    cmd = "ssh pi@{ip}; cd /home/pi/git_repo/{proj_name}; git pull; sudo python setup.py install".format(ip, proj_name)
    return subprocess.call(cmd, shell=True)


def make_dir(args):
    import pdb; pdb.set_trace()
    host_dir = get_host_dir()
    assert len(args['args']) == 1
    ip = args['ip']
    folder_name = args['args'][0]
    cmd = "ssh pi@{ip}; cd {host_dir}; mkdir {folder_name}".format(ip, host_dir, folder_name)
    return subprocess.call(cmd, shell=True)


def main():
    cmd = sys.argv[1]
    func = globals().get(cmd)
    if func is None:
        raise RuntimeError("Cannot find method {0}".format(cmd))
    all_machine_ips = get_all_machine_addr()
    count = len(all_machine_ips)
    proc_pool = multiprocessing.Pool(processes=count)
    args = [{'ip': ip_addr, 'args': sys.argv[2:]} for ip_addr in all_machine_ips]
    import pdb; pdb.set_trace()
    proc_pool.map(func, args)
    proc_pool.close()


if __name__ == '__main__':
    main()
