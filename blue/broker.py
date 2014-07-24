#!/usr/bin/env python
# coding=utf-8
import argparse
import zmq
from zmq.eventloop import ioloop, zmqstream


PEERS = set()


io_loop = ioloop.IOLoop()

context = zmq.Context()

dealer_socket = context.socket(zmq.DEALER)
router_socket = context.socket(zmq.ROUTER)


def broker(stream, message):
    # raise Exception(message)
    # HELLOFROM <my ip address> <port number>
    print 'BROKER:', message
    msg = message[0].split()
    PEERS.add(msg[0])
    message[0] = 'OK'
    stream.send_multipart(message)


def router(stream, message):
    print 'ROUTER:', message
    message[0] = ' '.join(PEERS)
    stream.send_multipart(message)


zmqstream.ZMQStream(dealer_socket, io_loop=io_loop).on_recv_stream(broker)
zmqstream.ZMQStream(router_socket, io_loop=io_loop).on_recv_stream(router)

# parser = argparse.ArgumentParser()
# parser.add_argument('-b', '--bind-address', default='tcp://127.0.0.1:5555')
#2
# args = parser.parse_args()

dealer_socket.bind('tcp://127.0.0.1:5555')
router_socket.bind('tcp://127.0.0.1:5556')
io_loop.start()
