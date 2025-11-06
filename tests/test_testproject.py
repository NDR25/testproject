import pytest


def test_import_testproject():
    try:
        import testproject           # noqa
    except ImportError:
        pytest.fail('import testproject failed')
