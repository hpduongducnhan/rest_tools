# -*- coding: utf-8 -*-
import ndd_rest_tools


def test_welcome():
    try:
        ndd_rest_tools.welcome()
        assert True
    except Exception:
        assert False
