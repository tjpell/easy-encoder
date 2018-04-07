"""
A simple library of functions that provide scikit-learn-esque
feature engineering and preprocessing tools.
MIT License
Taylor Pellerin, https://www.linkedin.com/in/tjpell
"""

# not quite working yet

import numpy as np
from sklearn.model_selection import KFold

class TargetEncoder:
    """
    Encode validation data with a preset "unknown value" for observations that were not
    in the test set.

    Attributes
    ----------
    method : which statistical method to apply to target variable
    data : categorical variable used as a predictor
    target : variable that is of predictive interest
    k : what order of cross validation to use for regularization
    fill_na : whether or not to fill NA's with global method (such as mean)
    """

    def __init__(self):
        self.method = np.mean()
        self.data = None
        self.target = None
        self.k = None
        self.fill_na = True

    def fit(self, x, y):
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

        self.data = x
        self.target = y


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
        enc : returns an instance of self.
        """
        self.method = method
        self.k = k
        self.fill_na = fill_na

        enc = np.array()

        kf = KFold(n_splits=k)
        for compute_on, apply_to in kf.split(y):
            four = y.loc[compute_on]
            computed = method(four.groupby(col))
            enc = y.loc[apply_to, col].map(computed)

        if fill_na:
            global_mean = method(y)
            y.fillna(global_mean, inplace=True)

        return enc

