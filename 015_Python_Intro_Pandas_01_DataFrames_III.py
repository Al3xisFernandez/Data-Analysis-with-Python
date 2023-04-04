from __init__ import *


import os

def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')

def pausa():
    temp=input("\tPresione una tecla para continuar")

limpiar();
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║    ╔═══════╗            ╦                                   ╦   ╔═══╦═══╗   ║
║    ║                    ║                                   ║       ║       ║
║    ║                    ║                                   ║       ║       ║
║    ║                    ║                                   ║       ║       ║
║    ╠══════╣     ╔═══════╣    ╦       ╦    ╔═══════╗         ║       ║       ║
║    ║            ║       ║    ║       ║    ║                 ║       ║       ║
║    ║            ║       ║    ║       ║    ║          ╔╗     ║       ║       ║
║    ╚═══════╝    ╚═══════╝    ╚═══════╝    ╚═══════╝  ╚╝     ╩       ╩       ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
║                                                                             ║
║                                                                             ║
║    ╔══════╗    ╦       ╦   ╔═══╦═══╗   ╦       ╦    ╔═════╗    ╔╗      ╦    ║
║    ║      ╚╗   ╚╗     ╔╝       ║       ║       ║   ╔╝     ╚╗   ║╚╗     ║    ║
║    ║       ║    ╚╗   ╔╝        ║       ║       ║   ║       ║   ║ ╚╗    ║    ║
║    ║      ╔╝     ╚╗ ╔╝         ║       ║       ║   ║       ║   ║  ╚╗   ║    ║
║    ╠══════╝       ╚╦╝          ║       ╠═══════╣   ║       ║   ║   ╚╗  ║    ║
║    ║               ║           ║       ║       ║   ║       ║   ║    ╚╗ ║    ║
║    ║               ║           ║       ║       ║   ╚╗     ╔╝   ║     ╚╗║    ║
║    ╩               ╩           ╩       ╩       ╩    ╚═════╝    ╩      ╚╝    ║
║                                                                             ║
║                                ╦                                            ║
║                               ╔╝                                            ║
║                               ╩                                             ║
║      ╔════╗   ╔╗     ╦   ╔════╗   ╦         ╦    ╔════╗   ╦    ╔════╗       ║
║     ╔╝    ╚╗  ║╚╗    ║  ╔╝    ╚╗  ║         ║   ╔╝    ╚╗  ║   ╔╝    ╚╗      ║
║     ║      ║  ║ ╚╗   ║  ║      ║  ║         ║   ║         ║   ║             ║
║     ║      ║  ║  ╚╗  ║  ║      ║  ║         ║   ╚╗        ║   ╚╗            ║
║     ╠══════╣  ║   ╚╗ ║  ╠══════╣  ║         ║    ╚════╗   ║    ╚════╗       ║
║     ║      ║  ║    ╚╗║  ║      ║  ║         ║         ╚╗  ║         ╚╗      ║
║     ║      ║  ║     ╚╣  ║      ║  ║         ║   ╚╗    ╔╝  ║   ╚╗    ╔╝      ║
║     ╩      ╩  ╩      ╩  ╩      ╩  ╚══════╝  ╩    ╚════╝   ╩    ╚════╝       ║
║                                                                             ║
║  ╔═════╗   ╔══════╗      ╔═════╗    ╔════╗  ╔═══╦═══╗   ╔════╗     ╔════╗   ║
║  ║     ╚╗  ║             ║     ╚╗  ╔╝    ╚╗     ║      ╔╝    ╚╗   ╔╝    ╚╗  ║
║  ║      ║  ║             ║      ║  ║      ║     ║      ║      ║   ║         ║
║  ║      ║  ║             ║      ║  ║      ║     ║      ║      ║   ╚╗        ║
║  ║      ║  ╠═════╣       ║      ║  ╠══════╣     ║      ║      ║    ╚════╗   ║
║  ║      ║  ║             ║      ║  ║      ║     ║      ║      ║         ╚╗  ║
║  ║     ╔╝  ║             ║     ╔╝  ║      ║     ║      ╚╗    ╔╝   ╚╗    ╔╝  ║
║  ╚═════╝   ╚══════╝      ╚═════╝   ╩      ╩     ╩       ╚════╝     ╚════╝   ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
''')







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
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                               mas ejemplos                                  ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
pausa()
print("*"*50)
####################################################################################################
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})


print ("clasificamos/dividimos en terminos de 'cortes' el DF ")
cortes = [0, 3, 6, 10]
df['cortes'] = pd.cut(df['A'], cortes)
print(f"{df=}")

print ("clasificamos/dividimos en x=4 el DF ")
x=4
df['cortes qcut'] = pd.qcut(df['A'], x)


print(f"{df=}")

pausa()
print("*"*50)


####################################################################################################
print("df.at:\n",df.at,"\nAccess a single value for a row/column label pair.")
print("df.attrs:\n",df.attrs,"\nDictionary of global attributes on this object.")
print("df.axes:\n",df.axes,"\nReturn a list representing the axes of the df.")
print("df.columns:\n",df.columns,"\nThe column labels of the df.")
print("df.dtypes:\n",df.dtypes,"\nReturn the dtypes in the df.")
print("df.empty:\n",df.empty,"\nIndicator whether df is empty.")
print("df.index:\n",df.index,"\nThe index (row labels) of the df.")
print("df.loc:\n",df.loc,"\nAccess a group of rows and columns by label(s) or a boolean array.")
print("df.iloc:\n",df.iloc,"\nPurely integer-location based indexing for selection by position.")
print("df.iat:\n",df.iat,"\nAccess a single value for a row/column pair by integer position.")
print("df.ndim:\n",df.ndim,"\nReturn an int representing the number of axes / array dimensions.")
print("df.shape:\n",df.shape,"\nReturn a tuple representing the dimensionality of the df.")
print("df.size:\n",df.size,"\nReturn an int representing the number of elements in this object.")
# ~ print("df.style:\n",df.style,"\nReturns a Styler object.")
print("df.values:\n",df.values,"\nReturn a Numpy representation of the df.")
pausa()
limpiar()
print("*"*50)

####################################################################################################
import pandas as pd
import numpy as np
print ("*"*104)
print ("*","apply".center(100),"*")
print ("*"*104)
df = pd.DataFrame(np.random.randint(10, size=(5,5)), columns=list('ABCDE'))
print(f"original=\n{df}")
def promedio(row_col):
    return row_col.mean()
df1=df.apply(promedio,axis=0)
print(f"df.apply(promedio,axis=0)=\n{df1}")
df1=df.apply(promedio,axis=1)
print(f"df.apply(promedio,axis=1)=\n{df1}")
pausa()
####################################################################################################
print ("*"*104)
print ("*","applymap".center(100),"*")
print ("*"*104)
df = pd.DataFrame(np.random.randint(10, size=(5,5)), columns=list('ABCDE'))
print(f"original=\n{df}")
df1=df.applymap(lambda x : x**2)
print(f"df.applymap(lambda x : x**2)=\n{df1}")
pausa()
####################################################################################################
print ("*"*104)
print ("*","mean".center(100),"*")
print ("*"*104)
df = pd.DataFrame(np.random.randint(10, size=(5,5)), columns=list('ABCDE'))
print(f"original=\n{df}")
df1=df.mean(axis=0)
print(f"df.mean(axis=0)=\n{df1}")
df1=df.mean(axis=1)
print(f"df.mean(axis=1)=\n{df1}")
pausa()
limpiar()
####################################################################################################
print ("*"*104)
print ("*","map".center(100),"*")
print ("*"*104)
df = pd.DataFrame(np.random.randint(10, size=(5,5)), columns=list('ABCDE'))
print(f"original=\n{df}")
df1['A']=df['A'].map(lambda x: x**2)
print(f"df['A'].map(lambda x: x**2)=\n{df1['A']}")
df1=df.iloc[0,:].map(lambda x: x**2)
print(f"df.iloc[0,:].map(lambda x: x**2)=\n{df1}")
pausa()
print("*"*50)
###################################################################################################

df_bicicletas = pd.DataFrame(data={"dueño" :{"Juan","Ana","Pedro","Lu","Vito","Vivi","Jor","Benja","Eze","Andrea"},
                 "rodado":{14,26,14,28,26,14,28,26,14,28},                
                 "cuadro":{"cross","carrera","montain","cross","carrera","montain","cross","carrera","montain","carrera"},
                 "color" :{"rojo","verde","azul","amarilla","negra","celeste","celeste","violeta","gris","mostaza"},
                 "canasta":{True,False,True,False,True,False,True,False,True,False}
                 })
                 
print (f"DataFrame=\n",df_bicicletas)
