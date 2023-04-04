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

print('''
    El método .groupby() de Pandas permite obtener mediante el uso de división, 
        aplicación y combinación un sinfin de la combinación, transformación y generación de datos derivados. 
    Este proceso maneja de manera eficiente grandes conjuntos de datos para manipular datos 
        de formas increíblemente poderosas siendo el motivo por lo cual es una piedra angular para 
        manipular y analizar datos. 
    Aprenderá a dominar el método de principio a fin, incluido el acceso a grupos, 

            Dividir los datos en grupos según algunos criterios
            Aplicar una función a cada grupo de forma independiente
                    --------------------------------------------------------------
                    |  Algunos de los casi 70  método agregación SeriesGroupBy   |
                    ---------------------+----------------------------------------    
                    |        Nombre      |     Descripción del  Método           |
                    ---------------------+----------------------------------------
                            .count()     |	   Cantidad de registros no nulos.
                            .sum()	     |     La suma de los valores.
                            .mean()	     |     El promedio / media aritmética de los valores.
                            .median()    |     La mediana de los valores
                            .min()	     |     El valor mínimo del grupo.
                            .max()	     |     El valor máximo del grupo.
                            .std()	     |     La desviación estándar del grupo.
                            .var()	     |     La varianza del grupo.

                ['agg', 'aggregate', 'all', 'any', 'apply', 'backfill', 'bfill', 'boxplot', 
                'corr', 'corrwith', 'count', 'cov', 'cumcount', 'cummax', 'cummin', 'cumprod', 
                'cumsum', 'describe', 'diff', 'dtypes', 'ewm', 'expanding', 'ffill', 'fillna', 
                'filter', 'first', 'get_group', 'groups', 'head', 'hist', 'idxmax', 'idxmin', 
                'indices', 'last', 'mad', 'max', 'mean', 'median', 'min', 'ndim', 'ngroup', 
                'ngroups', 'nth', 'nunique', 'ohlc', 'pad', 'pct_change', 'pipe', 'plot', 
                'prod', 'quantile', 'rank', 'resample', 'rolling', 'sample', 'sem', 'shift', 
                'size', 'skew', 'std', 'sum', 'tail', 'take', 'transform', 'tshift', 'value_counts', 'var']

            Combinar los resultados en una estructura de datos apropiada


    El método Pandas .groupby() funciona de manera muy similar a la instrucción SQL GROUP BY. 
    De hecho, está diseñado para reflejar su contraparte de SQL y aprovechar sus eficiencias e intuición. 
    De manera similar a la GROUP BYdeclaración SQL,
        el método Pandas funciona dividiendo nuestros datos, agregándolos de una manera determinada (o formas) 
        y recombinando los datos de manera significativa.
    La razón para aplicar este método es dividir un problema de análisis de big data en partes manejables.
    Esto le permite realizar operaciones en las partes individuales y volver a armarlas. 
    Si bien los pasos de aplicar y combinar ocurren por separado, Pandas lo abstrae y lo hace parecer 
        como si fuera un solo paso.


    Debido a que el método .groupby() funciona dividiendo primero los datos, en realidad podemos 
    trabajar con los grupos directamente. 
    Del mismo modo, debido a que cualquier agregación se realiza después de la división, tenemos pleno dominio sobre cómo agregamos los datos. 
    Luego, Pandas maneja cómo se combinan los datos para presentar un DataFrame significativo.

    Lo bueno de esto es que nos permite usar el método en una variedad de formas, especialmente de forma creativa. 
    Debido a esto, el método es una piedra angular para comprender cómo se pueden usar Pandas para manipular y analizar datos. 
    ¡La longitud de este tutorial refleja esa complejidad e importancia!
    Pandas parece ofrecer una gran variedad de opciones para ayudarlo a analizar y agregar nuestros datos.
    Los métodos .pivot(), .pivot_table(), .groupby() proporciona el conjunto de herramientas 
        sobre cómo se agregan los datos. 
    No son simplemente reempaquetados, sino que representan formas útiles de realizar diferentes tareas.
    Cargando un DataFrame de Pandas de Muestra. 

                    --------------------------------------------------------------
                    |  agg. sumamos método agregación SeriesGroupBy              |
                    ---------------------+----------------------------------------        
    nota:
        El método 'agg()' es un alias del método 'aggregate()'.
        Se estila usar los alias.               


    Pandas también viene con un método adicional .agg(), que nos permite aplicar múltiples agregaciones en el método groupby(). 
    El método nos permite pasar una lista de invocables / métodos pandas (la parte de la función sin los paréntesis). 
        .agg(['size','count','sum','mean','median','min','max','std','var'])
    o métodos de la biblioteca numpy para agregar nuestros datos.
        .agg([np.size,np.count_nonzero,np.sum,np.mean,np.median,np.min,np.max,np.std,np.var])

                    --------------------------------------------------------------
                    |  transform. sumamos método de agregación incluso propios   |
                    ---------------------+---------------------------------------- 

    Transform permite amplias la cantidad de metodos de agregacion a los que puedas generar en una función/metodo incluso propios . 
''')



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# ~ df_titanic = pd.read_csv('titanic.csv')
# ~ df_titanic3 = pd.read_excel("titanic3.xls")#, index_col=None)
def ya_hechos():
    pass
#######################################################################################################
    limpiar()
def ARG_csv():
    print ("*"*104)
    print ("*","1)  Lee el archivos csv y genera un DataFrame".center(100),"*")
    print ("*"*104)



    # ~ df = pd.DataFrame(data=datos)
    # ~ df = pd.read_csv('https://raw.githubusercontent.com/datagy/data/main/Población.csv', parse_dates=['date'])
    df = pd.read_csv('Arg.csv')
    print (f"{df.head (25)}")

    print (f"{df.groupby('región')=}")
    #Es un objeto de tipo DataFrameGroupBy.
    # ~ print (f"{dir(df.groupby('región'))=}")
    # ~ Código	Provincia	región	Área km 2	Área prop.	Área % país	Población	Poblacion.prop.	Poblacion % país	Densidad	Dens.prop.

    limpiar()
    def ya_hechos():
        pass
    #------------------------------------------------------------------------------------------------------
    print ("*"*100)
    print (f"""df.groupby('columna').ngroups
    Devuelve la cantidad de elementos distintos en la columna 'región'.""")
    print (f"df.groupby('región').ngroups={df.groupby('región').ngroups}")
    # ~ print (f"df.groupby('gender').ngroups={df.groupby('gender').ngroups}")
    pausa()
    #------------------------------------------------------------------------------------------------------
    print ("*"*100)
    print (f"""df.groupby('columna').groups
    Devuelve los distintos componentes de la columna en forma de claves diccionarios 
    y los valores del diccionario son formados por una lista los index del df donde se encuentra cada clave.""")
    print (f"df.groupby('región').groups=\n{df.groupby('región').groups}")
    # ~ print (f"df.groupby('gender').groups=\n{df.groupby('gender').groups}")
    pausa()
    #------------------------------------------------------------------------------------------------------
    print ("*"*100)
    print (f"""df.groupby('columna').groups.keys()
    Devuelve la lista de los distintos componentes de la columna en forma de claves diccionarios.""")
    print (f"df.groupby('región').groups.keys()={df.groupby('región').groups.keys()}")
    # ~ print (f"df.groupby('gender').groups.keys()={df.groupby('gender').groups.keys()}")
    pausa()
    #------------------------------------------------------------------------------------------------------
    print ("*"*100)
    print (f"""df.groupby('columna').get_group('elemento de la columna')
    Devuelve un sub-DataFrame donde en la columna indicada tenga el elemento requerido.""")
    print (f"df.groupby('región').get_group('South')=\n{df.groupby('región').get_group('pampeana')}")
    # ~ print (f"df.groupby('gender').get_group('Male')=\n{df.groupby('gender').get_group('Male')}")
    pausa()
    #------------------------------------------------------------------------------------------------------
    print ("*"*100)
    print (f"""df.groupby('columna').count()
    Devuelve una matriz con los distintos elementos de la columna 
    la cantidad de las repeticiones de estos en cada columna del df.""")
    print (f"df.groupby('región').count()=\n{df.groupby('región').count()}")
    # ~ print (f"df.groupby('gender').count()=\n{df.groupby('gender').count()}")
    pausa()
    #------------------------------------------------------------------------------------------------------
    print ("*"*100)
    print (f"""
    Dividir los datos: Comencemos por dividir los datos: podemos recorrer cada valor único en el DataFrame, dividiendo los datos por 'región'columna.
    """)

    # Replicating split-apply-combine Without GroupBy

    # Create a Container Dictionary
    averages = {}

    # genero un bucle donde paso cada valor unico dde la columna región
    for región in df['región'].unique():
    #------------------------------------------------------------------------------------------------------
        # Generamos un DafaFrame temporal con solo los registros de cada región
        tempdf = df[df['región'] == región]
        # Aplicamos la agregación del DataFrame temporal de cada región con el valor del promedio la columna 'Población' 
        average = tempdf['Población'].mean()
        # Combinames los datos de la región y el promedio de ventas en un diccionario
        averages[región] = [average]
    #------------------------------------------------------------------------------------------------------
        # todo en una
        averages[región] = [df[df['región'] == región]['Población'].mean()]
    #------------------------------------------------------------------------------------------------------
        print(f"averages={averages}")

    aggregate_df = pd.DataFrame.from_dict(averages, orient='index', columns=['Average Sales'])
    print(f"aggregate_df={aggregate_df}")
    #------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------
    print (f"""
    obtenemos el mismo resultado sin bucle ni df temporal ni mas q una linea.""")
    aggregate_df = df.groupby('región')['Población'].mean()
    print(f"{aggregate_df=}")
    '''
    df.groupby('región')
                Divide los datos en diferentes grupos, según la regióncolumna .
    ['Población']   
                selecciona solo esa columna de las agrupaciones
    .mean() 
                aplica el método mean (promedio) a la columna de cada grupo
                
            --------------------------------------------------------------
            |  Algunos de los casi 70  método agregación SeriesGroupBy   |
            ---------------------+----------------------------------------    
            |        Nombre      |     Descripción del  Método           |
            ---------------------+----------------------------------------
                    .count()     |	   Cantidad de registros no nulos.
                    .sum()	     |     La suma de los valores.
                    .mean()	     |     El promedio / media aritmética de los valores.
                    .median()    |     La mediana de los valores
                    .min()	     |     El valor mínimo del grupo.
                    .max()	     |     El valor máximo del grupo.
                    .std()	     |     La desviación estándar del grupo.
                    .var()	     |     La varianza del grupo.
                    
    https://economipedia.com/definiciones           
    *   La varianza es una medida de dispersión que representa la variabilidad de una serie de datos respecto a su media. 
            Formalmente se calcula como la suma de los residuos al cuadrado divididos entre el total de observaciones.      
    *   La desviación estándar o típica es una medida que ofrece información sobre la dispersión media de una variable. 
            La desviación estándar es siempre mayor o igual que cero.
    Desviación: La desviación es la separación que existe entre un valor cualquiera de la serie y la media.

    *   La desviación cuartil (DQ) es una medida estadística de dispersión que devuelve el valor central del 
            rango intercuartílco y se utiliza en conjuntos de datos sesgados. 
        En otras palabras, la desviación cuartil es calcular la mediana del rango intercuartílico (RIC) 
            y se emplea en conjuntos de datos con bastantes valores extremos.

    *   El rango intercuartílico es un medida de dispersión de un conjunto de datos generalmente utilizado en el 
            diagrama de caja. 
        En otras palabras, el rango intercuartílico es la diferencia entre el penúltimo y el primer cuartil de 
            una distribución utilizado en el diagrama de caja.
                    
                    
    ['agg', 'aggregate', 'all', 'any', 'apply', 'backfill', 'bfill', 'boxplot', 
    'corr', 'corrwith', 'count', 'cov', 'cumcount', 'cummax', 'cummin', 'cumprod', 
    'cumsum', 'describe', 'diff', 'dtypes', 'ewm', 'expanding', 'ffill', 'fillna', 
    'filter', 'first', 'get_group', 'groups', 'head', 'hist', 'idxmax', 'idxmin', 
    'indices', 'last', 'mad', 'max', 'mean', 'median', 'min', 'ndim', 'ngroup', 
    'ngroups', 'nth', 'nunique', 'ohlc', 'pad', 'pct_change', 'pipe', 'plot', 
    'prod', 'quantile', 'rank', 'resample', 'rolling', 'sample', 'sem', 'shift', 
    'size', 'skew', 'std', 'sum', 'tail', 'take', 'transform', 'tshift', 'value_counts', 'var']
    '''
    # ~ print(dir(df.groupby('región')))
    salida = df.groupby('región')['Población'].count()
    print("Cantidad de registros no nulos.")
    print(f"df.groupby('región')['Población'].count()=\n{salida}")
    print ("-"*25)
    salida = df.groupby('región')['Población'].sum()
    print("La suma de los valores.")
    print(f"df.groupby('región')['Población'].sum()=\n{salida}")
    print ("-"*25)
    salida = df.groupby('región')['Población'].mean()
    print("El promedio / media aritmética de los valores.")
    print(f"df.groupby('región')['Población'].mean()=\n{salida}")
    print ("-"*25)
    salida = df.groupby('región')['Población'].median()
    print("La mediana de los valores.")
    print(f"df.groupby('región')['Población'].median()=\n{salida}")
    print ("-"*25)
    salida = df.groupby('región')['Población'].min()
    print("El valor mínimo del grupo.")
    print(f"df.groupby('región')['Población'].min()=\n{salida}")
    print ("-"*25)
    salida = df.groupby('región')['Población'].max()
    print("El valor máximo del grupo.")
    print(f"df.groupby('región')['Población'].max()=\n{salida}")
    print ("-"*25)
    salida = df.groupby('región')['Población'].std()
    print("La desviación estándar del grupo.")
    print(f"df.groupby('región')['Población'].std()=\n{salida}")
    print ("-"*25)
    salida = df.groupby('región')['Población'].var()
    print("La varianza del grupo.")
    print(f"df.groupby('región')['Población'].var()=\n{salida}")
    pausa()
    limpiar()
    #------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------
    print('''
                        --------------------------------------------------------------
                        |  agg. sumamos método agregación SeriesGroupBy              |
                        ---------------------+---------------------------------------- 
    Pandas también viene con un método adicional .agg(), que nos permite aplicar múltiples agregaciones en el método groupby(). 
    El método nos permite pasar una lista de invocables / métodos pandas (la parte de la función sin los paréntesis). 
        .agg(['size','count','sum','mean','median','min','max','std','var'])
    o métodos de la biblioteca numpy para agregar nuestros datos.
        .agg([np.size,np.count_nonzero,np.sum,np.mean,np.median,np.min,np.max,np.std,np.var])

        ver np.char.count
    ''')

    salida = df.groupby('región')['Población'].agg(['size','count','sum','mean','median','min','max','std','var'])
    print(f"df.groupby('región')['Población'].agg([...])=\n{salida}")

    salida = df.groupby('región')['Población'].agg([np.size,np.count_nonzero,np.sum,np.mean,np.median,np.min,np.max,np.std,np.var])
    print(f"df.groupby('región')['Población'].agg([np....])=\n{salida}")


    # ~ [np.mean, np.std, np.var]
    #------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------
    print('''
                        --------------------------------------------------------------
                        |  transform. sumamos método de agregación incluso propios   |
                        ---------------------+---------------------------------------- 

    Transform permite amplias la cantidad de metodos de agregacion a los que puedas generar en una función/metodo incluso propios . 
    En este ejemplo, calcularemos el porcentaje de las ventas totales de cada región que representa cada venta. 
    Para hacer esto, podemos aplicar el método .transform() al objeto GroupBy. 
    Podemos pasar el metodo invocable 'sum'  para devolver la suma de todo el grupo en cada fila. 
    Finalmente, dividimos la columna 'Población' original por esa suma.
    ''')
    def agregacion_propio():
        df['Percent Of Region Sales'] = df['Población'] / df.groupby('región')['Población'].transform('sum')

    df['Percent Of Region Sales'] = df['Población'] / df.groupby('región')['Población'].transform('sum')
    print(f"'Percent Of Region Sales'=\n{df}")
    print(f"{df['Población']=}")
    print(f"{df.groupby('región')['Población']=}")
    print(f"{df.groupby('región')['Población'].transform('sum')=}")


    exit()
def sales_csv():
        # ~ df = pd.read_csv('https://raw.githubusercontent.com/datagy/data/main/Población.csv', parse_dates=['date'])
    df = pd.read_csv('sales.csv')
    print (f"{df.head (25)}")

    print (f"{df.groupby('region')=}")
    #Es un objeto de tipo DataFrameGroupBy.
    # ~ print (f"{dir(df.groupby('región'))=}")
    # ~ Código	Provincia	región	Área km 2	Área prop.	Área % país	Población	Poblacion.prop.	Poblacion % país	Densidad	Dens.prop.

    limpiar()
    def ya_hechos():
        pass
    
#------------------------------------------------------------------------------------------------------
    print ("*"*100)
    print (f"""df.groupby('columna').ngroups
    Devuelve la cantidad de elementos distintos en la columna 'region'.""")
    print (f"df.groupby('region').ngroups={df.groupby('region').ngroups}")
    print (f"df.groupby('gender').ngroups={df.groupby('gender').ngroups}")
    pausa()
    #------------------------------------------------------------------------------------------------------
    print ("*"*100)
    print (f"""df.groupby('columna').groups
    Devuelve los distintos componentes de la columna en forma de claves diccionarios 
    y los valores del diccionario son formados por una lista los index del df donde se encuentra cada clave.""")
    print (f"df.groupby('region').groups=\n{df.groupby('region').groups}")
    print (f"df.groupby('gender').groups=\n{df.groupby('gender').groups}")
    pausa()
    #------------------------------------------------------------------------------------------------------
    print ("*"*100)
    print (f"""df.groupby('columna').groups.keys()
    Devuelve la lista de los distintos componentes de la columna en forma de claves diccionarios.""")
    print (f"df.groupby('region').groups.keys()={df.groupby('region').groups.keys()}")
    print (f"df.groupby('gender').groups.keys()={df.groupby('gender').groups.keys()}")
    pausa()
    #------------------------------------------------------------------------------------------------------
    print ("*"*100)
    print (f"""df.groupby('columna').get_group('elemento de la columna')
    Devuelve un sub-DataFrame donde en la columna indicada tenga el elemento requerido.""")
    print (f"df.groupby('region').get_group('South')=\n{df.groupby('region').get_group('South')}")
    print (f"df.groupby('gender').get_group('Male')=\n{df.groupby('gender').get_group('Male')}")
    pausa()
    #------------------------------------------------------------------------------------------------------
    print ("*"*100)
    print (f"""df.groupby('columna').count()
    Devuelve una matriz con los distintos elementos de la columna 
    la cantidad de las repeticiones de estos en cada columna del df.""")
    print (f"df.groupby('region').count()=\n{df.groupby('region').count()}")
    print (f"df.groupby('gender').count()=\n{df.groupby('gender').count()}")
    pausa()
    #------------------------------------------------------------------------------------------------------
    print ("*"*100)
    print (f"""
    Dividir los datos: Comencemos por dividir los datos: podemos recorrer cada valor único en el DataFrame, dividiendo los datos por 'region'columna.
    """)

    # Replicating split-apply-combine Without GroupBy

    # Create a Container Dictionary
    averages = {}

    # genero un bucle donde paso cada valor unico dde la columna región
    for region in df['region'].unique():
    #------------------------------------------------------------------------------------------------------
        # Generamos un DafaFrame temporal con solo los registros de cada región
        tempdf = df[df['region'] == region]
        # Aplicamos la agregación del DataFrame temporal de cada region con el valor del promedio la columna 'sales' 
        average = tempdf['sales'].mean()
        # Combinames los datos de la region y el promedio de ventas en un diccionario
        averages[region] = [average]
    #------------------------------------------------------------------------------------------------------
        # todo en una
        averages[region] = [df[df['region'] == region]['sales'].mean()]
    #------------------------------------------------------------------------------------------------------
        print(f"averages={averages}")

    aggregate_df = pd.DataFrame.from_dict(averages, orient='index', columns=['Average Sales'])
    print(f"aggregate_df={aggregate_df}")
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
    print (f"""
    obtenemos el mismo resultado sin bucle ni df temporal ni mas q una linea.""")
    aggregate_df = df.groupby('region')['sales'].mean()
    print(f"{aggregate_df=}")
    '''
    df.groupby('region')
                Divide los datos en diferentes grupos, según la regioncolumna .
    ['sales']   
                selecciona solo esa columna de las agrupaciones
    .mean() 
                aplica el método mean (promedio) a la columna de cada grupo
                
            --------------------------------------------------------------
            |  Algunos de los casi 70  método agregación SeriesGroupBy   |
            ---------------------+----------------------------------------    
            |        Nombre      |     Descripción del  Método           |
            ---------------------+----------------------------------------
                    .count()     |	   Cantidad de registros no nulos.
                    .sum()	     |     La suma de los valores.
                    .mean()	     |     El promedio / media aritmética de los valores.
                    .median()    |     La mediana de los valores
                    .min()	     |     El valor mínimo del grupo.
                    .max()	     |     El valor máximo del grupo.
                    .std()	     |     La desviación estándar del grupo.
                    .var()	     |     La varianza del grupo.
                    
    https://economipedia.com/definiciones           
    *   La varianza es una medida de dispersión que representa la variabilidad de una serie de datos respecto a su media. 
            Formalmente se calcula como la suma de los residuos al cuadrado divididos entre el total de observaciones.      
    *   La desviación estándar o típica es una medida que ofrece información sobre la dispersión media de una variable. 
            La desviación estándar es siempre mayor o igual que cero.
    Desviación: La desviación es la separación que existe entre un valor cualquiera de la serie y la media.

    *   La desviación cuartil (DQ) es una medida estadística de dispersión que devuelve el valor central del 
            rango intercuartílco y se utiliza en conjuntos de datos sesgados. 
        En otras palabras, la desviación cuartil es calcular la mediana del rango intercuartílico (RIC) 
            y se emplea en conjuntos de datos con bastantes valores extremos.

    *   El rango intercuartílico es un medida de dispersión de un conjunto de datos generalmente utilizado en el 
            diagrama de caja. 
        En otras palabras, el rango intercuartílico es la diferencia entre el penúltimo y el primer cuartil de 
            una distribución utilizado en el diagrama de caja.
                    
                    
    ['agg', 'aggregate', 'all', 'any', 'apply', 'backfill', 'bfill', 'boxplot', 
    'corr', 'corrwith', 'count', 'cov', 'cumcount', 'cummax', 'cummin', 'cumprod', 
    'cumsum', 'describe', 'diff', 'dtypes', 'ewm', 'expanding', 'ffill', 'fillna', 
    'filter', 'first', 'get_group', 'groups', 'head', 'hist', 'idxmax', 'idxmin', 
    'indices', 'last', 'mad', 'max', 'mean', 'median', 'min', 'ndim', 'ngroup', 
    'ngroups', 'nth', 'nunique', 'ohlc', 'pad', 'pct_change', 'pipe', 'plot', 
    'prod', 'quantile', 'rank', 'resample', 'rolling', 'sample', 'sem', 'shift', 
    'size', 'skew', 'std', 'sum', 'tail', 'take', 'transform', 'tshift', 'value_counts', 'var']
    '''
    # ~ print(dir(df.groupby('region')))
    salida = df.groupby('region')['sales'].count()
    print("Cantidad de registros no nulos.")
    print(f"df.groupby('region')['sales'].count()=\n{salida}")
    print ("-"*25)
    salida = df.groupby('region')['sales'].sum()
    print("La suma de los valores.")
    print(f"df.groupby('region')['sales'].sum()=\n{salida}")
    print ("-"*25)
    salida = df.groupby('region')['sales'].mean()
    print("El promedio / media aritmética de los valores.")
    print(f"df.groupby('region')['sales'].mean()=\n{salida}")
    print ("-"*25)
    salida = df.groupby('region')['sales'].median()
    print("La mediana de los valores.")
    print(f"df.groupby('region')['sales'].median()=\n{salida}")
    print ("-"*25)
    salida = df.groupby('region')['sales'].min()
    print("El valor mínimo del grupo.")
    print(f"df.groupby('region')['sales'].min()=\n{salida}")
    print ("-"*25)
    salida = df.groupby('region')['sales'].max()
    print("El valor máximo del grupo.")
    print(f"df.groupby('region')['sales'].max()=\n{salida}")
    print ("-"*25)
    salida = df.groupby('region')['sales'].std()
    print("La desviación estándar del grupo.")
    print(f"df.groupby('region')['sales'].std()=\n{salida}")
    print ("-"*25)
    salida = df.groupby('region')['sales'].var()
    print("La varianza del grupo.")
    print(f"df.groupby('region')['sales'].var()=\n{salida}")
    

    
    
    
    
    pausa()
    limpiar()
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
    print('''
                        --------------------------------------------------------------
                        |  agg. sumamos método agregación SeriesGroupBy              |
                        ---------------------+---------------------------------------- 
                        
    nota:
        El método 'agg()' es un alias del método 'aggregate()'.
        Se estila usar los alias.                
                        
    Pandas también viene con un método adicional .agg(), que nos permite aplicar múltiples agregaciones en el método groupby(). 
    El método nos permite pasar una lista de invocables / métodos pandas (la parte de la función sin los paréntesis). 
        .agg(['size','count','sum','mean','median','min','max','std','var'])
    o métodos de la biblioteca numpy para agregar nuestros datos.
        .agg([np.size,np.count_nonzero,np.sum,np.mean,np.median,np.min,np.max,np.std,np.var])

        ver np.char.count
    ''')

    salida = df.groupby('region')['sales'].agg(['size','count','sum','mean','median','min','max','std','var',list])
    print(f"df.groupby('region')['sales'].agg([...])=\n{salida}")

    salida = df.groupby('region')['sales'].agg([np.size,np.count_nonzero,np.sum,np.mean,np.median,np.min,np.max,np.std,np.var])
    print(f"df.groupby('region')['sales'].agg([np....])=\n{salida}")

    salida = df.groupby('region')['sales'].agg(['size',list,dict])
    print(f"df.groupby('region')['sales'].agg([...])=\n{salida}")
    # ~ [np.mean, np.std, np.var]
    #------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------
    print('''
                        --------------------------------------------------------------
                        |  transform. sumamos método de agregación incluso propios   |
                        ---------------------+---------------------------------------- 

    Transform permite amplias la cantidad de metodos de agregacion a los que puedas generar en una función/metodo incluso propios . 
    En este ejemplo, calcularemos el porcentaje de las ventas totales de cada región que representa cada venta. 
    Para hacer esto, podemos aplicar el método .transform() al objeto GroupBy. 
    Podemos pasar el metodo invocable 'sum'  para devolver la suma de todo el grupo en cada fila. 
    Finalmente, dividimos la columna 'sales' original por esa suma.
    ''')
    def agregacion_propio():
        df['Percent Of Region Sales'] = df['sales'] / df.groupby('region')['sales'].transform('sum')

    df['Percent Of Region Sales'] = df['sales'] / df.groupby('region')['sales'].transform('sum')
    print(f"'Percent Of Region Sales'=\n{df}")
    print(f"{df['sales']=}")
    print(f"{df.groupby('region')['sales']=}")
    print(f"{df.groupby('region')['sales'].transform('sum')=}")
    # ~ custom_sum = df.agg('custom_sum', lambda sales: sales.sum(), lambda s0: s0.sum())
    # ~ print(f"{df.groupby('sales').agg(custom_sum)}")




