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
ADDR_STR = 'tcp://*:{0}'.format(PORT)


class Producer(object):

    def __init__(self):
        self._logger = get_logger('Producer')
        self._logger.info("Producer {0} started".format(socket.gethostname()))
        self._status = True
        self._ctx = zmq.Context.instance()
        self._skt = self._ctx.socket(zmq.PULL)
        self._skt.bind(ADDR_STR)
        self._monitor = threading.Thread(target=self.receive_heart_beat, args=())
        self._monitor.daemon = True
        self._monitor.start()
        self.job_q = deque()

    def receive_heart_beat(self):
        self._logger.info("Start listening heartbeat!")
        while self._status:
            msg = self._skt.recv_json()
            if msg:
                print msg
                self._logger.info("PRODUCER received heartbeat sent from {0}".format(socket.gethostname()))

    def stop(self):
        self.__exit__('', '', '')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._status = False
        self._monitor.join()
        self._logger.info("Stop receiving Heartbeat; producer exit")

if __name__ == '__main__':
    producer = Producer()
    time.sleep(20)
    producer.stop()
