import socket
import time
import yaml
import logging
from cluster import CONFIG


class HeartBeat:
    def __init__(self):
        self.meta_data = {}
        self._set_name()
        self._set_target()
        self._beat_time = time.time()

    def _set_target(self):
        self._targets = None
        target_list = CONFIG['machine_list']['master']
        if self._name not in target_list:
            self._targets = target_list.values()

    def _set_name(self):
        self._name = socket.gethostname()

    def get_name(self):
        return socket.gethostname()

    @property
    def get_time(self):
        return self._beat_time

if __name__ == '__main__':
    heart_beat = HeartBeat()
