'''
Publisher class
'''

import zmq
import os
import numpy as np



class Publihser():
	def __init__(self, port = 8989):
		self.context = zmq.Context()
		self.socket = self.context.socket(zmq.PUB)

		self.socket.bind(f'tcp://*:{port}')
	def publish_data(self):
		pass