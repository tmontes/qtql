from PyQt5.QtCore import QLocale


def name():
    """
    Returns system detected locale as a 'cc_LL' formatted string where:
    - cc is a 2-letter country code
    - LL is a 2/3-letter language code.
    """
    return QLocale.system().name()


def shortname():
    """
    Returns uppercased 2-letteer country code from system detected locale.
    """
    return name()[:2].upper()
