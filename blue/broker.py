#!/usr/bin/env python
# coding=utf-8
import argparse
import zmq
from zmq.eventloop import ioloop, zmqstream


PEERS = set()


io_loop = ioloop.IOLoop()

context = zmq.Context()
socket = context.socket(zmq.ROUTER)


def broker(stream, message):
    # raise Exception(message)
    # HELLOFROM <my ip address> <port number>
    print message
    msg = message[0].split()
    PEERS.add(msg[0])
    message[0] = ' '.join(PEERS)
    stream.send_multipart(message)


zmqstream.ZMQStream(socket, io_loop=io_loop).on_recv_stream(broker)

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--bind-address', default='tcp://127.0.0.1:5555')
args = parser.parse_args()


socket.bind(args.bind_address)
io_loop.start()
