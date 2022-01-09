import pandas as pd
from functools import wraps



def apply_to_df(func):
    """
    A dacorator fucntion, that takes a fucntion that operates on a single detection (row or obj),
    and returns a function that operates on an entire dataframe. The result will be saved as a new
    column that has the filter's name
    """
    @wraps(func)
    def df_function(df, *args, **kwargs):
        df[func.__name__] = df.apply(lambda row: func(row, *args, **kwargs), axis=1)
        return df

    return df_function


def parameterless_function(*args, **kwargs):
    """
    A dacorator fucntion, that takes a fucntion, and returns a function with all parameters set except the dataFrame paramter.
    """
    def wrapper(func):
        @wraps(func)
        def non_parameterized_function(df):
            func(df, *args, **kwargs)

        return non_parameterized_function

    return  wrapper