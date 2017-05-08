# Listens for wallet queries and responds accordingly

import zmq

class Comm:
    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind('tcp://*:1337')

    def run(self, wallet):
        while True:
            message = self.socket.recv()
            print(message)
            self.socket.send_string('hello')
