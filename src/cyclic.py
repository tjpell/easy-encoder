"""
A simple library of functions that provide scikit-learn-esque
feature engineering and preprocessing tools.

MIT License

Taylor Pellerin, https://www.linkedin.com/in/tjpell

Inspiration drawn from Ian London's blog post:
https://ianlondon.github.io/blog/encoding-cyclical-features-24hour-time/
"""

import numpy as np

class CyclicEncoder:
    """
    Encode time series data with sin and cosine transformations to their values.

    Attributes
    ----------
    period : period for cycle of time series data

    method : trigonometric transformation to apply to target data, like 'sin' and 'cos'
    """

    def __init__(self):
        self.period = None
        self.method = None


    def fit(self, period):
        """
        Trivially provide the period of the data to be encoded

        :param period: The period of the cyclic data to be encoded

        :return: returns an instance of self.
        """
        self.period = period
        return self


    def transform(self, y, method=('sin', 'cos')):
        """
        Transform the provided data using the trig methods provided

        :param y: Data that we wish to transform
        :param method: Trig transformation to apply to the data

        :return: Trandformed data
        """
        self.method = method
        if not all(m in ('sin', 'cos') for m in method):
            print("Error: please supply a valid method, such \
                  as sin or cos")

        ret = []
        if 'sin' in method:
            ret.append([np.sin(2*np.pi*v/self.period) for v in y])
        if 'cos' in method:
            ret.append([np.cos(2*np.pi*v/self.period) for v in y])
        return ret


    def fit_transform(self, y, period, method=('sin', 'cos')):
        """
        T

        :param y: Data that we wish to transform
        :param method: Trig transformation to apply to the data

        :return: Trandformed data
        """
        self.period = period
        self.method = method

        if not all(m in ('sin', 'cos') for m in method):
            print("Error: please supply a valid method, such \
                  as sin or cos")
        ret = []

        if 'sin' in method:
            sin = [np.sin(2*np.pi*v/period) for v in y]
            ret.append(sin)
        if 'cos' in method:
            cos = [np.cos(2*np.pi*v/period) for v in y]
            ret.append(cos)
        return ret
