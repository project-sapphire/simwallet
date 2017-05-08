import zmq
import sys


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:1337')

while True:
    s = input('\n-$ ')
    socket.send_string(s)
    rep = socket.recv()
    print('\nREPLY:')
    print(rep)
