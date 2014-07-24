#!/usr/bin/env python
# coding=utf-8

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import argparse
import time
import zmq


from utils import get_local_ip

context = zmq.Context()

socket = context.socket(zmq.DEALER)

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--connect-address', default='tcp://127.0.0.1:5555')
parser.add_argument('-H', '--hider', default=False, action='store_true')
parser.add_argument('-C', '--city',  default='Barcelona')

args = parser.parse_args()

socket.connect(args.connect_address)

hider = args.hider
city = args.hider
myip = get_local_ip()
address = args.connect_address

while 1:
    if hider : command = "REGISTER {}:{}".format(myip, '5555')
    else     : command = "LIST"
    print 'Sending command "{}" to dealer {}'.format(command, address)
    socket.send(command)
    print socket.recv()
    time.sleep(1)
