# coding=utf-8

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import argparse
import time
import zmq


from utils import get_local_ip

context = zmq.Context()

dealer_socket = context.socket(zmq.DEALER)
router_socket = context.socket(zmq.ROUTER)

# parser = argparse.ArgumentParser()
# parser.add_argument('-c', '--connect-address', default='tcp://127.0.0.1:5555')
#
# args = parser.parse_args()

dealer_socket.connect('tcp://127.0.0.1:5555')
router_socket.connect('tcp://127.0.0.1:5556')
while 1:
    msg = "{}:{}".format(get_local_ip(), '5555')
    print 'Sending address to the dealer', msg
    dealer_socket.send(msg)
    print dealer_socket.recv()

    print 'Asking router...'
    router_socket.send('WHO')
    print router_socket.recv()
    time.sleep(1)
