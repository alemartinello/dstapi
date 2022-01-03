# Using DST's API with Python

The scope of this repository is to provide a guide for using [Denmark Statistics' API](https://www.dst.dk/da/Statistik/brug-statistikken/muligheder-i-statistikbanken/api) using python.

You can find the full guide in [this notebook](Using DSTs API with python.ipynb).

The guide also presents a helper class I wrote to more easily access DST's data, `DstApi`. The class is defined in the python file [`dstapi.py`](dstapi.py).

This class is useful to visualize a table's metadata, as in the example below, and to import data from DST directly into pandas.

I hope you'll find this guide useful!

![How to use the DstApi class to visualize a table's metadata](https://github.com/alemartinello/dstapi/blob/7537f38a28eb033743f803a702fd5803c2af72ff/pics/screenshot.png)
