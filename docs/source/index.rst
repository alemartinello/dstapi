Documentation for the dstapi
===================================

Here you can learn how to use the dstapi.


How to install dstapi
====

For now download the dstapi.py file, and make sure it is in your working directory.
After that just write

   import dstapi

Or

   pip install git+https://github.com/JonasW01ff/dstapi.git#subdirectory=dstapi

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

   **parameters**

                  tablename : string
                     The name of the table as given on dst.dk


   **methods**
      **tablesummary(self, verbose=True, language='da')**
        Returns a summary of a published DST table containing the description of
        the table and of the variables according to which the values are
        reported

        **parameters**
                  verbose : bool
                     If True prints table id, description and when it was last updated
                  language : string
                     "da" for danish version, "en" for english version.

        **returns : DataFrame**
             A DataFrame with information about the dst table


      **variable_levels(self, varname, language='da')**
        Returns a DataFrame with the possible values of `varname` in the table.

        **parameters**
                  varname : string
                     name of the variable you want to see the levels of.
                  language : string
                     "da" for danish version, "en" for english version.



        **returns : DataFrame**
             A DataFrame of values the variable can take.
         
      **get_data(self, params=None, language='da', as_DataFrame=True, override_warning=False)**
        Downloads table data according to API call specified in `params`. If
        `params` is None (default), parameters resulting in the download of the
        entire data table will be automatically generated, raising a warning.
        
        The function returns a Pandas DataFramse by default. Specify
        `as_DataFrame=False` to obtain the original `requests.Response` object

        **parameters**
                  params : dict
                     Dictionary with the parametors to pass to the dstapi.
                  language : string
                     "da" for danish version, "en" for english version.
                  as_DataFrame : bool
                     If true gives back a pandas DataFrame; if not, it gives back a `requests.Response` object.
                  override_warning : bool
                     If True, it warns you if the param variable is not given.



        **returns : DataFrame**
             A DataFrame or a `requests.Response` object of data from dst api.

