Qt QLocale Test
===============

Sample project to diagnose Qt's QLocale calls and mocks in AppVeyor.

Motivation: understand why this `PR <https://github.com/mu-editor/mu/pull/764>`_ is failing when building in AppVeyor.


Installation
------------

Clone and install width:

.. code-block:: console

	$ pip install .



Using
-----

.. code-block:: python

    import qtql

    locale = qtql.name()



Testing
-------

.. clode-block:: console

	$ pip install -e .[dev]
	$ pytest


About
-----

Created by Tiago Montes.

