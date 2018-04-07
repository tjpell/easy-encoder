"""
A simple library of functions that provide scikit-learn-esque
feature engineering and preprocessing tools.
MIT License
Taylor Pellerin, https://www.linkedin.com/in/tjpell
"""

import pandas as pd
import numpy as np

class CyclicEncoder:
    """
    Encode validation data with a preset "unknown value" for observations that were not
    in the test set.

    Attributes
    ----------
    classes_ : array of shape (n_class,)
        Holds the label for each class.
    """

    def __init__(self):
        self.classes_ = dict()
        self.unk_val = None