# Listens for wallet queries and responds accordingly

import zmq

class Comm:
    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind('tcp://*:1337')

    def run(self, wallet):
        while True:
            message = self.socket.recv_multipart()
            op = message[0].decode('utf-8')
            reply = 'Unknown operation'
            if op == 'balance':
                if len(message) == 2:
                    cc = message[1].decode('utf-8')
                    b = wallet.balance(cc)
                    reply = str(b)
                    print('Sending balance (' + str(b) + ') for ' + cc)
            elif op == 'pay':
                # TODO: add actual payment verification
                if len(message) == 4:
                    cc = message[1].decode('utf-8')
                    amt = float(message[2].decode('utf-8'))
                    address = message[3].decode('utf-8')
                    wallet.pay(cc, amt)
                    reply = 'ok'
                    print('Paying ' + str(amt) + ' ' + cc)
            elif op == 'receive':
                # TODO: add actual payment verification
                if len(message) == 2:
                    cc = message[1].decode('utf-8')
                    wallet.receive(cc, 1)
                    reply = 'wallet-address'
                    print('Receiving 1 ' + cc)



            self.socket.send_string(reply)
