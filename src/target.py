"""
A simple library of functions that provide scikit-learn-esque
feature engineering and preprocessing tools.
MIT License
Taylor Pellerin, https://www.linkedin.com/in/tjpell
"""

### not quite working yet

import pandas as pd
import numpy as np
from sklearn.model_selection import KFold

class TargetEncoder:
    """
    Encode validation data with a preset "unknown value" for observations that were not
    in the test set.

    Attributes
    ----------
    method : which method to apply to target variable
    """

    def __init__(self):
        self.method = np.mean()

    def fit(self, y):
        """Fit unknown encoder

        Parameters
        ----------
        y : array-like of shape (n_samples,)
            Target values.

        method : which statistical method to apply to input data.
                 Recommended uses include np.mean, max, variance

        k : which order of regularization to apply.

        fill_na : whether or not to apply global method (such as mean)
                  when filling in NA values

        Returns
        -------
        self : returns an instance of self.
        """


    def transform(self, y, method=np.mean(), k=None, fill_na=True):
        """Fit unknown encoder

        Parameters
        ----------
        y : array-like of shape (n_samples,)
            Target values.

        method : which statistical method to apply to input data.
                 Recommended uses include np.mean, max, variance

        k : which order of regularization to apply.

        fill_na : whether or not to apply global method (such as mean)
                  when filling in NA values

        Returns
        -------
        self : returns an instance of self.
        """
        self.method = method
        self.k = k
        self.


    def reg_target_encoding2(self, train, col, splits=5):
        """ Computes regularize mean encoding.
        Inputs:
           train: training dataframe

        """
        kf = KFold(n_splits=5)
        for four_index, one_index in kf.split(train):
            four = train.loc[four_index]
            mean_device_type = four.groupby(col).Real_Spots.mean()
            train.loc[one_index, col + "_enc"] = train.loc[one_index, col].map(mean_device_type)

        global_mean = train.Real_Spots.mean()
        train[col + '_enc'].fillna(global_mean, inplace=True)