****************
thonny-crosshair
****************

.. image:: https://github.com/mristin/thonny-crosshair/workflows/Continuous%20Integration%20-%20Ubuntu/badge.svg
    :alt: Continuous Integration - Ubuntu

.. image:: https://github.com/mristin/thonny-crosshair/workflows/Continuous%20Integration%20-%20OSX/badge.svg
    :alt: Continuous Integration - OSX

.. image:: https://github.com/mristin/thonny-crosshair/workflows/Continuous%20Integration%20-%20Windows/badge.svg
    :alt: Continuous Integration - Windows

.. image:: https://coveralls.io/repos/github/mristin/thonny-crosshair/badge.svg?branch=main
    :target: https://coveralls.io/github/mristin/thonny-crosshair?branch=main
    :alt: Test coverage

.. image:: https://badge.fury.io/py/thonny-crosshair.svg
    :target: https://badge.fury.io/py/thonny-crosshair
    :alt: PyPI - version

.. image:: https://img.shields.io/pypi/pyversions/thonny-crosshair.svg
    :alt: PyPI - Python Version


Thonny-crosshair is a plug-in for `Thonny IDE`_ to automatically test
Python code using `CrossHair`_.

.. _Thonny IDE: https://thonny.org/
.. _CrossHair: https://github.com/pschanely/CrossHair


Installation
============
In Thonny
---------
The plug-in can be easily installed *via* Thonny.
Go to ``Tools`` menu and select ``Manage plug-ins...``:

.. image:: https://raw.githubusercontent.com/mristin/thonny-crosshair/main/readme/manage_plugins.png
    :alt: Tools -> Manage plug-ins...
    :width: 916
    :height: 472

TODO: screenshot
Search for ``thonny-crosshair`` on PyPI and click on the link to install it:

.. image:: https://raw.githubusercontent.com/mristin/thonny-crosshair/main/readme/search_on_pypi.png
    :alt: Search on PyPI
    :width: 1251
    :height: 984

With pip
--------
In your virtual environment, invoke:

.. code-block::

    pip install --user thonny-crosshair

Usage
=====
To check all the functions in the file with `CrossHair`, go to ``Tools``
menu and select ``Check the current file with CrossHair``:

.. image:: https://raw.githubusercontent.com/mristin/thonny-crosshair/main/readme/tools_check.png
    :alt: Tools -> Check
    :width: 909
    :height: 475

All changes to the file will be saved prior to executing the tests.
If you prefer, you can undo them.

TODO: capture
The check will be executed in the Thonny shell:

.. image:: https://raw.githubusercontent.com/mristin/thonny-crosshair/main/readme/shell.png
    :alt: Shell running the tests
    :width: 1317
    :height: 1045

You can stop the check with the "Stop" sign:

.. image:: https://raw.githubusercontent.com/mristin/thonny-crosshair/main/readme/stop.png
    :alt: Stop the checks
    :width: 741
    :height: 378

Sometimes it is practical to check only a single function (*e.g.*, if it takes too long
to check the whole file).
In that case, move the caret to the body of the function that you would like to verify,
go to ``Tools`` menu and select ``Check the function under the caret with
CrossHair``:

.. image:: https://raw.githubusercontent.com/mristin/thonny-crosshair/main/readme/tools_check_at.png
    :alt: Tools -> Check at
    :width: 917
    :height: 471

TODO: capture
Additionally, `CrossHair` can check your code while you type and immediately warn you
of coding mistakes.
To check the current file continuously, go to ``Tools`` menu and select ``Check the
current file with CrossHair continuously``:

.. image:: https://raw.githubusercontent.com/mristin/thonny-crosshair/main/readme/tools_check_at.png
    :alt: Tools -> Watch


Contributing
============

Feature requests or bug reports are always very, very welcome!

Please see quickly if the issue does not already exist in the `issue section`_ and,
if not, create `a new issue`_.

.. _issue section: https://github.com/mristin/thonny-crosshair/issues
.. _a new issue: https://github.com/mristin/thonny-crosshair/issues/new

You can also contribute in code.
Please see `contributing.rst`_.

.. _contributing.rst: https://github.com/mristin/thonny-crosshair/blob/main/contributing.rst

Versioning
==========
We follow a bit unusual semantic versioning schema:

* X is the oldest supported version of `CrossHair`_,
* Y is the minor version (new or modified features), and
* Z is the patch version (only bug fixes).
