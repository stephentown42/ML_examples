
import os
from pathlib import Path


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns



def main():
    

    # Methods for loading
    file_path = Path('') 

    df = pd.read_csv( file_path)
    df = pd.read_csv( file_path, usecols=['a','b'], parse_dates=['date_col'])

    # Methods used to check dataframe
    df.head()
    df.describe(percentiles=[0.1, 0.25, 0.5, 0.8])
    df.info()

    # Data wrangling
    df = (
        df
        .rename(columns={'a':'A'})
        .astype({'b':np.int64})
        .assign(new_col = lambda x: x.A**4)
    )

    # Pivoting
    df_long = df_wide.melt(id_vars='location', value_vars=['sun','rain'], var_name='weather', value_name='hours')   # Imagine dataset with separate columns for hours of sun and rain at different locations

    # Grouping and filtering
    grp = df.groupby(by=['a','c'])
    grp_agg = grp.agg({'e':['mean', 'sum','count','max']})

    filtered = df.query(f"a < {insert_value}")

    idx = df[df['a'] < test_value].index
    filtered = df.loc[idx, 'b']


if __name__ == '__main__':
    main()