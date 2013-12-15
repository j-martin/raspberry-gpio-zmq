import raspzmq.server

class fakeGPIO(object):
	"""docstring for GPIO"""
	def __init__(self):
		
		self.BOARD
		self.IN
		self.BOTH
		self.PUD_DOWN

	def setup(self, *kargs):
		pass
	
	def setmode(self, *kargs):
		pass
	def add_event_detect(self, *kargs):
		pass
	def input(self, *kargs):
		pass
	def setmode(self, *kargs):
		pass
	def setmode(self, *kargs):
		pass

def test_starting_the_server():
	GPIO = fakeGPIO()
	m = publisher()
	