#!/usr/bin/python

import time
import threading
import socket
from cluster.utils.logging_util import get_logger
from cluster import CONFIG
import zmq

HEARTBEAT_PERIOD = CONFIG['heart_beat_period']
MASTER_ADDR = CONFIG['machine_list']['master'].values()[0]
PORT = CONFIG['port']
ADDR_STR = 'tcp://{0}:{1}'.format(MASTER_ADDR, PORT)


class Consumer(object):

    def __init__(self):
        self._logger = get_logger('Consumer')
        self._logger.info("Consumer {0} started".format(socket.gethostname()))
        self._status = True
        self._ctx = zmq.Context.instance()
        self._skt = self._ctx.socket(zmq.PUSH)
        self._skt.connect(ADDR_STR)
        self._heart_beater = threading.Thread(target=self.send_heart_beat, args=())
        self._heart_beater.daemon = True
        self._heart_beater.start()
        self.job_list = {}

    def send_heart_beat(self):
        self._logger.info("Heartbeat Start!")
        while self._status:
            beat_info = {
                'host': socket.gethostname(),
                'ip': socket.gethostbyname(socket.gethostname()),
                'local_time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            }
            try:
                self._skt.send_json(beat_info)
                self._logger.info("Heartbeat sent from {0}".format(socket.gethostname()))
            except:
                self._logger.error("Failed to send Heartbeat!")
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
    time.sleep(20)
    consumer.stop()
