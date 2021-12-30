"""
Helper class to facilitate working with Statistics Denmark's API. See the
official API documentation here
https://www.dst.dk/da/Statistik/brug-statistikken/muligheder-i-statistikbanken/api

Author: Alessandro Tang-Andersen Martinello
"""
import requests
import warnings
import pandas as pd
from io import StringIO


class DstApi:
    def __init__(self, tablename) -> None:
        self.apiip = "https://api.statbank.dk/v1"
        self.tablename = str(tablename).lower()
        self.tableinfo = None

    def tablesummary(self, verbose=True, language='da'):
        """
        Returns a summary of a published DST table containing the description of
        the table and of the variables according to which the values are
        reported
        """
        # Get table info from API
        if self.tableinfo is None:
            self.tableinfo = self._get_tableinfo(language=language)

        # Make report
        if verbose:
            print(f"Table {self.tableinfo['id']}: {self.tableinfo['description']}")
            print(f"Last update: {self.tableinfo['updated']}")

        table = self._wrap_tableinfo_variables(self.tableinfo)
        return table

    def variable_levels(self, varname, language='da'):
        """
        Returns a DataFrame with the possible values of `varname` in the table.
        """
        # Get table info from API
        if self.tableinfo is None:
            self.tableinfo = self._get_tableinfo(language=language)

        try:
            return pd.DataFrame(
                [i for i in self.tableinfo["variables"] if i["id"] == varname][0][
                    "values"
                ]
            )
        except IndexError as err:
            print(
                """
                Error: The table does not seem to contain the requested variable.
                Check the spelling (variable names are case sensitive
                )"""
            )
            return err

    def get_data(self, params=None, language='da', as_DataFrame=True, override_warning=False):
        """
        Downloads table data according to API call specified in `params`. If
        `params` is None (default), parameters resulting in the download of the
        entire data table will be automatically generated, raising a warning.

        The function returns a Pandas DataFramse by default. Specify
        `as_DataFrame=False` to obtain the original `requests.Response` object
        """
        if params is None:
            if override_warning is False:
                warnings.warn((
                    "API call parameters are not specified. Parameters resulting "
                    "in the download of the entire table will be automatically generated. "
                    "This can result in massive data downloads."
                ), stacklevel=2)
                answer = input("Continue (Y/Yes)?")
            else:
                answer = "yes"
            if answer.lower() in ["y", "yes"]:
                params = self._define_base_params(language=language)
            else:
                print("Execution aborted")
                return

        r = requests.post(self.apiip + "/data", json=params)
        if as_DataFrame:
            return pd.read_csv(StringIO(r.text), sep=';', decimal=',')
        else:
            return r

    def _get_tableinfo(self, language='da'):
        tableinfo = self.tableinfo = requests.get(
            self.apiip + "/tableinfo",
            params={"id": self.tablename, "format": "JSON", 'lang': language}
        ).json()
        return tableinfo

    def _define_base_params(self, language='da'):
        """
        Return a parameter dictionary resulting in the download of an entire
        data table. Use with caution.
        """
        ts = self.tablesummary(verbose=False)

        variables = [{'code': var, 'values': ['*']} for var in ts['variable name']]
        params = {
            'table': 'metrox1',
            'format': 'BULK',
            'lang': language,
            'variables': variables
        }

        return params

    @staticmethod
    def _wrap_tableinfo_variables(tiresponse):
        toplist = []
        for var in tiresponse["variables"]:
            vallist = [var["id"]]
            vallist.append(len(var["values"]))
            vallist.append(var["values"][0]["id"])
            vallist.append(var["values"][0]["text"])
            vallist.append(var["values"][-1]["id"])
            vallist.append(var["values"][-1]["text"])
            vallist.append(var["time"])
            toplist.append(vallist)
        return pd.DataFrame(
            toplist,
            columns=[
                "variable name",
                "# values",
                "First value",
                "First value label",
                "Last value",
                "Last value label",
                "Time variable",
            ],
        )
