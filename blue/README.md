# Run broker in host pegasus

To start the broker:
python broker.py -b tcp://172.16.17.6:5556

To connect the clients:
python client.py -c tcp://172.16.17.6:5556

The client in hider mode:
python client.py -c tcp://172.16.17.6:5556 -H
