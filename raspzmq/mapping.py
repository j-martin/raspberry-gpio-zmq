from json import loads
from os import path

class mapping(object):

    """docstring for mapping"""

    def __init__(self, config_path = "./config/"):
        self.load(config_path)

    def load(self, config_path):

        config_path += 'mapping.json'

        if path.isfile(config_path):
            data = open(config_path).read()
            self._map = self.reformat_mapping(loads(data))
            return 0
        else:
            print 'Config file not found: %r' % config_path
            exit
            

    def get_channels(self):

        return [int(value) for value in self._map.keys()]

    def get_message(self, channel, state):

        if channel in self._map:

            message = "%s (sensor) as changed to %s. (Pin%s)" % (
                self._map[channel]['sensor'],
                self._map[channel]['state'][state].upper(),
                channel)
            return message

        else:
            return 0

    def reformat_mapping(self, data):

        processed_data = {}

        for item in data:
            if item['sensor'].lower() == 'unused':
                continue

            pin = item['pin']
            item.pop('pin')

            processed_data.update({pin: item})

        return processed_data
