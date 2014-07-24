# coding=utf-8
import argparse
import time
import zmq

context = zmq.Context()

s = context.socket(zmq.DEALER)

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--connect-address', default='tcp://127.0.0.1:5555')

args = parser.parse_args()

s.connect(args.connect_address)
while 1:
    msg = "HELLOFROM {} {}".format(get_local_ip(), '5555')
    print msg
    s.send(msg)
    print s.recv()

    s.send('WHO')
    print s.recv(), time.time()

    time.sleep(1)
