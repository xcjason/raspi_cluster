import logging

LOGGING_FILE = '/home/jason/log/distributed_proj.log'
FORMAT = '%(asctime)-15s %(message)s'


def get_logger(name):
    logging.basicConfig(filename=LOGGING_FILE, format=FORMAT, level=logging.INFO)
    return logging.getLogger(name)
