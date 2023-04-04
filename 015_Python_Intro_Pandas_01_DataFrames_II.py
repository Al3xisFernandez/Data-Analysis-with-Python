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
list_listas = [[ 1, 4],[ 2, 3],[ 3, 2],[ 4, 1]]
dataframe1 = pd.DataFrame(data=list_listas, columns=['uno', 'dos'])
print(dataframe1)
pausa()
print("*"*50)
####################################################################################################
dataframe = pd.DataFrame(data=list_listas, columns=['uno', 'dos'],index=[10,11,12,13])
print("df total:\n",dataframe)
print("en at[11,'dos'] encontraras :",dataframe.at[11,'dos'])
pausa()
print("*"*50)
####################################################################################################

dataframe = pd.DataFrame(data=list_listas, columns=['uno', 'dos'],index=['a', 'b', 'c' , 'd'])
print("df total:\n",dataframe)
pausa()
print("*"*50)
####################################################################################################

print("en at['c','dos'] encontraras :",dataframe.at['c','dos'])

print("Sobrescribimos el valor at['c','dos']= 9 ")
dataframe.at['c','dos']=9
print("df total:\n",dataframe)
pausa()
print("*"*50)
####################################################################################################
print("Sobrescribimos el valor at['a','uno']=222 ")
dataframe.at['a','uno']=222
print("df total:\n",dataframe)
pausa()
limpiar()
print("*"*50)
####################################################################################################

dict_listas = {'uno' : [1, 2, 3, 4], 'dos' : [4, 3, 2, 1]}
dataframe = pd.DataFrame(dict_listas)
print("df total:\n",dataframe)
print("en at[1,'dos'] encontraras :",dataframe.at[1,'dos'])
pausa()
limpiar()
print("*"*50)
####################################################################################################

print("Cambio de index de numero a letras")
dataframe = pd.DataFrame(dict_listas, index=['a', 'b', 'c', 'd'])
print("df total:\n",dataframe)
print("en at['c','dos'] encontraras :",dataframe.at['c','dos'])
pausa();print("*"*50)
dict_series = {
                'uno' : [1, 2, 3, 4],
                'dos' : [4, 3, 2, 1]
                }
dataframe = pd.DataFrame(data=dict_series)

dataframe = pd.DataFrame(data=dict_series, index=['a', 'b', 'c', 'd'])
print("df total:\n",dataframe)
print("en at['c','dos'] encontraras :",dataframe.at['c','dos'])
pausa()
limpiar()
print("*"*50)
####################################################################################################
dict_series = {
                'uno'   : Series(["1","28","63","0"],	index=['a', 'b', 'c', 'd']),
                'dos'   : Series(["2","12","53","1"],	index=['a', 'b', 'c', 'd']),
                'tres'  : Series(["3","22","43","2"],	index=['a', 'b', 'c', 'd']),
                'cuatro': Series(["4","32","33","5"],	index=['a', 'b', 'c', 'd']),
                'cinco' : Series(["5","52","23","3"],	index=['a', 'b', 'c', 'd']),
                'seis'  : Series(["6","42","13","4"],	index=['a', 'b', 'c', 'd']),
                'siete' : Series(["7","22","73","6"],	index=['a', 'b', 'c', 'd']),
                'ocho'  : Series(["8","12","83","5"],	index=['a', 'b', 'c', 'd']),
                'nueve' : Series(["9","21","93","4"],	index=['a', 'b', 'c', 'd']),
                'diez'  : Series(["10","31","100","6"],	index=['a', 'b', 'c', 'd'])
                }
dataframe = pd.DataFrame(data=dict_series)
print("df:\n",dataframe)
pausa()
print("-"*50)
print("en at['a','dos'] encontraras :",dataframe.at['a','dos'])
pausa()
print("-"*50)
print("df.head:\n",dataframe.head(10))
pausa()
print("-"*50)
print("df.describe:\n",dataframe.describe())
pausa()
print("-"*50)
pd.set_option('max_rows',99999)
print("df:\n",dataframe)


#dataframe =del dataframe['d']
pausa()
limpiar()
print("*"*50)
####################################################################################################
dict_series = {
                'uno'   : ["1","28","63","0"],		
                'dos'   : ["2","12","53","1"],		
                'tres'  : ["3","22","43","2"],	
                'cuatro': ["4","32","33","5"],	
                'cinco' : ["5","52","23","3"],	
                'seis'  : ["6","42","13","4"],	
                'siete' : ["7","22","73","6"],	
                'ocho'  : ["8","12","83","5"],	
                'nueve' : ["9","21","93","4"],	
                'diez'  : ["10","31","100","6"],
                }
df = pd.DataFrame(data=dict_series,index=['a', 'b', 'c', 'd'])
df=df[['uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez']].astype(int)
original = df.T.copy()	
print("df:\n",df)
pausa()
limpiar()
print("*"*50)


# ~ notacion slicing
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                              tipos de datos                                 ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
dict_series = {	
                'uno' : [1,2,3,4,1,2,3,4],
                'dos' : [4,3,2,1,0,9,8,7],
                'tres': [5,6,7,8,9,10,11,12],
               }
dataframe = pd.DataFrame(dict_series,index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
print("\nDataFrame:\n",dataframe)

dataframe["uno"]=dataframe.uno.astype(int)
dataframe["dos"]=dataframe.dos.astype(int)
dataframe["tres"]=dataframe.tres.astype(int)
print("df:\n",dataframe)
print("-"*50)
print("df.describe:\n",dataframe.describe())
pausa()
limpiar()
print("*"*50)
print("df.index:\n",dataframe.index)
pausa()
print("-"*50)
print("df.columns:\n",dataframe.columns)
pausa()
print("-"*50)
print("df.dtypes:\n",dataframe.dtypes)
pausa()
print("-"*50)
print("df.values:\n",dataframe.values)
pausa()
print("-"*50)
df = dataframe > 2
print("df. booleano dataframe > 2:\n",df)
pausa()
print("-"*50)
df = (dataframe > 2).all()
print("df. booleano (dataframe > 2).all :\n",df)
pausa()
print("-"*50)
df = (dataframe > 2).any()
print("df. booleano (dataframe > 2).any :\n",df)
pausa()
print("-"*50)
print("df.info:\n",dataframe.info)
pausa()
print("-"*50)
print("df.select_dtypes:\n",dataframe.select_dtypes)
pausa()
print("-"*50)
print("df.values:\n",dataframe.values)
pausa()
print("-"*50)
print("df.axes:\n",dataframe.axes)
pausa()
print("-"*50)
print("df.ndim:\n",dataframe.ndim)
pausa()
print("-"*50)
print("df.size:\n",dataframe.size)
pausa()
print("-"*50)
print("df.shape:\n",dataframe.shape)
pausa()
print("-"*50)
print("df.memory_usage:\n",dataframe.memory_usage)
pausa()
print("-"*50)
print("df.empty:\n",dataframe.empty)
pausa()
print("-"*50)
print("df.astype:\n",dataframe.astype)
pausa()
print("-"*50)
print("df.convert_dtypes:\n",dataframe.convert_dtypes)
pausa()
print("-"*50)
print("df.infer_objects:\n",dataframe.infer_objects)
pausa()
print("-"*50)
print("df.copy:\n",dataframe.copy)
pausa()
print("-"*50)
print("df.bool:\n",dataframe.bool)
pausa()
print("-"*50)
print("df.head:\n",dataframe.head)
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("df.at:\n",dataframe.at,"\nAccess a single value for a row/column label pair.")
print("df.attrs:\n",dataframe.attrs,"\nDictionary of global attributes on this object.")
print("df.axes:\n",dataframe.axes,"\nReturn a list representing the axes of the DataFrame.")
print("df.columns:\n",dataframe.columns,"\nThe column labels of the DataFrame.")
print("df.dtypes:\n",dataframe.dtypes,"\nReturn the dtypes in the DataFrame.")
print("df.empty:\n",dataframe.empty,"\nIndicator whether DataFrame is empty.")
print("df.iat:\n",dataframe.iat,"\nAccess a single value for a row/column pair by integer position.")
print("df.iloc:\n",dataframe.iloc,"\nPurely integer-location based indexing for selection by position.")
print("df.index:\n",dataframe.index,"\nThe index (row labels) of the DataFrame.")
print("df.loc:\n",dataframe.loc,"\nAccess a group of rows and columns by label(s) or a boolean array.")
print("df.ndim:\n",dataframe.ndim,"\nReturn an int representing the number of axes / array dimensions.")
print("df.shape:\n",dataframe.shape,"\nReturn a tuple representing the dimensionality of the DataFrame.")
print("df.size:\n",dataframe.size,"\nReturn an int representing the number of elements in this object.")
print("df.style:\n",dataframe.style,"\nReturns a Styler object.")
print("df.values:\n",dataframe.values,"\nReturn a Numpy representation of the DataFrame.")
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("df.mean:\n",dataframe['uno'].mean())
print("df.Todos:\n",dataframe)
print("df.columna uno:\n",dataframe[['uno']])
print("df.columna dos:\n",dataframe[['dos']])
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("df.suma columna:\n",dataframe.sum(axis=0))
dataframe.loc['total_x_Col']=dataframe.sum(axis=0)
print("df.suma columna:\n",dataframe)

print("df.suma fila:\n",dataframe.sum(axis=1))
dataframe.loc[:,'total_x_fila']=dataframe.sum(axis=1)
print("df.suma filas:\n",dataframe)
pausa()
limpiar()
print("*"*50)
####################################################################################################
#		https://www.youtube.com/watch?v=bmM_RhjuT3k
aNumpy= dataframe[['uno']].to_numpy()
funcion=lambda dato: dato**2
aNumpy=funcion(aNumpy)
print(aNumpy)
dataframe.loc[:,'Cuadrado UNO']=aNumpy
print("df.cuadrado columna:\n",dataframe)
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("*"*50)
for x in dataframe.index:
    print(x)
    if dataframe.loc[x,"uno"]>dataframe.loc[x,"dos"]:
        dataframe.loc[x,"mayor"]=dataframe.loc[x,"uno"]
    else:
        dataframe.loc[x,"mayor"]=dataframe.loc[x,"dos"]

print("df.mayor columna:\n",dataframe)
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("""
Parameters

    path_or_buf: The File object to write the CSV data. If this path argument is not provided, the CSV data is returned as a string, and we can print the string to see how our CSV data looks like.
    sep: It is the delimiter for CSV data. It should be the string of length 1, and the default is a comma.
    na_rep: It is a string representing null or missing values; the default is an empty string.
    columns: It is the sequence to specify the columns to include in the CSV output.
    header: The allowed values are boolean or the list of string, default is True. If it is False, then the column names are not written in the output. If the list of string, it’s used to write the column names. The length of the list of the string should be the same as the number of columns being written in the CSV file.
    index: If it is True, the index is included in the CSV data. If it is set to False, the index value is not written in the CSV output.
    index_label: It is used to specify the column name for the index.
""")

datos = [[1,5],[5,6],[9,3]]
dataframe = pd.DataFrame(datos, index=['d', 'b', 'a'], columns=['dos', 'tres'])
print("df total:\n",dataframe)
pausa()
limpiar()
print("*"*50)
####################################################################################################

#serie = Series(dict, index=['pregunta3', 'pregunta1', 'pregunta4')
dict_series = {'uno' : Series([1, 2, 3], index=['a', 'b', 'c']),'dos' : Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
dataframe = pd.DataFrame(dict_series)
print("df total:\n",dataframe)
pausa()
limpiar()
print("*"*50)
####################################################################################################

df = pd.DataFrame(
                    {
                        'turno':	["M","M","M","M","M","M","T","T","T","T"],
                        'nombre': 	['Gabriel', 'Ricardo', 'Ana', 'Daniel', 'Laura', 'Anabel', 'Andrea', 'Ariel', 'Pedro', 'Ines'],
                        'apellido': ['Perez', 'Garcia', 'Gonzalez', 'Gomez', 'Lujan', 'Martinez', 'Molina', 'Costa', 'Gilar', 'Mendez'],
                        'puesto':	['Administracion', 'Marqueting', 'Contable', 'Produccion', 'Mantenimiento', 'Produccion','Produccion', 'Mantenimiento', 'Produccion', 'Mantenimiento'],
                        'nota_1C':[10,9,5,7,8,9,6,7,8,9],
                        'nota_2C':[8,9,10,9,5,7,8,9,6,7],
                        'Final':[9,6,7,8,9,10,9,5,7,8]
                    }, 
                    columns=['turno','nombre', 'apellido', 'puesto','nota_1C','nota_2C','Final'], 
                    )

print (f"df total\n\n{df}\n")
pausa()
limpiar()
df_Alfa = df.copy()
dfNombre=df.copy()
print("*"*50)
####################################################################################################
df['index']=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]#le agregamos un index numérico
#df.set_index("index",inplace=True)	#actualizamos el inice de busqueda
df = df.set_index("index")#actualizamos el inice de busqueda
print (f"df total\n\n{df}\n")
pausa()
limpiar()
dfNombre= df.copy()

print("*"*50)
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                               concatenate                                   ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')

    
df_1 = pd.DataFrame(
    [['Ariel', 68, 84, 78, 96],
    ['Ana'   , 74, 56, 88, 85],
    ['Pedro' , 77, 73, 82, 87]],
    columns=['Nombre', 'Fisica', 'Quimica','Matematica','Literatura'])

df_2 = pd.DataFrame(
    [['Juan' , 72, 67, 91, 83],
    ['Ariel' , 79, 88, 89, 78],
    ['Lisa'  , 78, 69, 87, 92]],
    columns=['Nombre', 'Fisica', 'Quimica','Matematica','Literatura'])	

df_3 = pd.DataFrame(
    [['Juan' ,  67, 91, 83, 76],
    ['Pedro' ,  88, 88, 88, 88],
    ['Lisa'  ,  69, 87, 92, 67]],
    columns=['Nombre', 'Fisica', 'Quimica','Matematica','Literatura'])	
    
    
#concatenate dataframes
dfSalida = pd.concat([df_1, df_2, df_3], sort=False , ignore_index=True)
#print dataframe
print("df_1\n------\n",df_1)
print("\ndf_2\n------\n",df_2)
print("\ndf_3\n------\n",df_3)
print("\ndfSalida\n--------\n",dfSalida)


pausa()
#concatenate dataframes
dfSalida = pd.concat([df_1, df_2, df_3], sort=False , axis="columns")
#print dataframe
print("df_1\n------\n",df_1)
print("\ndf_2\n------\n",df_2)
print("\ndf_3\n------\n",df_3)
print("\ndfSalida\n--------\n",dfSalida)
pausa()
limpiar()
print("*"*50)

####################################################################################################

pelis = pd.read_csv('http://bit.ly/imdbratings')
pd.set_option('max_rows',99999)
pd.set_option('max_columns',99999)
print (f"pelis:\n{pelis}")
pausa()
print("-"*50)

pelis_1 = pelis.sample(frac=0.75, random_state=1234)
pelis_2 = pelis.drop(pelis_1.index)#borro lo q ya esta en el primero

print (pelis_1,"\n",pelis_1.index.sort_values())
pausa()
print("-"*50)

print (pelis_2,"\n",pelis_2.index.sort_values())
pausa()
print("-"*50)
####################################################################################################
    
pelOp=pelis[	(pelis.genre == 'Action')|
                (pelis.genre == 'Mystery')|
                (pelis.genre == 'Family')|
                (pelis.genre == 'Sci-Fi')
                ]
print (pelOp)
pausa()
print("-"*50)

pelOp=pelis[pelis.genre.isin(['Action','Mystery','Family','Sci-fi'])]
print (pelOp)


pelOp=pelis[~pelis.genre.isin(['Action','Mystery','Family','Sci-fi'])]
print ("inverso\n",pelOp)


pausa()
print("-"*50)
####################################################################################################
    
pelisCant=pelis.genre.value_counts()
print ("pelisCant\n",pelisCant)
pausa()
print("-"*50)
####################################################################################################
    
pelisCantLargest=pelisCant.nlargest(10)
print ("pelisCant\n",pelisCantLargest,pelisCantLargest.index )
pausa()
print("-"*50)
####################################################################################################
    

pelisCant2=pelis[pelis.genre.isin(pelisCant.nlargest(10).index)].head(10)
print ("pelisCant\n",pelisCant2)
pausa()
print("-"*50)

limpiar()

dfNombre= df.copy()

print("*"*50)
####################################################################################################
    
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                  append                                     ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')

df_1 = pd.DataFrame(
    [['Ariel', 68, 84, 78, 96],
    ['Ana', 74, 56, 88, 85],
    ['Pedro', 77, 73, 82, 87]],
    columns=['Nombre', 'Fisica', 'Quimica','Matematica','Literatura'])

df_2 = pd.DataFrame(
    [['Juan', 72, 67, 91, 83],
    ['Ariel', 88, 88, 88, 88],
    ['Lisa', 78, 69, 87, 92]],
    columns=['Nombre', 'Fisica', 'Quimica','Matematica','Ingles'])	


#concatenate dataframes
dfSalida = df_1.append(df_2, sort=False , ignore_index=True)

#print dataframe
print("df_1\n------\n",df_1)
print("\ndf_2\n------\n",df_2)

print("\ndfSalida\n--------\n",dfSalida)


pausa()
limpiar()
dfNombre= df.copy()

print("*"*50)
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                               shape - forma                                 ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')

print('The DataFrame is :\n', df)

#get dataframe shape
shape = df.shape
print('\nDataFrame Shape :', shape)
print('\ncantidad de filas :', shape[0])
print('\ncantidad de columnas :', shape[1])

pausa()
limpiar()
dfNombre= df.copy()


print("*"*50)
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                           startswith // endswith                            ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
dfNombre=df.copy()
print ("\noriginal df:\n:",dfNombre)
print("-"*50)
dfNombre=df.loc[df['nombre'].str.startswith("An")]
print ("dataframe por nombre inicien con 'An' :\n",dfNombre)
print("-"*50)
dfNombre = dfNombre.reset_index()
print ("dataframe reset_index() :\n",dfNombre)
print("-"*50)
# ~ dfNombre.to_csv('salidaDeDatos2.csv',header=True, index=False)
# ~ print("Archivo exportado 2")
pausa()
limpiar()
print("*"*50)
####################################################################################################
dfNombre=df.copy()
print ("\noriginal df:\n:",dfNombre)
print("-"*50)
dfNombre=df.loc[df['nombre'].str.endswith("iel")]
print ("dataframe por nombre termine en 'iel' :\n",dfNombre)
print("-"*50)
dfNombre = dfNombre.reset_index()
print ("dataframe reset_index() :\n",dfNombre)
print("-"*50)
# ~ dfNombre.to_csv('salidaDeDatos2.csv',header=True, index=False)
# ~ print("Archivo exportado 2")
pausa()
limpiar()
print("*"*50)
###################################################################################################

dfNombre=df.copy()
print ("\noriginal df:\n:",dfNombre)
print("-"*50)
dfNombre= dfNombre[dfNombre['nombre'].str[:1]=='A']#.str[0]
print ("dataframe por nombre inicie con 'A' :\n",dfNombre)
pausa()
limpiar()
print("*"*50)


###################################################################################################

dfNombre=df.copy()
print ("\noriginal df:\n:",dfNombre)
print("-"*50)
# ~ print(dfNombre[dfNombre['puesto'].str[4:7]])
dfNombre1= dfNombre[dfNombre['puesto'].str.lower().str.find('cion')==-1]
print ("dataframe por puesto que no tengan  tengan 'cion' :\n",dfNombre1)
pausa()
dfNombre2= dfNombre[dfNombre['puesto'].str.lower().str.find('cion')!=-1]
print ("dataframe por puesto que tengan  tengan 'cion' :\n",dfNombre2)
pausa()

limpiar()
####################################################################################################
df_turno_M=df.loc[(df['turno']=='M')]
df_turno_T=df.loc[(df['turno']=='T')]
print ("\n\ndf_turno_M:\n:",df_turno_M)
print ("\n\ndf_turno_T:\n:",df_turno_T)

print ("\n\ndf_cantidad turno:\n:",df['turno'].count())
print ("\n\ndf_cant-Unicos turno:\n:",df['turno'].nunique())
print ("\n\ndf_Unicos turno :\n:",df['turno'].unique())

pausa()
limpiar()
print("*"*50)
####################################################################################################
print ("\n\ndf_turno_M:\n:",df[(df['turno']=='M')].iloc[:]['nombre'])
print ("\n\ndf_turno_T:\n:",df[(df['turno']=='T')].iloc[:]['nombre'])
pausa()
limpiar()
print("*"*50)
####################################################################################################
print ("\n\ndf_turno_MC:\n:turno manana:",df.loc[(df['turno']=='M')].count()['turno'])
print ("\n\ndf_turno_TC:\n:turno tarde :",df.loc[(df['turno']=='T')].count()['turno'])
pausa()
limpiar()
print("*"*50)
####################################################################################################
df_aprobado=df.loc[(df['nota_1C']>=7)&(df['nota_2C']>=7)]
print ("\n\df_aprobado:\n",df_aprobado)
print ("\n\df_aprobado:\n",df.loc[(df['nota_1C']>=7)&(df['nota_2C']>=7)]['Final'])
print ("\n\df_aprobado:\n",df.loc[(df['nota_1C']>=7)&(df['nota_2C']>=7)]['nombre'])
pausa()
limpiar()
print("*"*50)
####################################################################################################
df['promedio'] = (df ['nota_1C']+df ['nota_2C'])/2
print (f"\n\n{df}\n")
pausa()
limpiar()
print("*"*50)
####################################################################################################

# ~ df = df.set_index("puesto")#actualizamos el inice de busqueda
# ~ print (f"\n\n{df}\n")

print ("\n\correlacion debe tender a 1:\ndf['nota_1C'].corr(df['promedio']\n",df['nota_1C'].corr(df['promedio']))
print ("\n\correlacion debe tender a 1:\ndf['nota_2C'].corr(df['promedio']\n",df['nota_2C'].corr(df['promedio']))
print ("\n\correlacion debe tender a 1:\ndf['nota_1C']+df['nota_2C']).corr(df['promedio']\n",(df['nota_1C']+df['nota_2C']).corr(df['promedio']))
pausa()
limpiar()
print("*"*50)
####################################################################################################
try:
    print ("ver ortografia",list(df))
    col1 = input("ingrese la 1er columna para comparar :")
    col2 = input("ingrese la 2da columna para comparar :")
    correl=df[col1].corr(df[col2])
    if correl >= .90 and correl <=1.1:
        print ("datos relacionados")
    else:
        print ("datos NO relacionados")
    
    print (f"\n\correlacion debe tender a 1:\ndf['{col1}'].corr(df['{col2}']\n",correl)
except:
    print ("error en las variables")

pausa()
limpiar()
print("*"*50)
####################################################################################################


My_dic= {'cero':0,'uno':1,'dos':2,'tres':3,'cuatro':4,'cinco':5,'seis':6,'siete':7,'ocho':8,'nueve':9,'diez':10}

df.Final.value_counts().plot(kind='pie',labels=None,autopct='%1.2f%%',shadow=True,startangle=180,fontsize=12,pctdistance=1.1,labeldistance=1.4)
plt.title("correlacionados")
plt.legend(loc='best',labels=My_dic)
plt.ylabel('Cursos2023')
plt.axis('equal')
plt.show()

pausa()
limpiar()
print("*"*50)
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                  columns                                    ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
dic= {'cero':[0,'zero'],'uno':[1,'one'],'dos':[2,'two'],'tres':[3,'three'],'cuatro':[4,'four'],'cinco':[5,'five'],'seis':[6,'six'],'siete':[7,'seven'],'ocho':[8,'eight'],'nueve':[9,'nine'],'diez':[10,'ten']}

dataframe =pd.DataFrame(dic, index =['num','alfa'])
#dataframe = pd.DataFrame(dict_, index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
print ("original:\n",dataframe)
Nombres_columnas = dataframe.columns.values
print ("Nombres_columnas:",Nombres_columnas)
lista = list(Nombres_columnas)
print ("Py_lista_columnas:",Nombres_columnas)
print("-"*50)
dataframe =dataframe.T
print ("Transpuesto:\n",dataframe)
Nombres_columnas = dataframe.columns.values
print ("Nombres columna T:",Nombres_columnas)
lista = list(Nombres_columnas)
print ("Py_lista_columnas T:",Nombres_columnas)
pausa()
limpiar()
print("*"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                Date  Time                                   ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')	
"""
Parameters
The data to be converted to timedelta.

Deprecated since version 1.2: Strings with units ‘M’, ‘Y’ and ‘y’ do not represent unambiguous timedelta values and will be removed in a future version
unitstr, optional

Possible values:

‘W’
‘D’ / ‘days’ / ‘day’
‘hours’ / ‘hour’ / ‘hr’ / ‘h’
‘m’ / ‘minute’ / ‘min’ / ‘minutes’ / ‘T’
‘S’ / ‘seconds’ / ‘sec’ / ‘second’
‘ms’ / ‘milliseconds’ / ‘millisecond’ / ‘milli’ / ‘millis’ / ‘L’
‘us’ / ‘microseconds’ / ‘microsecond’ / ‘micro’ / ‘micros’ / ‘U’
‘ns’ / ‘nanoseconds’ / ‘nano’ / ‘nanos’ / ‘nanosecond’ / ‘N’
"""

dataframe = pd.read_csv("todatetime.csv") 
print ("original. info:\n",dataframe.dtypes)
print ("original:\n",dataframe)
dataframe["Date"]= pd.to_datetime(dataframe["Date"], errors= 'coerce')# errors= 'raise'
print ("errors= 'coerce' si encuentra un error lo pasa x alto \nerrors= 'raise' si encuentra un error lo presenta")
print ("original Date dtypes:\n",dataframe.dtypes)
print ("original Date:\n",dataframe)
dataframe["Time"]= pd.to_datetime(dataframe["Time"]) 
print ("original Time  dtypes:\n",dataframe.dtypes)
print ("original:\n",dataframe)
print  ("OJO, Agrega la fecha de hoy a la hora del archivo")
pausa()
print("-"*50)
####################################################################################################
dataF_datetime= pd.date_range('2023-01-01',  periods=20, freq='3H')
datos = {'valor_accion':[10,10.2,10.3,10.4,9.5,9.6,9.7,9.8,9.9,10,10,10.2,10.3,10.4,9.5,9.6,9.7,9.8,9.9,10]}
dataframe =pd.DataFrame(data=datos, index =dataF_datetime)
print ("original:\n",dataframe)
df= dataframe.at_time('12:00')
print ("dataframe.at_time('12:00'):\n",df)
pausa()
print("-"*50)
df= dataframe.between_time('9:00', '15:00')
print ("dataframe.between_time('9:00', '15:00'):\n",df)
pausa()
print("-"*50)
####################################################################################################
dataF_datetime= pd.date_range('2023-01-01',  periods=60, freq='1D')#1D Day
rango = list(range (10,610,10))
datos = {'valor_accion':rango}
dataframe =pd.DataFrame(data=datos, index =dataF_datetime)
print ("original:\n",dataframe)
print("-"*50)
df= dataframe.first('5D')
print ("dataframe.first('5D')5 Days:\n",df)

pausa()
print("-"*50)
df= dataframe.last('10D')
print ("dataframe.last('10D')10 Days:\n",df)
pausa()
# ver conversion
print("-"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                       agg  - multiples operaciones                          ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL} 
    El método nos permite pasar una lista de invocables / métodos pandas (la parte de la función sin los paréntesis). 
        .agg(['size','count','sum','mean','median','min','max','std','var'])
    o métodos de la biblioteca numpy para agregar nuestros datos.
        .agg([np.size,np.count_nonzero,np.sum,np.mean,np.median,np.min,np.max,np.std,np.var])


''')	

dict_series = {
                'uno'   : ["1","28","63","0"],		
                'dos'   : ["2","12","53","1"],		
                'tres'  : ["3","22","43","2"],	
                'cuatro': ["4","32","33","5"],	
                'cinco' : ["5","52","23","3"],	
                'seis'  : ["6","42","13","4"],	
                'siete' : ["7","22","73","6"],	
                'ocho'  : ["8","12","83","5"],	
                'nueve' : ["9","21","93","4"],	
                'diez'  : ["10","31","100","6"],
                }
original = pd.DataFrame(data=dict_series,index=['a', 'b', 'c', 'd'])
original=original[['uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez']].astype(int)
dataframe= original.copy()		
print ("original:\n",dataframe)
dataframe = dataframe.agg(['min','max','mean'])
print ("cambios:\n",dataframe)
pausa()
print("-"*50)
####################################################################################################
dataframe= original.T.copy()	
print ("original Transpuesta:\n",dataframe)
dataframe = dataframe.agg({'a':['min'],'b':['max'],'c':['mean']})
print ("cambios:\n",dataframe)
print("-"*50)
pausa()
limpiar()
print("*"*50)
####################################################################################################
dataframe= original.T.copy()	
print ("original Transpuesta:\n",dataframe)
dataframe = dataframe.agg({'a':['min','max'],'b':['mean','std'],'c':['size','count','sum','mean','median','min','max','std','var',list]})
print ("cambios:\n",dataframe)
print("-"*50)
pausa()
limpiar()
print("*"*50)
# ~ ####################################################################################################
# ~ import numpy as np
# ~ dataframe= original.T.copy()	
# ~ print ("original Transpuesta:\n",dataframe)
# ~ dataframe = dataframe.agg([np.size,np.count_nonzero,np.sum,np.mean,np.median,np.min,np.max,np.std,np.var])
# ~ print ("cambios:\n",dataframe)
# ~ print("-"*50)
# ~ pausa()
# ~ limpiar()
# ~ print("*"*50)
####################################################################################################
dataframe= original.T.copy()	
print ("original Transpuesta:\n",dataframe)
dataframe  = dataframe.agg(x=('a', max), y=('b', 'min'), z=('c', np.mean))
print ("cambios:\n",dataframe)
print("-"*50)
pausa()
limpiar()
print("*"*50)
# ~ df.agg("mean", axis="columns")







####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                   index                                     ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')	
dataframe = original.copy()	
print(dataframe.add_prefix('Item_'))
pausa()
print("-"*50)
####################################################################################################
print(dataframe.add_suffix('_2023'))
pausa()
print("*"*50)
dataframe = original.copy()	
print ("cambios:\n",dataframe)
dataframe=dataframe[['a','b','c','d']].astype(int)
idmax = dataframe['a'].idxmax()
print("-"*50)
print ("idmax:",idmax)
pausa()
print("-"*50)
####################################################################################################
print ("esta 'c' in columnas:",'c' in dataframe.columns)
print ("esta 'uno' in lista:",'uno' in dataframe.index)


pausa()
print("-"*50)
####################################################################################################
limpiar()
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                         nsmallests / nlargest                               ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')

dataframe = pd.DataFrame({
                            'population': [59000000, 65000000, 434000, 434000, 434000, 337000, 337000, 11300, 11300],
                            'GDP': [1937894, 2583560 , 12011, 4520, 12128, 17036, 182, 38, 311],
                            'alpha-2': ["IT", "FR", "MT", "MV", "BN", "IS", "NR", "TV", "AI"]},
                            index=["Italy", "France", "Malta", "Maldives", "Brunei", "Iceland", "Nauru", "Tuvalu", "Anguilla"])
print (f"\n\noriginal df:\n {dataframe}\n")

print("-"*50)
print (dataframe.dtypes)
df=dataframe.nsmallest(3,'population')# df.sort_values(columns, ascending=True).head(n)
print (f"dataframe.nsmallest(3,'population'):\n {df}\n")
print("-"*50)
pausa()
####################################################################################################

df=dataframe.nsmallest(4,'population',keep='last')# df.sort_values(columns, ascending=True).head(n)
print (f"dataframe.nsmallest(4,'population',keep='last):\n {df}\n")
print("-"*50)
pausa()
####################################################################################################

df=dataframe.nsmallest(4,'population',keep='all')# df.sort_values(columns, ascending=True).head(n)
print (f"dataframe.nsmallest(4,'population',keep='all'):\n {df}\n")
print("-"*50)
pausa()
####################################################################################################

df=dataframe.nsmallest(4,['population','GDP'])# df.sort_values(columns, ascending=True).head(n)
print (f"dataframe.nsmallest(4,['population','GDP']):\n {df}\n")
print("-"*50)
pausa()
####################################################################################################

countries_population = {"Italy": 59000000, "France": 65000000,
                        "Malta": 434000, "Maldives": 434000,
                        "Brunei": 434000, "Iceland": 337000,
                        "Nauru": 11300, "Tuvalu": 11300,
                        "Anguilla": 11300, "Montserrat": 5200}
df = pd.Series(countries_population)

print("-"*50)
####################################################################################################

df=df.nlargest()
print (f"df.nlargest():\n {df}\n")
print("-"*50)
dataframe = original.T.copy()
pausa()
print("-"*50)
####################################################################################################
limpiar()
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                               str.contains                                  ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
####################################################################################################
df = df_Alfa.copy()
print (f"dataframe():\n {df}\n")
pausa()
df_rec = df[df["puesto"].str.contains("cion")]
print ("df_rec:\n",df_rec)
pausa()
print("-"*50)
####################################################################################################
limpiar()
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                             funcion  Apply II                               ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
####################################################################################################
df = df_Alfa.copy()
print (f"of():\n {df}\n")
def promedio_aula(Final):
    Final = Final * 100
    return Final 
df['total'] = df["Final"].apply(promedio_aula)
print ("df:\n",df)

pausa()
print("-"*50)
####################################################################################################
df = df_Alfa.copy()
print (f"of():\n {df}\n")
def promedion_Tota1(fila):
    salida = (fila['nota_1C']+fila['nota_2C'])/2
    return salida 
df['Final_chequeado'] = df.apply(promedion_Tota1, axis=1)
print ("df:\n",df)
pausa()
print("-"*50)

####################################################################################################
limpiar()
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║            Operaciones entre un DF y una constante o si mismo               ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
####################################################################################################
dic= {'cero':[0,99],'uno':[1,88],'dos':[2,77],'tres':[3,66],'cuatro':[4,55],'cinco':[5,44],'seis':[6,33],'siete':[7,22],'ocho':[8,11],'nueve':[9,0],'diez':[10,1]}

#df = pd.DataFrame ([My_dic])
#df = pd.DataFrame(list(My_dic.items()),columns = ['column1','column2']) 
df = pd.DataFrame.from_dict(dic, orient ='index', columns=['num','alfa'])   
####################################################################################################

print (f"\n\noriginal df1:\n {df}\n")
pausa()
print("*"*50)
print("df.add(10) Add a scalar with operator version which return the same results.")
print (f"\ndf.add(10):\n{df.add(10)}\n")
print("-"*50)
print (f"\ndf.add(df):\n{df.add(df)}\n")
pausa()
print("*"*50)
####################################################################################################
print("df.mul(x) multiplica by constant with reverse version.")
print (f"\ndf.mul(10):\n{df.mul(10)}\n")
print("-"*50)
print (f"\ndf.mul(df):\n{df.mul(df)}\n")
pausa()
print("*"*50)
####################################################################################################
print("df.sub(x) resta by constant with reverse version.")
print (f"\ndf.sub(10):\n{df.sub(10)}\n")
print("-"*50)
print (f"\ndf.sub(df):\n{df.sub(df)}\n")
pausa()
print("*"*50)
####################################################################################################
print("df.div(x) Divide by constant with reverse version.")
print (f"\ndf.div(10):\n{df.div(10)}\n")
print("-"*50)
print (f"\ndf.div(df):\n{df.div(df)}\n")
pausa()
print("*"*50)
####################################################################################################
print("df.rdiv(x) Subtract a list and Series by axis with operator version.")
print (f"\ndf.rdiv(10):\n{df.rdiv(2)}\n")
print("-"*50)
print (f"\ndf.rdiv(df):\n{df.rdiv(df)}\n")
pausa()
print("*"*50)
####################################################################################################
print (f"\ndf- [1,25]:\n{df - [1,25]}\n")
pausa()
print("*"*50)
####################################################################################################
print ("\n\n{df.sub([1, 25], axis='columns')}\n")
print (f"\n\n{df.sub([1, 25], axis='columns')}\n")
pausa()
print("*"*50)
####################################################################################################
print("df.mod(x) Modulo a list and Series by axis with operator version.")
print (f"\ndf.mod(2):\n{df.mod(2)}\n")
pausa()
limpiar()
print("*"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                    Operaciones entre DOS dataframes                         ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
####################################################################################################
# ~ dic_1= {'cero':[0,'zero'],'uno':[1,'one'],'dos':[2,'two'],'tres':[3,'three'],'cuatro':[4,'four'],'cinco':[5,'five'],'seis':[6,'six'],'siete':[7,'seven'],'ocho':[8,'eight'],'nueve':[9,'nine'],'diez':[10,'ten']}
# ~ dic_2= {'A':[0,50],'B':[1,51],'C':[2,52],'D':[3,53],'E':[4,54],'F':[5,55],'G':[6,56],'H':[7,57],'I':[8,58],'J':[9,59],'K':[10,60]}

dic_1= {'A':[0,10],'B':[10,20],'C':[20,30],'D':[30,40],'E':[40,50],'F':[50,60],'G':[60,70],'H':[70,80],'I':[80,90],'J':[90,100],'K':[10,110]}
dic_2= {'A':[1,50],'B':[11,51],'C':[22,52],'D':[30,53],'E':[44,54],'F':[55,55],'G':[66,56],'H':[77,57],'I':[88,58],'J':[99,59],'K':[111,60]}
df1 = pd.DataFrame.from_dict(dic_1, orient ='index', columns=['num','alfa'])   
df2 = pd.DataFrame.from_dict(dic_2, orient ='index', columns=['num','alfa'])   
print("-"*50) 
print (f"\n\noriginal df1:\n {df1}\n")
print("-"*50) 
print (f"\n\noriginal df2:\n {df2}\n")
pausa()
print("*"*50) 

print (f"\ndf1.add(df2):\n{df1.add(df2)}\n")
pausa()
print("*"*50)
####################################################################################################
print (f"\ndf1.mul(df2):\n{df1.mul(df2)}\n")
pausa()
print("*"*50)
####################################################################################################
print (f"\ndf1.sub(df2):\n{df1.sub(df2)}\n")
pausa()
print("*"*50)
####################################################################################################
print (f"\ndf1.div(df2):\n{df1.div(df2)}\n")
pausa()
print("*"*50)
####################################################################################################
print (f"\ndf1.rdiv(df2):\n{df1.rdiv(df2)}\n")
pausa()
print("*"*50)
####################################################################################################
# ~ print (f"\ndf1.dot(df2):\n{df1.dot(df2)}\n")
# ~ pausa()
# ~ print("*"*50)
####################################################################################################

####################################################################################################
print (f"\ndf1.eq(df2) igual:\n{df1.eq(df2)}\n")
pausa()
print("*"*50)
####################################################################################################
print (f"\ndf1.ne(df2) diferente:\n{df1.ne(df2)}\n")
pausa()
print("*"*50)
####################################################################################################

funcion = lambda serie_1, serie_2: serie_1.sum() if serie_1.sum() < serie_2.sum() else serie_2.sum() 

print (f"\nCombine :\n{df1.combine(df2, funcion)}\n")
pausa()
print("*"*50)

####################################################################################################


dic_1= {'A':[0,10,20],'B':[10,20,30],'C':[20,30,40],'D':[30,40,50],'E':[40,50,60],'F':[50,60,70],'G':[60,70,80],'H':[70,80,90]}
dic_2= {'A':[1,50],'B':[11,51],'C':[22,52],'D':[30,53],'E':[44,54],'F':[55,55],'G':[66,56],'H':[77,57],'I':[88,58],'J':[99,59],'K':[111,60]}
df1 = pd.DataFrame.from_dict(dic_1, orient ='index', columns=['uno','dos','tres'])   
df2 = pd.DataFrame.from_dict(dic_2, orient ='index', columns=['uno','dos'])   

print (f"\n\noriginal df1:\n {df1}\n")
print (f"\n\noriginal df2:\n {df2}\n")

####################################################################################################
print (f"\ndf1.eq(df2) igual:\n{df1.eq(df2)}\n")
pausa()
print("*"*50)
####################################################################################################
print (f"\ndf1.ne(df2) diferente:\n{df1.ne(df2)}\n")
pausa()
print("*"*50)

####################################################################################################
funcion = lambda serie_1, serie_2: serie_1.sum() if serie_1.sum() < serie_2.sum() else serie_2.sum() 

print (f"\nCombine :\n{df1.combine(df2, funcion)}\n")
pausa()
print("*"*50)
####################################################################################################

limpiar()
print ("DataFrame:\n",df)

print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                Exportamos                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                            df.to_csv("filename")                            ║
║                            df.to_json("filename")                           ║
║                            df.to_excel("filename")                          ║
║                            df.to_sql(table_name, connection_object)         ║
║                            df.to_pickle('filename')                         ║
║                                                                             ║
║                      ver archivo pandas_import-export                       ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
df = df.reset_index()
df.to_csv   ('IO_pandas.csv',header=True, index=False)
print ("Archivo IO_pandas.csv  - Grabado ")
df.to_json  ('IO_pandas.json')
print ("Archivo IO_pandas.json - Grabado ")
df.to_excel ('IO_pandas.xlsx', sheet_name='HOJA_I')
print ("Archivo IO_pandas.xlsx - Grabado ")
df.to_pickle ('IO_pandas.pkl')
print ("Archivo IO_pandas.pkl - Grabado ")
# ~ df.to_sql   ('IO_pandas', connection_object)
# ~ print ("base de datos - Grabado ")
####################################################################################################

pausa();
limpiar()
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                Importamos                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                            pd.read_csv("filename")                          ║
║                            pd.read_json(json_string)                        ║
║                            pd.read_excel("filename")                        ║
║                            pd.read_pickle("filename")                       ║
║                            pd.read_table("filename")                        ║
║                            pd.read_sql(query, connection_object)            ║
║                                                                             ║
║                      ver archivo pandas_import-export                       ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
desdeCSV   = pd.read_csv  ('IO_pandas.csv')
desdeJson  = pd.read_json ('IO_pandas.json')
desdeExcel = pd.read_excel("IO_pandas.xlsx")
desdePickle= pd.read_pickle("IO_pandas.pkl")
# ~ desdeSQL   = pd.read_sql_query("SELECT * FROM purchases", connection_object)
print("desdeCSV:\n",desdeCSV)
print("desdeJson:\n",desdeJson)
print("desdeExcel:\n",desdeExcel)
print("desdePickle:\n",desdePickle)
pausa();
####################################################################################################

df = pd.DataFrame([
                    [7, 9,  8,'H'],
                    [7.25  , 7,  np.nan,'F'],
                    [9  , 9,   8,'H'],
                    [6,  np.nan, 8,'H'],
                    [7, 4, 10,'F'],
                    [7.25  , 7,  np.nan,'F'],
                    [9  ,  np.nan,   8,'H'],
                    [10, '7', '8','F'],
                    [6,  np.nan, 8,'H'],
                    [7, 4, 10,'F'],
                    [ np.nan,  np.nan,  np.nan, np.nan],
                    [9  ,  np.nan,   8,'H'],
                    [10, '7', '8','F'],
                    [6, 6.99, 8,'H'],
                    [7, 4, 10,'F'],
                    [7.25  , 7, 8.5,'F'],
                    [9  ,  np.nan,   8,'H'],
                    [10, '7', '8','F'],
                    [6,  np.nan, 8,'H'],
                    [7, 4, 10, np.nan]],
                    columns=['trim_1', 'trim_2', 'trim_3', 'sexo']
                    )
df['index']=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
df.set_index("index",inplace=True)
df.plot(kind='line', y='trim_1' , color = 'blue') 
plt.show()

df.dropna().plot(kind='line', y='trim_1' , color = 'blue') 
plt.show()


####################################################################################################
                
print("-"*50)
print("agrego una columna nueva")
df['Nombre']=['Ariel','Ana','Daniel','Paula','Jose','Juan','Gabriel','Lucia','Maria','Pamela','Pablo','Jose','Juan','Gabriel','Lucia','Maria','Pamela','Pablo','Ariel','Ana']
original=df.copy()
df=df[['trim_1','trim_2','trim_3']].fillna(0)
print("no se puede hacer el cambio a to_number/int/float si hay NaN")
df=df[['trim_1', 'trim_2', 'trim_3']].astype(int)
print ("df.original:\n",df,'\ndtypes\n',df.dtypes)

####################################################################################################

# ~ pausa()

# ~ df=original.copy()

# ~ print ("df.original:\n",df,'\ndtypes\n',df.dtypes)
# ~ df['trim_1']= df['trim_1'].fillna(value=df['trim_1'].mean())

# ~ print ("df.original:\n",df,'\ndtypes\n',df.dtypes)
# ~ df['trim_2']= df['trim_2'].fillna(value=df['trim_2'].mean())
# ~ print ("df.original:\n",df,'\ndtypes\n',df.dtypes)


# ~ df['trim_3']= df['trim_3'].fillna(value=df['trim_3'].mean())

# ~ print ("df.fillna..mean:\n",df,'\ndtypes\n',df.dtypes)
