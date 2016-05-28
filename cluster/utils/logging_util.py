import logging
import sys
from socket import gethostname

hostname = gethostname()

host = 'jason' if hostname == 'ubuntu' else 'pi'
LOGGING_FILE = '/home/{0}/log/distributed_proj.log'.format(host)
FORMAT = '%(asctime)-15s %(message)s'


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(FORMAT)

    fh = logging.FileHandler(LOGGING_FILE)
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger
