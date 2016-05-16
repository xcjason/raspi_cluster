#!/usr/bin/python

import time
import threading
import socket
from cluster.utils.logging_util import get_logger
from cluster import CONFIG

HEARTBEAT_PERIOD = CONFIG['heart_beat_period']
import pdb


class Consumer(object):

    def __init__(self):
        self._logger = get_logger('Consumer')
        self._logger.info("Consumer {0} started".format(socket.gethostname()))
        self._status = True
        self._heart_beater = threading.Thread(target=self.send_heart_beat, args=())
        self._heart_beater.start()
        self.job_list = {}

    def send_heart_beat(self):
        self._logger.info("Heartbeat Start!")
        while self._status:
            skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                skt.sendto('msg', ('192.168.171.134', 43287,))
                self._logger.info("Heartbeat sent from {0}".format(socket.gethostname()))
            except:
                pass
            time.sleep(HEARTBEAT_PERIOD)

    def stop(self):
        self.__exit__('', '', '')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._status = False
        self._heart_beater.join()
        self._logger.info("Heartbeat stopped; consumer finished")

if __name__ == '__main__':
    print 'start'
    consumer = Consumer()
    time.sleep(10)
    consumer.stop()
