import raspzmq.configuration



def test_load():
    config = raspzmq.configuration.load()

    assert (len(config) > 3)

