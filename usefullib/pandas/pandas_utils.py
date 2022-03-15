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
        if 'prop_name' in kwargs.keys():
            prop_name = kwargs['prop_name']
            del kwargs['prop_name']

        else:
            prop_name = ''

        if prop_name:
            df[prop_name] = df.apply(lambda row: func(row, *args, **kwargs), axis=1)

        else:
            df[func.__name__] = df.apply(lambda row: func(row, *args, **kwargs), axis=1)

        return df

    return df_function


def apply_many_to_df(func):
    """
    A dacorator fucntion, that takes a fucntion that operates on a single detection (row or obj),
    and returns a function that operates on an entire dataframe. The result from the function hould return as dictionary with the property name
    and the values
    """
    @wraps(func)
    def df_function(df, *args, **kwargs):
        res_dict = {}
        for _, row in df.iterrows():
            current_res_dict = func(row, *args, **kwargs)
            if len(res_dict) == 0:
                for key in current_res_dict.keys():
                    res_dict[key] = [current_res_dict[key]]

            else:
                for key in res_dict.keys():
                    res_dict[key].append(current_res_dict[key])

        # res_dict = df.apply(lambda row: func(row, *args, **kwargs), axis=1)
        # print(res_dict)
        # for key in res_dict.keys():
        #     df[key] = res_dict[key]

        for key in res_dict.keys():
            df[key] = res_dict[key]

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