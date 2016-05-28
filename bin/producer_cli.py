#!/usr/bin/python

import time
import threading
import socket
from collections import deque
from cluster.utils.logging_util import get_logger
from cluster import CONFIG
import zmq

HEARTBEAT_PERIOD = CONFIG['heart_beat_period']
MASTER_ADDR = CONFIG['machine_list']['master'].values()[0]
PORT = CONFIG['port']
# ADDR_STR = 'tcp://*:{0}'.format(PORT)
ADDR_STR = 'tcp://127.0.0.1:{0}'.format(PORT)
import pdb


class Producer(object):

    def __init__(self):
        self._logger = get_logger('Producer')
        self._logger.info("Producer {0} started".format(socket.gethostname()))
        self._status = True
        self._ctx = zmq.Context.instance()
        self._skt = self._ctx.socket(zmq.PULL)
        self._skt.bind(ADDR_STR)
        self._monitor = threading.Thread(target=self.send_heart_beat, args=())
        self._monitor.start()
        self.job_q = deque()

    def receive_heart_beat(self):
        self._logger.info("Start listening heartbeat!")
        while self._status:
            self._skt.recv()
            self._logger.info("Received heartbeat sent from {0}".format(socket.gethostname()))

    def stop(self):
        self.__exit__('', '', '')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._status = False
        self._heart_beater.join()
        self._logger.info("Heartbeat stopped; consumer finished")

if __name__ == '__main__':
    print 'start'
    producer = Producer()
    time.sleep(10)
    producer.stop()
