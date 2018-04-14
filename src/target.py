"""
A simple library of functions that provide scikit-learn-esque
feature engineering and preprocessing tools.
MIT License
Taylor Pellerin, https://www.linkedin.com/in/tjpell
"""

import numpy as np

from sklearn.model_selection import KFold
from collections import defaultdict

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
        self.values_dict = None
        self.k = None

        self.fill_na = True
        self.fill_val = None


    def fit(self, x, y):
        """Fit unknown encoder

        Parameters
        ----------
        :param x: array-like of shape (n_samples,)
            Categorical predictor values.

        :param y: array-like of shape (n_samples,)
            Target values.

        :param method : which statistical method to apply to input data.
                 Recommended uses include np.mean, max, variance

        k : which order of regularization to apply.

        fill_na : whether or not to apply global method (such as mean)
                  when filling in NA values

        Returns
        -------
        self : returns an instance of self.
        """

        if len(x) != len(y):
            print("Size mismatch")

        # put all values associated with each variable in a list
        values_dict = defaultdict(list)
        [values_dict[key].append(val) for key, val in zip(x,y)]

        self.values_dict = values_dict
        self.data = y
        return self


    def transform(self, x, method=np.mean(), k=None, fill_na=True):
        """Replace categorical value with target encoded version

        Parameters
        ----------
        :param x: array-like of shape (n_samples,)
            Categorical predictor values.

        :param method: which statistical method to apply to input data.
                 Recommended uses include np.mean, max, variance

        :param k: which order of regularization to apply.

        :param fill_na: whether or not to apply global method (such as mean)
                  when filling in NA values

        Returns
        -------
        :return: an instance of self
        """
        self.method = method
        self.k = k
        self.fill_na = fill_na

        if fill_na:
            self.fill_val = self.method(self.data)

        return self.regularized_encode(x) if k else self.encode(x)


    def encode(self, x):
        """

        :param x: data that we
        :return:
        """
        apply_dict = dict()
        applied_method = [apply_dict.update({key, self.method(self.values_dict[key])})
                                                for key in self.values_dict.keys()]

        return [applied_method[val] if applied_method.get(val) else self.fill_val for val in x]


    # it might make more sense for the regularized encoding to be a "fit_transform"

    def regularized_encode(self, x):
        # Todo: prepare the regularized encoding functionality
        pass
    #
    #     enc = np.array()
    #
    #     # Work in progress
    #     kf = KFold(n_splits=k)
    #     for compute_on, apply_to in kf.split(y):
    #         four = y.loc[compute_on]
    #         computed = method(four.groupby(col))
    #         enc = y.loc[apply_to, col].map(computed)
    #
    #     if fill_na:
    #         global_mean = method(y)
    #         y.fillna(global_mean, inplace=True)
    #
    #     return enc

