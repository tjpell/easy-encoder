"""
A simple library of functions that provide scikit-learn-esque
feature engineering and preprocessing tools.
MIT License
Taylor Pellerin, https://www.linkedin.com/in/tjpell
"""

import pandas as pd
import numpy as np

class UnknownEncoder:
    """
    Encode validation data with a preset "unknown value" for observations that were not
    in the test set.

    Attributes
    ----------
    classes_ : array of shape (n_class,)
        Holds the label for each class.

    unk_val : int, None, string
                  Value to replace new observations with
    """

    def __init__(self):
        self.classes_ = dict()
        self.unk_val = None

    def fit(self, y):
        """Fit unknown encoder

        Parameters
        ----------
        y : array-like of shape (n_samples,)
            Target values.

        Returns
        -------
        self : returns an instance of self.
        """

        # create dict of values in input for quicker lookups
        values_dict = dict()
        [values_dict.update({val: ""}) for val in y]
        self.classes_ = values_dict  # keep this around

        return self

    def transform(self, y, unk_val=None):
        """
        Parameters
        ----------
        y : array-like of shape (n_samples,)
            Target values.

        unk_val : int, None, string
                  Value to replace new observations with
        """

        # make sure that every value in val and test is in train. if not, replace with unk_val
        self.unk_val = unk_val if unk_val else None
        values_dict = self.classes_

        val_col = [unk_val if values_dict.get(v) is None else v for v in y.values]

        return pd.Series(val_col)

    def fit_transform(self, y, unk_val=None):
        raise NotImplementedError


