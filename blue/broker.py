# coding=utf-8
import argparse
import zmq
from zmq.eventloop import ioloop, zmqstream


PEERS = set()


io_loop = ioloop.IOLoop()

context = zmq.Context()

socket = context.socket(zmq.ROUTER)


stream = zmqstream.ZMQStream(socket, io_loop=io_loop)


def echo(stream, message):
    # raise Exception(message)
    # HELLOFROM <my ip address> <port number>
    reply = 'OK'
    msg = message[1].split()

    if msg[0] == 'HELLOFROM':
        PEERS.add(msg[1])

    elif msg[0] == 'WHO':
        reply = ' '.join(PEERS)

    message[1] = reply
    stream.send_multipart(message)

stream.on_recv_stream(echo)

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--bind-address', default='tcp://127.0.0.1:5555')

args = parser.parse_args()

socket.bind(args.bind_address)
io_loop.start()
