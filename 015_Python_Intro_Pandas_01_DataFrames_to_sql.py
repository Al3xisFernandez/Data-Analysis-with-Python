from Estructura import *
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
from pandas import Series
from pandas import DataFrame
import seaborn as sns
limpiar()
def ya_hechos():
	pass
	metodos = ['abs', 'add', 'add_prefix', 'add_suffix', 'agg', 'aggregate', 'align', 'all', 'any', 'append', 'apply', 'applymap', 'asfreq', 'asof', 'assign', 'astype', 'at', 'at_time', 'attrs', 'axes', 'backfill', 'between_time', 'bfill', 'bool', 'boxplot', 'clip', 'columns', 'combine', 'combine_first', 'compare', 'convert_dtypes', 'copy', 'corr', 'corrwith', 'count', 'cov', 'cummax', 'cummin', 'cumprod', 'cumsum', 'describe', 'diff', 'div', 'divide', 'dot', 'drop', 'drop_duplicates', 'droplevel', 'dropna', 'dtypes', 'duplicated', 'empty', 'eq', 'equals', 'eval', 'ewm', 'expanding', 'explode', 'ffill', 'fillna', 'filter', 'first', 'first_valid_index', 'flags', 'floordiv', 'from_dict', 'from_records', 'ge', 'get', 'groupby', 'gt', 'head', 'hist', 'iat', 'idxmax', 'idxmin', 'iloc', 'index', 'infer_objects', 'info', 'insert', 'interpolate', 'isin', 'isna', 'isnull', 'items', 'iteritems', 'iterrows', 'itertuples', 'join', 'keys', 'kurt', 'kurtosis', 'last', 'last_valid_index', 'le', 'loc', 'lookup', 'lt', 'mad', 'mask', 'max', 'mean', 'median', 'melt', 'memory_usage', 'merge', 'min', 'mod', 'mode', 'mul', 'multiply', 'ndim', 'ne', 'nlargest', 'notna', 'notnull', 'nsmallest', 'nunique', 'pad', 'pct_change', 'pipe', 'pivot', 'pivot_table', 'plot', 'pop', 'pow', 'prod', 'product', 'quantile', 'query', 'radd', 'rank', 'rdiv', 'reindex', 'reindex_like', 'rename', 'rename_axis', 'reorder_levels', 'replace', 'resample', 'reset_index', 'rfloordiv', 'rmod', 'rmul', 'rolling', 'round', 'rpow', 'rsub', 'rtruediv', 'sample', 'select_dtypes', 'sem', 'set_axis', 'set_flags', 'set_index', 'shape', 'shift', 'size', 'skew', 'slice_shift', 'sort_index', 'sort_values', 'sparse', 'squeeze', 'stack', 'std', 'style', 'sub', 'subtract', 'sum', 'swapaxes', 'swaplevel', 'tail', 'take', 'to_clipboard', 'to_csv', 'to_dict', 'to_excel', 'to_feather', 'to_gbq', 'to_hdf', 'to_html', 'to_json', 'to_latex', 'to_markdown', 'to_numpy', 'to_parquet', 'to_period', 'to_pickle', 'to_records', 'to_sql', 'to_stata', 'to_string', 'to_timestamp', 'to_xarray', 'transform', 'transpose', 'truediv', 'truncate', 'tshift', 'tz_convert', 'tz_localize', 'unstack', 'update', 'value_counts', 'values', 'var', 'where', 'xs']

	print("*"*50)
	####################################################################################################
	print("""\033[1;37;44m\n
	╔═════════════════════════════════════════════════════════════════════════════╗
	║                                  PANDAS                                     ║
	╠═════════════════════════════════════════════════════════════════════════════╣
	║                                  to_sql                                     ║
	╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
import pandas as pd
jobs_df = pd.read_csv('data/nyc-jobs.csv')



table_name = 'nyc_jobs'
jobs_df.to_sql(
    table_name,
    engine,
    if_exists='replace',#'''Passing replace to this argument will drop the existing table and replace it with the data & data types associated with the current DataFrame. append will keep the existing table the same, but append all rows in the DataFrame to the existing table.'''

    index=False,
    '''When True, the resulting table will honor your DataFrame's index to create a column with the appropriate key in your database  How to behave if the table already exists.

fail: Raise a ValueError.
replace: Drop the table before inserting new values.
append: Insert new values to the existing table.'''
    chunksize=500,#'''Passing a number to this parameter will attempt to upload your data as a stream of "chunks" n rows at a time, as opposed to all at once. Passing a chunksize is useful for particularly large datasets that may be at risk of interruption during upload.'''
    dtype={
        "job_id": Integer,
        "agency": Text,
        "business_title": Text,
        "job_category":  Text,
        "salary_range_from": Integer,
        "salary_range_to": Integer,
        "salary_frequency": String(50),
        "work_location": Text,
        "division/work_unit": Text,
        "job_description": Text,
        "posting_date": DateTime,
        "posting_updated": DateTime
    }''' Passing a Python dictionary to dtype lets us explicitly set the datatypes of each column in our database,
         where each key is the column name and each value is the data type (I highly recommend doing this). 
         You'll notice we import various data types from sqlalchemy.types, which we then associate with each column's name. 
         If the target SQL table doesn't exist yet, passing these datatypes will ensure that each SQL column is created with the appropriate data constraint,
         as opposed to each column rendered simply as "text." If a target SQL table does exist, these data types must match the types of the existing table, or you'll receive a SQL error during the upload.'''
#https://hackingandslacking.com/connecting-pandas-to-a-database-with-sqlalchemy-b6a187675c4a
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html



https://www.w3resource.com/pandas/dataframe/dataframe-to_sql.php








