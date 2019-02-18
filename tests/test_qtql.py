from unittest import mock

import qtql


def test_name_returns_string():
    # Really call into Qt.
    name = qtql.name()
    assert isinstance(name, str)


def test_name_returns_non_emty_string():
    # Really call into Qt.
    name = qtql.name()
    assert len(name) > 0


def test_short_name_for_es_MX_is_ES():
    # Mocking Qt call.
    qlocale_system = mock.Mock()
    qlocale_system.name.return_value = 'es_MX'
    with mock.patch('PyQt5.QtCore.QLocale.system', return_value=qlocale_system):
        shortname = qtql.shortname()

    assert shortname == 'ES'