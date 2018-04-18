"""
A simple library of functions that provide scikit-learn-esque
feature engineering and pre-processing tools.

MIT License

Taylor Pellerin, https://www.linkedin.com/in/tjpell

Target encoding inspired by the following Kaggle kernel:
https://www.kaggle.com/tnarik/likelihood-encoding-of-categorical-features
"""

import numpy as np
import pandas as pd

from collections import defaultdict
from sklearn.model_selection import KFold

__all__ = ["TargetEncoder"]


class TargetEncoder:
    """
    Encode validation data with a preset "unknown value" for observations that were not
    in the test set.

    Attributes
    ----------
    method : which statistical method to apply to target variable
    data : categorical variable used as a predictor
    values_dict :
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
        """
        Fit target encoder. Builds dictionary mapping {category: list(target values)}

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
        """
        Replace categorical data with target encoded version

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
        Apply standard target encoding, using the stored method.
        Best used on new data. For Training data, use fit_transform.

        :param x: Data that we are going to encode
        :return: Transformed data
        """
        apply_dict = dict()
        applied_method = [apply_dict.update({key, self.method(self.values_dict[key])})
                                                for key in self.values_dict.keys()]

        return [applied_method[val] if applied_method.get(val) else self.fill_val for val in x]


    def regularized_encode(self, x):
        """
        Not yet implemented

        :param x: Data to be transformed
        :return: Message
        """
        # Todo: prepare the regularized encoding functionality, or verify that it doesn't make sense
        print("Not yet implemented, for now, please use fit_transform")


    def fit_transform(self, x, y, method="mean", k=5, fill_na=True):
        """
        For a given pair of categorical and response data, create a column of target encoded data. Default behavior
        expects that we are going to fit transform training data, with k fold regularization. For test data, it is
        recommended that you fit on training data and transform the new data.

        :param x: Categorical variable to apply the encoding for
        :param y: Target variable, either label encoded categories or continuous values
        :param method: Numpy method that we wish to apply to target data
        :param k: Order of k-fold cross validation that we wish to apply
        :param fill_na: Whether or not to fill Nones in x with the result of applying method to all target data

        :return:
        """

        if k > 1:
            df = pd.DataFrame([x, y], columns=["x", "y"])
            return self.reg_target_encoding(df, method, k, fill_na)

        # Just do target encoding without regularization if k is not greater than 1 (or is None)
        self.fit(x, y)
        return self.transform(x, method, fill_na)


    def reg_target_encoding(self, df, method="mean", k=5, fill_na=True):
        """ Computes regularize target encoding.

        Inputs:
           train: training dataframe

        """
        col = "X"
        new_col_name = "X_enc"
        kf = KFold(n_splits=k)
        df[new_col_name] = None

        for method_index, apply_index in kf.split(df):
            if method == "mean":
                method_on_fold = df.loc[method_index].groupby(col).y.mean()  # get mean of train
                if fill_na:
                    global_method = df.loc[method_index].y.mean()  # get global mean for na imputation

            if method == "sd":
                method_on_fold = df.loc[method_index].groupby(col).y.sd()  # get mean of train
                if fill_na:
                    global_method = df.loc[method_index].y.sd()  # get global mean for na imputation

            # apply the new method to the data
            df.loc[apply_index, new_col_name] = df.loc[apply_index, col].map(method_on_fold)  # apply train mean to test
            if fill_na:
                df.loc[apply_index, new_col_name].fillna(global_method, inplace=True)

        return df["X_enc"]

