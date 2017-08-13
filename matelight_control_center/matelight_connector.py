import threading

import socket
from time import sleep

import numpy as np
from PIL import Image


class Sendworker(threading.Thread):

    def __init__(self, host, data):
        super().__init__()
        self.host = host
        self.data = data
        self.stop = False
        self.socket = socket.socket(type=socket.SOCK_DGRAM)

    def run(self):
        while True:
            if self.stop:
                return
            self.socket.sendto(self.data, (self.host, 1337))
            sleep(10)


class MatelightConnector:

    def __init__(self, hostname='display.ilexlux.xyz'):
        self.hostname = hostname
        self.is_running = False
        self.worker = None

        # TODO make this adjustable
        self.image_width = 15
        self.image_height = 16

    def show_color(self, color, length=10):
        image = Image.new("RGB", (self.image_width, self.image_height), color=color)

        if self.worker is not None and self.worker.is_alive():
            self.worker.stop = True
            self.worker.join()

        self.worker = Sendworker(self.hostname, np.array(image, dtype=np.uint8))
        self.worker.start()
        self.is_running = True

    def stop(self):
        if self.is_running:
            self.worker.stop = True
            self.worker.join()
