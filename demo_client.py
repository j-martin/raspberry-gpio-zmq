import raspzmq.client as client

s = client.subscriber(config_path = "./config/")
s.run() #Simple infinite look so the client keep running