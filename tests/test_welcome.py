import rest_tools


def test_welcome():
    try:
        rest_tools.welcome()
        assert True
    except Exception:
        assert False