import configuration

def test_load():
    configuration.load()

def test_reformat_mapping():

	data = [{'pin':'2', 'value1':'ok', 'value2':'nay'}]

	result = configuration.test_reformat_mapping(data)

	print result