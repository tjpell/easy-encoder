"""
A simple library of functions that provide scikit-learn-esque
feature engineering and preprocessing tools.
MIT License
Taylor Pellerin, https://www.linkedin.com/in/tjpell
"""

import pandas as pd
import numpy as np

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
