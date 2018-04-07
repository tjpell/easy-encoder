class UnknownEncoder:
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
    def fit(self, y, unk_val=None):
        """Fit unknown encoder
        Parameters
        ----------
        y : array-like of shape (n_samples,)
            Target values.
        
        unk_val : int, NA, string
                  Value to replace new observations with
        Returns
        -------
        self : returns an instance of self.
        """
        
        self.unk_val = unk_val
        
        values = list(set(y.values))
        values.append(unk_val)  # add unk to this list so that encoder will have a value
        values_dict = dict() # create dict of values in train column for quicker lookups
        
        [values_dict.update({val: ""}) for val in y]  
            
        self.classes_ = values_dict  # keep this around
        
        return self
    
    
    def transform(self, y):
        # make sure that every value in val and test is in train. if not, replace with unk_val
        
        values_dict = self.classes_
        unk_val = self.unk_val
        
        val_col = [unk_val if values_dict.get(v) is None else v for v in y.values]
        return pd.Series(val_col)
    
    def fit_transform(self, y, unk_val=None):
        raise NotImplementedError
#         train_list = list(set(train_col.values))
#         train_list.append(unk_val)  # add unk to this list so that encoder will have a value
#         train_dict = dict() # create dict of values in train column for quicker lookups
#         for val in train_list:
#             train_dict[val] = ""
#         # make sure that every value in val and test is in train. if not, replace with unk_val
#         val_col = [unk_val if train_dict.get(v) is None else v for v in val_col.values]
#         return train_list, pd.Series(val_col)

