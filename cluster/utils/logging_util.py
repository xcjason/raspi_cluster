import logging
from socket import gethostname

hostname = gethostname()

host = 'jason' if hostname == 'ubuntu' else 'pi'
LOGGING_FILE = '/home/{0}/log/distributed_proj.log'.format(host)
FORMAT = '%(asctime)-15s %(message)s'


def get_logger(name):
    logging.basicConfig(filename=LOGGING_FILE, format=FORMAT, level=logging.INFO)
    return logging.getLogger(name)
