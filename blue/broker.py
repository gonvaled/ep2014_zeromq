# coding=utf-8
import argparse
import zmq
from zmq.eventloop import ioloop, zmqstream


PEERS = set()


io_loop = ioloop.IOLoop()

context = zmq.Context()
socket = context.socket(zmq.ROUTER)


def broker(stream, message):
    print message
    msg = message[1].split()
    if msg[0] == 'REGISTER':
        PEERS.add(msg[1])
        message[1] = ' '.join(PEERS)
    elif msg[0] == 'LIST':
        message[1] = ' '.join(PEERS)
    else:
        message[1] = 'ERROR'
    stream.send_multipart(message)


zmqstream.ZMQStream(socket, io_loop=io_loop).on_recv_stream(broker)

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--bind-address', default='tcp://127.0.0.1:5555')
args = parser.parse_args()

print 'Binding broker to {}'.format(args.bind_address)

socket.bind(args.bind_address)
io_loop.start()
