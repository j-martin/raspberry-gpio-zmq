from raspzmq.mapping import mapping

m = mapping()


def test_get_channels():
    print m.get_channels()


def test_get_message():
    print m.get_message('26', 1)
    print m.get_message('3', 0)


def test_reformat_mapping():

    data = [{'pin': '2', 'value1': 'ok', 'value2': 'nay', 'sensor': 'Door'}]
    expected = {'2': {'value1': 'ok', 'value2': 'nay', 'sensor': 'Door'}}

    result = m.reformat_mapping(data)

    assert(result == expected)

    data = [{'pin': '2', 'value1': 'ok', 'value2': 'nay', 'sensor': 'Unused'}]
    expected = {} # Nothing because the sensor is unused

    result = m.reformat_mapping(data)

    assert(result == expected)


    data = [{'pin': '10', 'value1': 'ok', 'value10': 'nay', 'sensor': 'used'}]
    expected = {'10': {'value1': 'ok', 'value10': 'nay', 'sensor': 'used'}}

    result = m.reformat_mapping(data)

    assert(result == expected)
