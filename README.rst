Lib Cove OC4IDS
===============

|PyPI Version| |Build Status| |Coverage Status| |Python Version|

Command line
------------

Call ``libcoveoc4ids`` and pass the filename of some JSON data.

::

   libcoveoc4ids tests/fixtures/api/basic_1.json

Code for use by external users
------------------------------

The only code that should be used directly by users is the ``libcoveoc4ids.config`` and ``libcoveoc4ids.api`` modules.

Other code (in ``lib``, etc.) should not be used by external users of this library directly, as the structure and use of these may change more frequently.


.. |PyPI Version| image:: https://img.shields.io/pypi/v/libcoveoc4ids.svg
   :target: https://pypi.org/project/libcoveoc4ids/
.. |Build Status| image:: https://github.com/open-contracting/lib-cove-oc4ids/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/open-contracting/lib-cove-oc4ids/actions/workflows/ci.yml
.. |Coverage Status| image:: https://coveralls.io/repos/github/open-contracting/lib-cove-oc4ids/badge.svg?branch=main
   :target: https://coveralls.io/github/open-contracting/lib-cove-oc4ids?branch=main
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/libcoveoc4ids.svg
   :target: https://pypi.org/project/libcoveoc4ids/
