Documentation for the dstapi
===================================

Here you can learn how to use the dstapi. Just click the links below.

.. note::

   This project is under active development.

How to install dstapi
====

For now download the dstapi.py file, and make sure it is in your working directory.
After that just write

   import dstapi
Using DST's API with Python
=====

The scope of this repository is to provide a guide for using Denmark Statistics' API using python.

You can find the full guide in this notebook.

The guide also presents a helper class I wrote to more easily access DST's data, DstApi. The class is defined in the python file dstapi.py.

This class is useful to visualize a table's metadata, as in the example below, and to import data from DST directly into pandas.

I hope you'll find this guide useful!

.. code-block:: console

  dnkapi = DstApi("dnkapi")
  display(dnkapi.tablesummary(langauge="en"))
  display(dnkapi.variable_levels("INSTRUMENTS", language ="en"))


Class DstApi
------

   A class that will be representative for you dst table

   parameters:
   ^^^^^^
                  tablename : String
                     The name of the table as given on dst.dk







Contents:

.. toctree::
   :maxdepth: 2

.. automodule:: dstapi
   :members:

.. autoclass:: DstApi
   :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
