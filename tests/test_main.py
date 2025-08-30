from src.main import divide


def test_divide():
    assert  divide(2, 1) == 2

    assert divide(2, 0) == 0