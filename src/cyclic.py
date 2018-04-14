"""
A simple library of functions that provide scikit-learn-esque
feature engineering and preprocessing tools.
MIT License
Taylor Pellerin, https://www.linkedin.com/in/tjpell
"""

import numpy as np

class CyclicEncoder:
    """
    Encode time series data with sin and cosine transformations to their values.

    Attributes
    ----------
    period : period for cycle of time series data

    methods : trigonometric transformation to apply to target data
    """

    def __init__(self):
        self.period = None
        self.method = None

    def fit(self, period):
        self.period = period
        return self

    def transform(self, y, method=('sin', 'cos')):
        self.method = method
        period = self.period

        if not all(m in ['sin', 'cos'] for m in methods):
            print("Error: please supply a valid method, such \
                  as sin or cos")
        out = []

        if 'sin' in method:
            sin = [np.sin(2*np.pi*v/period) for v in y]
            out.append(sin)
        if 'cos' in method:
            cos = [np.cos(2*np.pi*v/period) for v in y]
            out.append(cos)
        return out


    def fit_transform(self, y, period, method=['sin', 'cos']):
        self.period = period
        self.method = method

        if not all(m in ['sin', 'cos'] for m in method):
            print("Error: please supply a valid method, such \
                  as sin or cos")
        out = []

        if 'sin' in method:
            sin = [np.sin(2*np.pi*v/period) for v in y]
            out.append(sin)
        if 'cos' in method:
            cos = [np.cos(2*np.pi*v/period) for v in y]
            out.append(cos)
        return out