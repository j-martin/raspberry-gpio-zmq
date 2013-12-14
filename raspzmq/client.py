import sys
import zmq
from logger import logger
from time import sleep
import config

config = config.load()['general']

logger.name = __name__.upper()

server = config['server']
port = config['port']
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)
    
if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

logger.info("Collecting updates from server...")
socket.connect ("tcp://%s:%s" % (server,port))

# Subscribe to zipcode, default is NYC, 10001
topicfilter = "26"
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)

while 1:
	logger.info(socket.recv())
	sleep(5)