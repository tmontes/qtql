Qt QLocale Test
===============

Sample project to diagnose Qt's QLocale calls and mocks in AppVeyor.

Motivation: understand why this `PR <https://github.com/mu-editor/mu/pull/764>`_ is failing when building in AppVeyor.

AppVeyor project page is `here <https://ci.appveyor.com/project/tmontes/qtql>`_.


Lesson
------

For some reason, importing `QLocale` with `from PyQt5.Qt import QLocale` leads to AppVeyor import time hangs; the solution seems to be importing it with `from PyQt5.QtCore import QLocale`, instead.


Installation
------------

Clone and install with:

.. code-block:: console

	$ pip install .



Using
-----

.. code-block:: python

    import qtql

    locale = qtql.name()



Testing
-------

.. code-block:: console

	$ pip install -e .[dev]
	$ pytest


About
-----

Created by Tiago Montes.
