from protos import index


def test_index():
    assert index.hello() == "Hello protos"
