from json import loads

def loadConfig():
	data = open(config.json).read()
	return loads(data)