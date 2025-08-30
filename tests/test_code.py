from src.code import up_first


def test_up_first():
    assert  up_first('skypro') == 'Skypro'


def test_upfirst_for_empty():
    assert up_first('') == ''