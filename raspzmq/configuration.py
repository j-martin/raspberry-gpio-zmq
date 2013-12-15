from json import loads

def load():
    data = open("config/general.json").read()
    return loads(data)