Lib Cove OC4IDS
===============

|Build Status| |Coverage Status|

Command line
------------

Call ``libcoveoc4ids`` and pass the filename of some JSON data.

::

   libcoveoc4ids tests/fixtures/api/basic_1.json

Code for use by external users
------------------------------

The only code that should be used directly by users is the ``libcoveoc4ids.config`` and ``libcoveoc4ids.api`` modules.

Other code (in ``lib``, etc.) should not be used by external users of this library directly, as the structure and use of these may change more frequently.

.. |Build Status| image:: https://secure.travis-ci.org/open-contracting/lib-cove-ocds.png
   :target: https://travis-ci.org/open-contracting/lib-cove-ocds
.. |Coverage Status| image:: https://coveralls.io/repos/github/open-contracting/lib-cove-ocds/badge.svg?branch=master
   :target: https://coveralls.io/github/open-contracting/lib-cove-ocds?branch=master
