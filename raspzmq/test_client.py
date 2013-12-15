import raspzmq.client

def test_starting_the_client():
	m = raspzmq.client.subscriber()

	print(dir(m))
