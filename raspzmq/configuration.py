from json import loads


def load():
    config = {}
    data = open("config_general.json").read()
    config['general'] = loads(data)
    data = open("config_mapping.json").read()
    config['mapping'] = reformat_mapping(loads(data))

    return config


def reformat_mapping(data):

    processed_data = {}

    for item in data:

        pin = item['pin']
        item.pop('pin')

        processed_data.update({pin: item})

    return processed_data
