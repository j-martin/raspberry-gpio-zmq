import raspzmq.configuration


def test_load():
    config = raspzmq.configuration.load('./config/')

    assert (len(config) > 3)
