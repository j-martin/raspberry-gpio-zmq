import raspzmq.configuration


def test_load():
    config = raspzmq.configuration.load()

    assert (len(config) == 2)
    assert (len(config['general']) > 3)
    assert (len(config['mapping']) > 10)


def test_reformat_mapping():

    data = [{'pin': '2', 'value1': 'ok', 'value2': 'nay'}]
    expected = {'2': {'value1': 'ok', 'value2': 'nay'}}

    result = raspzmq.configuration.reformat_mapping(data)

    assert(result == expected)


    data = [{'pin': '10', 'value1': 'ok', 'value10': 'nay'}]
    expected = {'10': {'value1': 'ok', 'value10': 'nay'}}

    result = raspzmq.configuration.reformat_mapping(data)

    assert(result == expected)
