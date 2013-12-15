import raspzmq.server as server

s = server.publisher(config_path = "./config/")
s.run() #Simple infinite look so the server keep running