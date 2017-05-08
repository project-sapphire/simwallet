import zmq
import sys


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:1337')

while True:
    inp = input('\n-$ ')
    data = []
    for s in inp.split():
        data.append(s.encode('utf-8'))

    socket.send_multipart(data)
    rep = socket.recv()
    print('\nREPLY:')
    print(rep)
