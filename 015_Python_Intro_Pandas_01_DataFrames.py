

from __init__ import *


import os

def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')

def pausa():
    input("\tPresione una tecla para continuar")

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
╠═════════════════════════════════════════════════════════════════════════════╣
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
#import seaborn as sns
import datetime
import math
limpiar()
def ya_hechos():
    pass
    
    
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                            Pandas DataFrame                                 ║
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║                            Attributes  (17)                                 ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL} 

    at                                                     Acceda a un solo valor para un par de etiquetas de fila/columna.
    attrs                                                  Diccionario de atributos globales de este conjunto de datos.
    axes                                                   Devuelve una lista que representa los ejes del DataFrame.
    columns                                                Las etiquetas de columna del DataFrame.
    dtypes                                                 Devuelve los dtypes en el DataFrame.
    empty                                                  Indicador de si Series/DataFrame está vacío.
    flags                                                  Obtenga las propiedades asociadas con este objeto pandas.
    iat                                                    Acceda a un valor único para un par de filas/columnas por posición de número entero.
    iloc                                                   Indexación puramente basada en la ubicación de enteros para la selección por posición.
    index                                                  El índice (etiquetas de fila) del DataFrame.
    loc                                                    Acceda a un grupo de filas y columnas por etiqueta(s) o una matriz booleana.
    ndim                                                   Devuelve un int que representa el número de ejes/dimensiones de la matriz.
    shape                                                  Devuelve una tupla que representa la dimensionalidad del DataFrame.
    size                                                   Devuelve un int que representa el número de elementos en este objeto.
    style                                                  Devuelve un objeto Styler.
    values                                                 Devuelve una representación Numpy del DataFrame.
    T                                                      Devuelve el DF Transpuesto (filas x columnas y columnas x filas) .
    
    
    
    inplace : Especificar True permite que Pandas reemplacen el índice en el DataFrame original en lugar de crear una copia del DataFrame.
    ''')
    pausa()
    limpiar()
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                            Pandas DataFrame                                 ║
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║                             Methods (191)                                   ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL} 

    abs()                                                   Devuelve una serie/marco de datos con el valor numérico absoluto de cada elemento.
    add(otro[, eje, nivel, valor_relleno])                  Obtener Adición de marco de datos y otros, por elementos (operador binario agregar ).
    add_prefix(prefijo)                                     Etiquetas de prefijo con prefijo de cadena .
    add_suffix(sufijo)                                      Etiquetas de sufijo con sufijo de cadena
    agg([función, eje])                                     Agregue usando una o más operaciones sobre el eje especificado.
    aggregate([función, eje])                               Agregue usando una o más operaciones sobre el eje especificado.
    align(otro[, unión, eje, nivel, copia, ...])            Alinee dos objetos en sus ejes con el método de unión especificado.
    all([eje, bool_only, skipna, nivel])                    Devuelve si todos los elementos son verdaderos, potencialmente sobre un eje.
    any(*[, eje, bool_only, skipna, nivel])                 Devuelve si algún elemento es Verdadero, potencialmente sobre un eje.
    apply(func[, eje, raw, tipo_resultado, argumentos])     Aplicar una función a lo largo de un eje del DataFrame.
    applymap(func[, na_action])                             Aplique una función a un marco de datos por elementos.
    asfreq(frecuencia[, método, cómo, normalizar, ...])     Convierte series de tiempo a la frecuencia especificada.
    asof(donde[, subconjunto])                              Devuelve la(s) última(s) fila(s) sin NaN antes de where .
    assign(**kwargs)                                        Asigne nuevas columnas a un DataFrame.
    astype(dtype[, copiar, errores])                        Transmita un objeto pandas a un tipo de d especificado dtype.
    at_time(tiempo[, a partir de, eje])                     Seleccione valores a una hora determinada del día (p. ej., 9:30 a. m.).
    backfill(*[, eje, en el lugar, límite, abatido])        Sinónimo de DataFrame.fillna()con method='bfill'.
    between_time(hora_inicio, hora_fin[, ...])              Seleccione valores entre momentos particulares del día (p. ej., 9:00-9:30 a. m.).
    bfill(*[, eje, en el lugar, límite, abatido])           Sinónimo de DataFrame.fillna()con method='bfill'.
    bool()                                                  Devuelve el valor booleano de un solo elemento Series o DataFrame.
    boxplot([columna, x, hacha, tamañofuente, rot, ...])    Haz un diagrama de caja a partir de las columnas de DataFrame.
    clip([inferior, superior, eje, en su lugar])            Ajuste los valores en los umbrales de entrada.
    combine(otro, func[, fill_value, overwrite])            Realice una combinación por columnas con otro DataFrame.
    combine_first(otro)                                     Actualice elementos nulos con valor en la misma ubicación en otro archivo .
    compare(otro[, alinear_eje, mantener_forma, ...])       Compare con otro DataFrame y muestre las diferencias.
    convert_dtypes([objetos_inferidos, ...])                Convierta columnas a los mejores dtypes posibles usando dtypes compatibles con pd.NA.
    copy([profundo])                                        Haga una copia de los índices y datos de este objeto.
    corr([método, min_periods, numeric_only])               Calcule la correlación por pares de columnas, excluyendo NA/valores nulos.
    corrwith(otro[, eje, gota, método, ...])                Calcule la correlación por pares.
    count([eje, nivel, solo_numérico])                      Cuente las celdas que no sean NA para cada columna o fila.
    cov([min_periods, dof, numeric_only])                   Calcule la covarianza por pares de las columnas, excluyendo NA/valores nulos.
    cummax([eje, skipna])                                   Devuelve el máximo acumulativo sobre un eje DataFrame o Series.
    cummin([eje, skipna])                                   Devuelve el mínimo acumulativo sobre un eje DataFrame o Series.
    cumprod([eje, skipna])                                  Devuelve el producto acumulativo sobre un eje DataFrame o Series.
    cumsum([eje, skipna])                                   Devuelve la suma acumulada sobre un eje DataFrame o Series.
    describe([percentiles, incluir, excluir, ...])          Genera estadísticas descriptivas.
    diff([puntos, eje])                                     Primera diferencia discreta de elemento.
    div(otro[, eje, nivel, valor_relleno])                  Obtenga la división flotante del marco de datos y otros elementos (operador binario truediv ).
    divide(otro[, eje, nivel, valor_relleno])               Obtenga la división flotante del marco de datos y otros elementos (operador binario truediv ).
    dot(otro)                                               Calcule la multiplicación de matriz entre DataFrame y otro.
    drop([etiquetas, eje, índice, columnas, nivel, ...])    Suelta etiquetas específicas de filas o columnas.
    drop_duplicates([subconj, mantener,en su lugar,...])    Devuelve DataFrame con filas duplicadas eliminadas.
    droplevel(nivel[, eje])                                 Devolver serie/marco de datos con el índice o los niveles de columna solicitados eliminados.
    dropna(*[, eje, cómo, umbral, subconj, en el lugar])    Eliminar valores faltantes.
    duplicated([subconjunto, mantener])                     Devuelve una serie booleana que denota filas duplicadas.
    eq(otro[, eje, nivel])                                  Obtener igual a la trama de datos y otros elementos (operador binario eq ).
    equals(otro)                                            Prueba si dos objetos contienen los mismos elementos.
    eval(expr, *[, en el lugar])                            Evalúe una cadena que describa operaciones en columnas de DataFrame.
    ewm([com, intervalo, vida media, alfa, ...])            Proporcione cálculos ponderados exponencialmente (EW).
    expanding([min_periods, centro, eje, método])           Proporcionar cálculos de ventana en expansión.
    explode(columna[, ignore_index])                        Transforme cada elemento de una lista en una fila, replicando valores de índice.
    ffill(*[, eje, en el lugar, límite, abatido])           Sinónimo de DataFrame.fillna()con method='ffill'.
    fillna([valor, método, eje, en el lugar, ...])          Rellene los valores NA/NaN utilizando el método especificado.
    filter([elementos, me gusta, expresión regular, eje])   Subconjunto de las filas o columnas del marco de datos de acuerdo con las etiquetas de índice especificadas.
    first(compensar)                                        Seleccione períodos iniciales de datos de series temporales en función de un desplazamiento de fecha.
    first_valid_index()                                     Índice de retorno para el primer valor no NA o Ninguno, si no se encuentra ningún valor no NA.
    floordiv(otro[, eje, nivel, valor_relleno])             Obtenga la división entera del marco de datos y otros elementos (operador binario floordiv ).
    from_dict(datos [, orientación, tipo de d, columnas])   Construya DataFrame a partir de dict of array-like o dicts.
    from_records(datos[, índice, excluir, ...])             Convierta ndarray estructurado o de registros en DataFrame.
    ge(otro[, eje, nivel])                                  Obtener mayor o igual que el marco de datos y otros elementos (operador binario ge ).
    get(clave[, predeterminado])                            Obtenga el elemento del objeto para la clave dada (por ejemplo: columna DataFrame).
    groupby([por, eje, nivel, as_index, ordenar, ...])      Agrupe DataFrame usando un mapeador o por una Serie de columnas.
    gt(otro[, eje, nivel])                                  Obtener Mayor que del marco de datos y otros elementos (operador binario gt ).
    head([norte])                                           Devuelve las primeras n filas.
    hist([columna, por, grilla, xlabelsize, xrot, ...])     Haz un histograma de las columnas del DataFrame.
    idxmax([eje, skipna, numeric_only])                     Índice de retorno de la primera aparición del máximo sobre el eje solicitado.
    idxmin([eje, skipna, numeric_only])                     Índice de retorno de la primera aparición del mínimo sobre el eje solicitado.
    infer_objects()                                         Intente inferir mejores dtypes para columnas de objetos.
    info([verbose, buf, max_cols, memory_usage, ...])       Imprime un resumen conciso de un DataFrame.
    insert(ubicación, columna, valor [, allow_duplicates])  Inserte la columna en DataFrame en la ubicación especificada.
    interpolate([método, eje, límite, en el lugar, ...])    Rellene los valores de NaN utilizando un método de interpolación.
    isetitem(ubicación, valor)                              Establezca el valor dado en la columna con la posición 'loc'.
    isin(valores)                                           Si cada elemento del DataFrame está contenido en valores.
    isna()                                                  Detectar valores faltantes.
    isnull()                                                DataFrame.isnull es un alias de DataFrame.isna.
    items()                                                 Iterar sobre (nombre de columna, Serie) pares.
    iterrows()                                              Iterar sobre las filas de DataFrame como pares (índice, Serie).
    itertuples([índice, nombre])                            Iterar sobre las filas de DataFrame como tuplas con nombre.
    join(otro[, sobre, cómo, lsufijo, rsufijo, ...])        Unir columnas de otro DataFrame.
    keys()                                                  Obtenga el 'eje de información' (consulte Indexación para obtener más información).
    kurt([eje, skipna, nivel, numeric_only])                Devuelve la curtosis imparcial sobre el eje solicitado.
    kurtosis([eje, skipna, nivel, numeric_only])            Devuelve la curtosis imparcial sobre el eje solicitado.
    last(compensar)                                         Seleccione períodos finales de datos de series temporales en función de un desplazamiento de fecha.
    last_valid_index()                                      Índice de retorno para el último valor no NA o Ninguno, si no se encuentra ningún valor no NA.
    le(otro[, eje, nivel])                                  Obtener Menos o igual que del marco de datos y otros elementos (operador binario le ).
    lt(otro[, eje, nivel])                                  Obtenga Menos que del marco de datos y otros elementos (operador binario lt ).
    mask(cond[, otro, en el lugar, eje, nivel, ...])        Reemplace los valores donde la condición sea Verdadera.
    max([eje, skipna, nivel, numeric_only])                 Devuelve el máximo de los valores sobre el eje solicitado.
    mean([eje, skipna, nivel, numeric_only])                Devuelve la media de los valores sobre el eje solicitado.
    median([eje, skipna, nivel, numeric_only])              Devuelve la mediana de los valores sobre el eje solicitado.
    melt([id_vars, value_vars, var_name, ...])              Quite el pivote de un DataFrame de formato ancho a largo y, opcionalmente, deje los identificadores establecidos.
    memory_usage([índice, profundo])                        Devuelve el uso de memoria de cada columna en bytes.
    merge(derecha[,cómo, encendido, izq_enc, der_enco,...]) Combine DataFrame o objetos de serie con nombre con una combinación de estilo de base de datos.
    min([eje, skipna, nivel, numeric_only])                 Devuelve el mínimo de los valores sobre el eje solicitado.
    mod(otro[, eje, nivel, valor_relleno])                  Obtenga Modulo de marco de datos y otros elementos ( mod de operador binario ).
    mode([eje, numeric_only, dropna])                       Obtenga los modos de cada elemento a lo largo del eje seleccionado.
    mul(otro[, eje, nivel, valor_relleno])                  Obtenga la multiplicación del marco de datos y otros, por elementos (operador binario mul ).
    multiply(otro[, eje, nivel, valor_relleno])             Obtenga la multiplicación del marco de datos y otros, por elementos (operador binario mul ).
    ne(otro[, eje, nivel])                                  Obtener No es igual a del marco de datos y otros elementos (operador binario ne ).
    nlargest(n, columnas[, mantener])                       Devuelve las n primeras filas ordenadas por columnas en orden descendente.
    notna()                                                 Detectar valores existentes (no perdidos).
    notnull()                                               DataFrame.notnull es un alias de DataFrame.notna.
    nsmallest(n, columnas[, mantener])                      Devuelve las primeras n filas ordenadas por columnas en orden ascendente.
    nunique([eje, dropna])                                  Cuente el número de elementos distintos en el eje especificado.
    pad(*[, eje, en el lugar, límite, abatido])             Sinónimo de DataFrame.fillna()con method='ffill'.
    pct_change([períodos, método_relleno, límite, frec.])   Cambio porcentual entre el elemento actual y el anterior.
    pipe(función, *args, **kwargs)                          Aplicar funciones encadenables que esperan Series o DataFrames.
    pivot(*[, índice, columnas, valores])                   Devuelve el DataFrame remodelado organizado por valores de índice/columna dados.
    pivot_table([valores, índice, columnas, ...]            Cree una tabla dinámica al estilo de una hoja de cálculo como DataFrame.
    plot                                                    alias de pandas.plotting._core.PlotAccessor
    pop(artículo)                                           Devuelva el artículo y suéltelo del marco.
    pow(otro[, eje, nivel, valor_relleno])                  Obtenga el poder exponencial del marco de datos y otros elementos (operador binario pow ).
    prod([eje, skipna, nivel, numeric_only, ...])           Devuelve el producto de los valores sobre el eje solicitado.
    product([eje, skipna, nivel, numeric_only, ...])        Devuelve el producto de los valores sobre el eje solicitado.
    quantile([q, eje, solo_numérico, ...])                  Devolver valores en el cuantil dado sobre el eje solicitado.
    query(expr, *[, en el lugar])                           Consulta las columnas de un DataFrame con una expresión booleana.
    radd(otro[, eje, nivel, valor_relleno])                 Obtener Adición de marco de datos y otros elementos (operador binario radd ).
    rank([eje, método, numeric_only, ...])                  Calcule rangos de datos numéricos (1 a n) a lo largo del eje.
    rdiv(otro[, eje, nivel, valor_relleno])                 Obtenga la división flotante del marco de datos y otros elementos (operador binario rtruediv ).
    reindex([etiquetas, índice, columnas, eje, ...])        Conforme Series/DataFrame al nuevo índice con lógica de llenado opcional.
    reindex_like(otro[, método, copia, límite, ...])        Devuelve un objeto con índices coincidentes como otro objeto.
    rename([asignador, índice, columnas, eje, copia, ...])  Alterar las etiquetas de los ejes.
    rename_axis([carpeta, en el lugar])                     Establezca el nombre del eje para el índice o las columnas.
    reorder_levels(orden[, eje])                            Reorganizar los niveles de índice utilizando el orden de entrada.
    replace([para_reemplazar, valor,lugar, límite, ...])    Reemplace los valores dados en to_replace con value .
    resample(regla[, eje, cerrado, etiqueta, ...])          Vuelva a muestrear datos de series temporales.
    reset_index([nivel, soltar, en el lugar, ...])          Restablecer el índice, o un nivel del mismo.
    rfloordiv(otro[, eje, nivel, valor_relleno])            Obtenga la división entera del marco de datos y otros elementos (operador binario rfloordiv ).
    rmod(otro[, eje, nivel, valor_relleno])                 Obtenga Modulo de marco de datos y otros elementos (operador binario rmod ).
    rmul(otro[, eje, nivel, valor_relleno])                 Obtenga la multiplicación del marco de datos y otros elementos (operador binario rmul ).
    rolling(ventana[, min_períodos, centro, ...])           Proporcione cálculos de ventana móvil.
    round([decimales])                                      Redondea un DataFrame a un número variable de lugares decimales.
    rpow(otro[, eje, nivel, valor_relleno])                 Obtenga el poder exponencial del marco de datos y otros elementos (operador binario rpow ).
    rsub(otro[, eje, nivel, valor_relleno])                 Obtenga la resta del marco de datos y otros elementos (operador binario rsub ).
    rtruediv(otro[, eje, nivel, valor_relleno])             Obtenga la división flotante del marco de datos y otros elementos (operador binario rtruediv ).
    sample([n, frac, reemplazar, pesos, ...])               Devuelve una muestra aleatoria de elementos de un eje de objeto.
    select_dtypes([incluir excluir])                        Devuelve un subconjunto de las columnas de DataFrame en función de los tipos de columna.
    sem([eje, skipna, nivel, dof, numeric_only])            Devuelve el error estándar imparcial de la media sobre el eje solicitado.
    set_axis(etiquetas, *[, eje, en su lugar, copiar])      Asigne el índice deseado al eje dado.
    set_flags(*[, copiar, allow_duplicate_labels])          Devuelve un nuevo objeto con banderas actualizadas.
    set_index(teclas,*[, colocar, add, lugar, ...])         Establezca el índice de DataFrame usando las columnas existentes.
    shift([períodos, frecuencia, eje, valor_relleno])       Desplace el índice por el número deseado de períodos con una frecuencia de tiempo opcional .
    skew([eje, skipna, nivel, numeric_only])                Devuelve un sesgo imparcial sobre el eje solicitado.
    sort_index(*[, eje, nivel, ascendente, ...])            Ordenar objeto por etiquetas (a lo largo de un eje).
    sort_values(por, *[, eje, ascendente, ...])             Ordene por los valores a lo largo de cualquier eje.
    sparse                                                  alias depandas.core.arrays.sparse.accessor.SparseFrameAccessor
    squeeze([eje])                                          Comprime objetos de un eje dimensional en escalares.
    stack([nivel, dropna])                                  Apila los niveles prescritos de las columnas al índice.
    std([eje, skipna, nivel, dof, numeric_only])            Devuelve la desviación estándar de la muestra sobre el eje solicitado.
    sub(otro[, eje, nivel, valor_relleno])                  Obtenga la resta del marco de datos y otros elementos (operador binario sub ).
    subtract(otro[, eje, nivel, valor_relleno])             Obtenga la resta del marco de datos y otros elementos (operador binario sub ).
    sum([eje, skipna, nivel, numeric_only, ...])            Devuelve la suma de los valores sobre el eje solicitado.
    swapaxes(eje1, eje2[, copiar])                          Intercambie ejes e intercambie ejes de valores apropiadamente.
    swaplevel([i, j, eje])                                  Intercambie los niveles i y j en a MultiIndex.
    tail([norte])                                           Devuelve las últimas n filas.
    take(índices[, eje, es_copia])                          Devuelve los elementos en los índices posicionales dados a lo largo de un eje.
    to_clipboard([sobresalir, septiembre])                  Copie el objeto al portapapeles del sistema.
    to_csv([ruta_o_buf, sep, na_rep, ...])                  Escriba el objeto en un archivo de valores separados por comas (csv).
    to_dict([orientar, hacia])                              Convierta el DataFrame en un diccionario.
    to_excel(excel_writer[, sheet_name, na_rep, ...])       Escribir objeto en una hoja de Excel.
    to_feather(camino, **kwargs)                            Escriba un DataFrame en el formato Feather binario.
    to_gbq(destination_table[, project_id, ...])            Escribe un DataFrame en una tabla de Google BigQuery.
    to_hdf(path_or_buf, key[, mode, complevel, ...])        Escriba los datos contenidos en un archivo HDF5 usando HDFStore.
    to_html([buf, columnas, col_space, encabezado, ...])    Representar un DataFrame como una tabla HTML.
    to_json([path_or_buf, orient, date_format, ...])        Convierta el objeto en una cadena JSON.
    to_latex([buf, columnas, col_space, encabezado, ...])   Representar objeto en una tabla tabular, longtable o anidada de LaTeX.
    to_markdown([buf, modo, índice, op_de_almacen])         Imprima DataFrame en formato compatible con Markdown.
    to_numpy([dtype, copia, na_value])                      Convierta el DataFrame en una matriz NumPy.
    to_orc([ruta, motor, índice, motor_kwargs])             Escriba un DataFrame en formato ORC.
    to_parquet([ruta, motor, compresión, ...])              Escriba un DataFrame en el formato de parquet binario.
    to_period([frecuencia, eje, copia])                     Convierta DataFrame de DatetimeIndex a PeriodIndex.
    to_pickle(ruta[, compresión, protocolo, ...])           Pickle (serializar) objeto para archivar.
    to_records([índice, tipos_d_columna, tipos_d_índice])   Convierta DataFrame en una matriz de registros NumPy.
    to_sql(nombre, contra[, esquema, si_existe, ...])       Escriba registros almacenados en un DataFrame en una base de datos SQL.
    to_stata(ruta, *[, convert_dates, ...])                 Exportar objeto DataFrame a formato Stata dta.
    to_string([buf, columnas, col_space, encabezado, ...])  Renderice un DataFrame en una salida tabular compatible con la consola.
    to_timestamp([frecuencia, cómo, eje, copia])            Transmitir a DatetimeIndex de marcas de tiempo, al comienzo del período.
    to_xarray()                                             Devuelve un objeto xarray del objeto pandas.
    to_xml([ruta_o_búfer, índice, nombre_raíz, ...])        Representar un DataFrame en un documento XML.
    transform(función[, eje])                               Llame funca la autoproducción de un DataFrame con la misma forma de eje que la propia.
    transpose(*argumentos[, copiar])                        Transponer índice y columnas.
    truediv(otro[, eje, nivel, valor_relleno])              Obtenga la división flotante del marco de datos y otros elementos (operador binario truediv ).
    truncate([antes, después, eje, copia])                  Trunca una serie o trama de datos antes y después de algún valor de índice.
    tz_convert(tz[, eje, nivel, copia])                     Convierta el eje tz-aware a la zona horaria de destino.
    tz_localize(tz[, eje, nivel, copia, ...])               Localice el índice tz-naive de una serie o marco de datos para la zona horaria de destino.
    unstack([nivel, valor_de_relleno])                      Gire un nivel de las etiquetas de índice (necesariamente jerárquicas).
    update(otro[, unirse, sobrescribir, ...])               Modifique en su lugar usando valores que no sean NA de otro DataFrame.
    value_counts([subconjunto, normalizar, ordenar, ...])   Devuelve una Serie que contiene recuentos de filas únicas en el DataFrame.
    var([eje, skipna, nivel, dof, numeric_only])            Devuelve la varianza imparcial sobre el eje solicitado.
    where(cond[, otro, en el lugar, eje, nivel, ...])       Reemplace los valores donde la condición sea Falsa.
    xs(clave[, eje, nivel, drop_level])                     Devuelva la sección transversal de la Serie/Marco de datos.


    append(otro[, ignore_index, ...])                       (DEPRECATED) Agrega filas de other al final de la persona que llama, devolviendo un nuevo objeto.
    iteritems()                                             (DEPRECATED) Iterar sobre (nombre de columna, Serie) pares.
    lookup(row_labels, col_labels)                          (DEPRECATED) Función de "indexación elegante" basada en etiquetas para DataFrame.
    mad([eje, skipna, nivel])                               (DEPRECATED) Devuelve la desviación absoluta media de los valores sobre el eje solicitado.
    slice_shift([puntos, eje])                              (DEPRECATED) Equivalente a turno sin copiar datos.
    tshift([períodos, frecuencia, eje])                     (DEPRECATED) Cambia el índice de tiempo, usando la frecuencia del índice si está disponible.
    
    ''')
    pausa()
    limpiar()
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                  PANDAS                                     ║
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║                          generamos DataFrames                               ║
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║                              desde listas                                   ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
    '''
    https://www.w3resource.com/python-exercises/pandas/index-df.php

    https://www.w3resource.com/pandas/df/df-xs.php
    '''
    print("desde archivos importados")
    '''
    df_csv      =   pd.read_csv     ("archivo.csv") #   read_csv usa sep=','
    df_table    =   pd.read_table   ("archivo.csv') #   read_table usa sep='\t'
    df_table    =   pd.read_table   ("archivo.csv,delimiter=',')
    df_json     =   pd.read_json    ("archivo.json")
    df_pickle   =   pd.read_pickle  ("archivo.pkl")
    df_excel    =   pd.read_excel   ("archivo.xlsx", "hoja")
    df_sql      =   pd.read_sql     (query, connection_object))
    '''
    #se generan los dfs a partir de estos orígenes y se trabajan de la misma forma que se verá adelante
    pausa()
    limpiar()
    ####################################################################################################
    list_listas = [[ 1, 4, 5],[ 2, 3, 6],[ 3, 2, 7],[ 4, 1, 8],[ 1, 0, 9],[ 2, 9, 10],[ 3, 8, 11],[ 4, 7 , 12]]
    df = pd.DataFrame(data=list_listas)
    #index y nombre de columnas asignado automáticamente a partir del 0
    print ("Dataframe minimo:")
    print ("con index por default\n",df)
    pausa()
    print("-"*50)
    ####################################################################################################
    df.index = ['A', 'B', 'C' , 'D' , 'E' , 'F' , 'G' , 'H']
    print ("Dataframe con index (alfabético) :\n",df)
    pausa()
    print("*"*50)
    ####################################################################################################
    df.columns = ['UNO', 'DOS', 'TRES']
    print ("Dataframe con nombres en columnas :\n",df)
    pausa()
    print("*"*50)
    ####################################################################################################
    list_listas = [ ['UNO', 'DOS', 'TRES'],[ 1, 4, 5],[ 2, 3, 6],[ 3, 2, 7],[ 4, 1, 8],[ 1, 0, 9],[ 2, 9, 10],[ 3, 8, 11],[ 4, 7 , 12]]
    print('list_listas:',list_listas)
    df.columns = list_listas.pop(0)#   <<----------------------------
    print('columns = list_listas.pop(0)')
    print('list_listas:',list_listas)
    df = pd.DataFrame(data=list_listas)
    print ("Dataframe desde Matriz :\n",df)
    print("-"*50)
    df.index = ['A', 'B', 'C' , 'D' , 'E' , 'F' , 'G' , 'H']
    print ("con index y columnas\n",df)
    pausa()
    print("*"*50)
    ####################################################################################################
    df = pd.DataFrame(data=list_listas, columns=['uno', 'dos','tres'])
    print ("Dataframe :")
    print ("con index y columnas\n",df)
    pausa()
    print("*"*50)
    ####################################################################################################
    df = pd.DataFrame(data=list_listas, columns=['uno', 'dos','tres'],index=[10,11,12,13,14,15,16,17])
    print("\nindice numérico manual:\n",df)
    pausa()
    print("*"*50)
    ####################################################################################################
    df = pd.DataFrame(data=list_listas, columns=['uno', 'dos', 'tres'],index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
    df['Nombre']=['Ariel','Ana','Daniel','Paula','Jose','Juan','Gabriel','Lucia']

    df.name="Análisis de datos"
    print (f'''df.describe ()
    Este método se utiliza para obtener un resumen de los valores numéricos en su conjunto de datos. 

        Calcula con las columnas con valores numéricos
            la cantidad de registros,
            la media, 
            la desviación estándar, 
            el valor mínimo, 
            el primer percentil, 
            el segundo percentil, 
            el tercer percentil,
            el valor máximo. 
    {df.describe ()}\n\n
    Estos datos y muchos mas se pueden obtener por separado
    ''')
    print("DataFrame:",df)
    print("-"*50)
    print("objeto tipo:-------------------------------------->:",type(df))
    print("DataFrame index:---------------------------------->:",df.index)
    print("DataFrame desviacion estandar:-------------------->:",df.std(numeric_only=True))
    print("DataFrame media:---------------------------------->:",df.mean(numeric_only=True))
    print("DataFrame Minimo:--------------------------------->:",df.min(numeric_only=True))
    print("DataFrame Maximo:--------------------------------->:",df.max(numeric_only=True))
    print("DataFrame tamaño:--------------------------------->:",df.size)
    print("DataFrame shape:---------------------------------->:",df.shape)
    print("DataFrame memory_usage:--------------------------->:\n",df.memory_usage())
    print("DataFrame ndim:----------------------------------->:",df.ndim)
    print("DataFrame size:----------------------------------->:",df.size)
    print("DataFrame name:----------------------------------->:",df.name)
    print("DataFrame indice:--------------------------------->:",df.index)
    print("DataFrame columns:-------------------------------->:",df.columns)
    print("DataFrame axes:----------------------------------->:\n",df.axes)
    print("DataFrame dtypes:--------------------------------->:\n",df.dtypes)#TPara ver los tipos de datos de cada columnas
    print("DataFrame empty:---------------------------------->:",df.empty) 
    print("DataFrame info:----------------------------------->:",df.info())   
    print ('''
    El método .info() devuelve la siguiente información sobre cada columna de un DataFrame:
        índice de cada columna, 
        nombres, 
        cantidad de valores no nulos,
        uso de memoria.
    ''')
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
    df = pd.DataFrame(data=dict_series)
    print("df:\n",df)
    print("en at['a','dos'] encontraras :",df.at['a','dos'])
    print("\nDataFrame head muestro los primeros 2:\n",df.head(2))
    print("\nDataFrame tail muestro los ultimos 2:\n",df.tail(2))
    print("\nDataFrame slice muestro filas de la 2 a la 3:\n",df[1:3])
    print("df.describe:\n",df.describe())

    #pd.set_option('max_rows',99999)
    print("df:\n",df)
    #df =del df['d']
    pausa()
    limpiar()
    ####################################################################################################
    print("*"*50)
    #es equivalente a:

    dict_series = {
                'uno'   :["1","28","63","0"],
                'dos'   :["2","12","53","1"],
                'tres'  :["3","22","43","2"],
                'cuatro':["4","32","33","5"],
                'cinco' :["5","52","23","3"],
                'seis'  :["6","42","13","4"],
                'siete' :["7","22","73","6"],
                'ocho'  :["8","12","83","5"],
                'nueve' :["9","21","93","4"],
                'diez'  :["10","31","100","6"],
                }
    original= pd.DataFrame(data=dict_series, index=['a', 'b', 'c', 'd'])


    df = original.copy()
    ####################################################################################################
    print("*"*50)
    dict_series = {
                    'uno'   :["1","-28","63","0"],
                    'dos'   :["2","-12","-53","-"],
                    'tres'  :["3","-","43","2"],
                    'cuatro':["4","-32","33","5"],
                    'cinco' :["5","-52","23","3"],
                    'seis'  :["6","-42","-13","4"],
                    'siete' :["-","-22","73","6"],
                    'ocho'  :["8","-12","-","5"],
                    'nueve' :["9","-21","93","4"],
                    'diez'  :["10","-31","100","-"],
                    }
    df = pd.DataFrame(data=dict_series, index=['a', 'b', 'c', 'd'])


    print("df:\n",df)
    print("en at['a','dos'] encontraras :",df.at['a','dos'])
    print("\nDataFrame head muestro los primeros 2:\n",df.head(2))
    print("\nDataFrame tail muestro los ultimos 2:\n",df.tail(2))
    print("\nDataFrame slice muestro filas de la 2 a la 3:\n",df[1:3])
    print("df.describe:\n",df.describe())

    print("df:\n",df)
    pausa()
    limpiar()
    print("*"*50)
    ####################################################################################################
    print("Creo un DataFrame desde un diccionario con datos random ")
    dict_list={}
    lista_col= range (1,4)

    for col in lista_col:
        valor = range(1*col,25*col,col )
        dict_list[f'Columna_{col}'] = list(valor)
    df = pd.DataFrame(data=dict_list)
    print("\nDataFrame:\n",df)

    pausa()
    limpiar()
    print("*"*50)

    ####################################################################################################
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                  PANDAS                                     ║
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║                  generamos DataFrames desde diccionarios                    ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
    dict_series = {	
                    'uno' : Series([1,2,3,4,1,2,3,4],   index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h']),
                    'dos' : Series([4,3,2,1,0,9,8,7],   index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h']),
                    'tres': Series([5,6,7,8,9,10,11,12],index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
                    }
    df = pd.DataFrame(data=dict_series)
    print("\nDataFrame:\n",df)

    pausa()
    print("*"*50)
    ####################################################################################################
    dict_series = {	
                'uno' : [1,2,3,4,1,2,3,4],
                'dos' : [4,3,2,1,0,9,8,7],
                'tres': [5,6,7,8,9,10,11,12],
                }
    df = pd.DataFrame(data=dict_series, index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
    df['Nombre']=['Ariel','Ana','Daniel','Paula','Jose','Juan','Gabriel','Lucia']

    print("\nDataFrame:\n",df)
    print("-"*50)
    print("\nDataFrame head muestro los primeros 3:\n",df.head(3))
    print ("default = 5")
    print("-"*50)
    print("\nDataFrame tail muestro los ultimos 3:\n",df.tail(3))
    print ("default = 5")
    try:
        print("Estos default se modifica con pd.set_option('max_rows',500) y pd.set_option('max_columns',500)")
        pd.set_option('display.max_rows',500)
        pd.set_option('display.max_columns',500)
        print ("Cambiamos los maximos de visualización por default de pandas")
    except:
        print ("Error al cambiamos los maximos de visualización por default de pandas")
    pausa()
    print("-"*50)
    print("objeto tipo:-------------------------------------->:",type(df))
    print("DataFrame index:---------------------------------->:",df.index)
    print("DataFrame desviacion estandar:-------------------->:",df.std(numeric_only=True))
    print("DataFrame media:---------------------------------->:",df.mean(numeric_only=True))
    print("DataFrame Minimo:--------------------------------->:",df.min(numeric_only=True))
    print("DataFrame Maximo:--------------------------------->:",df.max(numeric_only=True))
    print("DataFrame tamaño:--------------------------------->:",df.size)
    print("DataFrame shape:---------------------------------->:",df.shape)
    print("DataFrame memory_usage:--------------------------->:\n",df.memory_usage())
    print("DataFrame ndim:----------------------------------->:",df.ndim)
    print("DataFrame size:----------------------------------->:",df.size)
    # ~ print("DataFrame name:----------------------------------->:",df.name)
    print("DataFrame indice:--------------------------------->:",df.index)
    print("DataFrame columns:-------------------------------->:",df.columns)
    print("DataFrame axes:----------------------------------->:\n",df.axes)
    print("DataFrame dtypes:--------------------------------->:\n",df.dtypes)#TPara ver los tipos de datos de cada columnas
    print("DataFrame empty:---------------------------------->:",df.empty) 
    print("DataFrame info:----------------------------------->:",df.info())  
    pausa()
    limpiar()
    print("*"*50)
    ####################################################################################################
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                  PANDAS                                     ║
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║                           RENAME(index / columns)                           ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')

    df = pd.DataFrame(data={"A": [1, 2, 3], "B": [4, 5, 6]}, index=["I","II","III"])
    print ("Dataframe :\n",df)
    df = df.rename(index=str, columns={"A": "UNO", "B": "DOS"})
    print ("df.rename() :\n",df)
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                 RESET_INDEX                                 ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}

    df.reset_index (drop= True , inplace= True )
    Tenga en cuenta los siguientes argumentos:

    drop    : Especificar True evita que Pandas guarden el índice original como una columna en el DataFrame.
    inplace : Especificar True permite que Pandas reemplacen el índice en el DataFrame original en lugar de crear una copia del DataFrame.

    ''')
    print ("Dataframe df.rename(str.lower, axis='columns'):\n",df)
    df = df.reset_index()#df = df.reset_index(level=0)

    print ("Dataframe reset_index():\n",df)
    print ("Agrego nuevo index pasando el anterior como una columna 'Index'.")
    pausa()
    print("-"*50)
    df.index=["I","II","III"]
    print ("Dataframe :\n",df)
    df = df.reset_index(drop =True)
    print ("Dataframe reset_index (drop =True):\n",df)
    print ("No agrego nuevo index pasando el anterior como una columna 'Index'.")
    ####################################################################################################
    pausa()
    print("-"*50)
    salida = df.to_string(index = False)
    print ("Dataframe con to_string :\n",salida,"\n type()",type(salida))
    ####################################################################################################
    pausa()
    print("-"*50)
    df['letras']=['UN','MUNDO',' en DATOS']
    print ("original:\n",df)
    df=df.rename(columns={"UNO":"Datos 1 a 3","DOS":"Datos 4 a 6"})
    print ("cambios:\n",df)
    ####################################################################################################
    pausa()
    print("-"*50)
    df = df.rename(str.upper, axis='columns')
    print ("Dataframe df.rename(str.upper, axis='columns'):\n",df)
    ####################################################################################################
    df = pd.DataFrame(data={"A": [1, 2, 3], "B": [4, 5, 6]}, index=["I","II","III"])
    print ("Dataframe :\n",df)
    '''
         A  B
    I    1  4
    II   2  5
    III  3  6
    '''
    pausa()
    print("-"*50)
    df = df.rename({"I":"uno", "II": "dos", "III": "tres"}, axis='index')# axis=0)
    print ("Dataframe df.rename({'I':'uno','II': 'dos','III': 'tres'}, axis='index') o axis=0:\n",df)

    print("-"*50)
    df = df.rename({"A":"Alfa", "B": "Beta"}, axis='columns')# axis=1)
    print ("Dataframe df.rename({'A':'Alfa', 'B': 'Beta'}, axis='columns') o axis=1:\n",df)
    ####################################################################################################
    pausa()
    print("-"*50)
    dict_series = {	
                'uno' : [1,2,3,4,1,2,3,4],
                'dos' : [4,3,2,1,0,9,8,7],
                'tres': [5,6,7,8,9,10,11,12],
                }
    df = pd.DataFrame(data=dict_series)
    print ("Dataframe original:\n",df)
    print("-"*50)
    df.index = ['A', 'B', 'C' , 'D' , 'E' , 'F' , 'G' , 'H']
    df.columns = ['ONE', 'TWO', 'THREE']
    print ("Dataframe con index :\n",df)
    ####################################################################################################
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                  SET_INDEX                                  ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
    REEMPLAZO EL INDEX POR UNO COLUMNA YA EXISTENTE''')
    pausa()
    print("-"*50)
    df['InDeX']=['I', 'II', 'III' , 'IV' , 'V' , 'VI' , 'VII' , 'VIII']
    df = df.set_index("InDeX")
    df = df.rename(columns={0:"uno",1:"dos",2:"tres",3:"Nombres"})
    print ("Dataframe cambio de indexs :\n",df)
    print ("Dataframe.loc[['I','V','VII']] :\n",df.loc[['I','V','VII']] )
    ####################################################################################################
    pausa()
    print("-"*50)
    df = df.rename(index={'I':1, 'II':2, 'III':3 , 'IV':4 , 'V':5 , 'VI':6 , 'VII':7 , 'VIII':8})
    print ("Dataframe cambio de indexs :\n",df)
    ####################################################################################################
    pausa()
    limpiar()
    print("*"*50)
    ####################################################################################################
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                  PANDAS                                     ║
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║                         SELECCIONO X TIPO DE DATOS                          ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
    dict_ = {
                    'uno'   :   [1],
                    'dos'   :   ['Curso 2023'],
                    'tres'  :   [pd.Timestamp(datetime.datetime.now())],
                    'cuatro':   [3.14159],
                    'cinco' :   [True]
                    }
    df = pd.DataFrame(data=dict_, index=['unico'])
    print("\nDataFrame:\n",df)
    print("-"*50)
    print("objeto tipo:-------------------------------------->:",type(df))
    print("DataFrame index:---------------------------------->:",df.index)
    print("DataFrame desviacion estandar:-------------------->:",df.std(numeric_only=True))
    print("DataFrame media:---------------------------------->:",df.mean(numeric_only=True))
    print("DataFrame Minimo:--------------------------------->:",df.min(numeric_only=True))
    print("DataFrame Maximo:--------------------------------->:",df.max(numeric_only=True))
    print("DataFrame tamaño:--------------------------------->:",df.size)
    print("DataFrame shape:---------------------------------->:",df.shape)
    print("DataFrame memory_usage:--------------------------->:\n",df.memory_usage())
    print("DataFrame ndim:----------------------------------->:",df.ndim)
    print("DataFrame size:----------------------------------->:",df.size)
    # ~ print("DataFrame name:----------------------------------->:",df.name)
    print("DataFrame indice:--------------------------------->:",df.index)
    print("DataFrame columns:-------------------------------->:",df.columns)
    print("DataFrame axes:----------------------------------->:\n",df.axes)
    print("DataFrame dtypes:--------------------------------->:\n",df.dtypes)#TPara ver los tipos de datos de cada columnas
    print("DataFrame empty:---------------------------------->:",df.empty) 
    print("DataFrame info:----------------------------------->:",df.info())  
    print("-"*50)
    pausa()
    limpiar()
    print("*"*50)

    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                         SELECCIONO X TIPO DE DATOS                          ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL} 

    metodos:
        include
        exclude
    Tipos Numpy
    Para seleccionar los tipos enteros 'int_','int64','int32','int16','int8','uint64','uint32','uint16','uint8'
        ej  df.select_dtypes(include='int64')
    Para seleccionar los tipos decimales  'float_','float64','float32','float16'
    Para seleccionar todos los tipos numéricos 'np.number' o 'number'

    Para seleccionar los tipos booleanas 'bool_'
    Para seleccionar 'strings', debe usar los objectos dtype 'object'
        nota: Este devolverá todas las columnas con columnas de este dtype 


    np.datetime64Para seleccionar fechas y horas , utilice 'datetime'o 'datetime64'
    Para seleccionar timedeltas, use np.timedelta64, 'timedelta'o 'timedelta64'
    Para seleccionar los dtypes categóricos de Pandas, utilice'category'
    Para seleccionar Pandas datetimetz dtypes, use 'datetimetz' o'datetime64[ns, tz]'

    ''')
    print("\nDataFrame:\n",df)
    print("\nselect_dtypes(include='number')) :\n",df.select_dtypes(include='number'))
    print("-"*50)
    pausa()
    print("\nselect_dtypes(include='int64')) :\n",df.select_dtypes(include='int64'))
    print("-"*50)
    pausa()
    print("\nselect_dtypes(include='float64')) :\n",df.select_dtypes(include='float64'))
    print("-"*50)
    pausa()
    print("\nselect_dtypes(include='bool_')) :\n",df.select_dtypes(include='bool_'))
    print("-"*50)
    pausa()
    print("\nselect_dtypes(include='object')) :\n",df.select_dtypes(include='object'))
    print("-"*50)
    pausa()
    print("\nselect_dtypes(include='datetime64[ns]')) :\n",df.select_dtypes(include='datetime64[ns]'))
    print("-"*50)
    pausa()
    print("\nselect_dtypes(include=['int64','float64'])) :\n",df.select_dtypes(include=['int64','float64']))
    print("-"*50)
    print("\nselect_dtypes(include=['int_','float_'])) :\n",df.select_dtypes(include=['int_','float_']))
    print("-"*50)
    pausa()
    print("\nselect_dtypes(exclude='number')) :\n",df.select_dtypes(exclude='number'))
    pausa()
    print("*"*50)
    limpiar()
    ####################################################################################################
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                  PANDAS                                     ║
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║                           cambio tipos de datos                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
    print ("original:\n",df)
    print("no se puede hacer el cambio si hay NaN")
    df["uno"]=df.uno.astype(str)
    df["dos"]=df.dos.astype(str)
    df["tres"]=df.dos.astype(str)
    print("df: con los datos cambiados x astype(str) \n",df)
    print("df.describe:\n",df.describe())
    print("df.dtypes:\n",df.dtypes)
    pausa()
    limpiar()
    print("*"*50)
    ####################################################################################################
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                     astype                                  ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
    dict_ = {
                'uno'   :   ["1"],
                'dos'   :   ['2023'],
                'tres'  :   [pd.Timestamp(datetime.datetime.now())],
                'cuatro':   [3.14159],
                'cinco' :   [True]
            }
    df = pd.DataFrame(data=dict_, index=['unico'])
    print("\nDataFrame:\n",df)
    df=df.astype({'uno':'int64','dos':'int64','cuatro':'int64','cinco':'int_'})
    print("df: con los datos cambiados x astype(int64) \n",df)
    print("df.describe:\n",df.describe())
    print("df.dtypes:\n",df.dtypes)
    pausa()
    limpiar()
    print("*"*50)
    ####################################################################################################
    print ("Convertimos a 'FLOAT' las columnas uno dos y cuatro")
    df["uno"]   =   df["uno"].astype(float)
    df["dos"]   =   df["dos"].astype(float)
    df["cuatro"]=   df["cuatro"].astype(float)
    print("df: con los datos cambiados x astype(float) \n",df)
    print("df.describe:\n",df.describe())
    print("df.dtypes:\n",df.dtypes)
    pausa()
    limpiar()
    print("*"*50)
    ####################################################################################################
    print ("Convertimos a 'INT' las columnas de a uno")
    df.uno     =   df.uno.astype(int)
    df.dos     =   df.dos.astype(int)
    df.cuatro  =   df.cuatro.astype(int)
    print("df: con los datos cambiados x astype(int) \n",df)
    print("df.describe:\n",df.describe())
    print("df.dtypes:\n",df.dtypes)
    pausa()
    limpiar()
    print("*"*50)
    ####################################################################################################
    print ("Convertimos a 'INT' todas las columnas a un tiempo")
    df1= df.select_dtypes(include='number')[:].astype(int)
    print("df: con los datos cambiados x astype(int) \n",df)
    print("df.describe:\n",df.describe())
    print("df.dtypes:\n",df.dtypes)
    pausa()
    limpiar()
    print("*"*50)
    ####################################################################################################
    print ("Convertimos a 'INT' / 'FLOAT'  las columnas de a uno /dos")
    df=df.astype({'uno':float,'dos':int}).dtypes
    print("df: con los datos cambiados x astype() \n",df)
    print("df.describe:\n",df.describe())
    print("df.dtypes:\n",df.dtypes)
    pausa()
    limpiar()
    print("*"*50)
    ####################################################################################################
    dict_series = {
                    'col1' :[1,28,63,0],
                    'col2' :[1,12,53,0],
                    'col3' :[3,34,43,2],
                    'col4' :[4,32,33,5],
                    'col5' :[5,None,23,3],
                    'col6' :[6,42,13,6],
                    'col7' :[5,22,73,6],
                    'col8' :[4,32,26,5],
                    'col9' :[3,21,np.nan,4],
                    'col10':[1,31,11,0],
                    }
    df = pd.DataFrame(data=dict_series, index=['a', 'b', 'c', 'd'])
    print("df: original \n",df)
    print("df.describe:\n",df.describe())
    print("df.info():\n",df.info)
    print("df.dtypes:\n",df.dtypes)
    df=df.apply(pd.to_numeric, errors='coerce').fillna(0)
    print("df: con df.apply(pd.to_numeric, errors='coerce').fillna(0) \n",df)
    print("df.describe:\n",df.describe())
    print("df.dtypes:\n",df.dtypes)
    pausa()
    limpiar()
    print("*"*50)

    ####################################################################################################

    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                              to_numeric (series)                            ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
    dict_series = {
                    'uno'   :["1","28",np.nan,"0"],
                    'dos'   :["2","12","53",""],
                    'tres'  :["3","","43",np.nan],
                    'cuatro':["4","32","33","5"],
                    'cinco' :["5","52","23","3"],
                    'seis'  :["6","42","13","4"],
                    'siete' :[None,"22","73","6"],
                    'ocho'  :["8","12","","5"],
                    'nueve' :["9",np.nan,"21","4"],
                    'diez'  :["10","31","100",""],
                    }
    df = pd.DataFrame(data=dict_series, index=['a', 'b', 'c', 'd'])

    print("df: original \n",df)
    print("df.describe:\n" ,df.describe())
    print("df.dtypes:\n"   ,df.dtypes)
    pausa()
    print("-"*50)
    ####################################################################################################
    print ("Convertimos to_numeric")
    df1=pd.to_numeric(df.uno)
    print("df: con los datos cambiados x to_numeric() \n",df1)
    print("df.describe:\n",df1.describe())
    print("df.dtypes:\n",df1.dtypes)
    pausa()
    print("-"*50)
    ####################################################################################################
    df1=pd.to_numeric(df["dos"], downcast='float')
    print("df: con los datos cambiados x to_numeric() \n",df1)
    print("df.describe:\n",df1.describe())
    print("df.dtypes:\n",df1.dtypes)
    pausa()
    print("-"*50)
    ####################################################################################################
    df1=pd.to_numeric(df.tres, downcast='signed')
    print("df: con los datos cambiados x to_numeric() \n",df1)
    print("df.describe:\n",df1.describe())
    print("df.dtypes:\n",df1.dtypes)
    pausa()
    print("-"*50)
    ####################################################################################################
    df1=pd.to_numeric(df.cuatro, errors='ignore')
    print("df: con los datos cambiados x to_numeric() \n",df1)
    print("df.describe:\n",df1.describe())
    print("df.dtypes:\n",df1.dtypes)
    pausa()
    print("-"*50)
    ####################################################################################################
    df1=pd.to_numeric(df.cinco, errors='coerce')
    print("df: con los datos cambiados x to_numeric() \n",df1)
    print("df.describe:\n",df1.describe())
    print("df.dtypes:\n",df1.dtypes)
    pausa()
    print("-"*50)
    ####################################################################################################
    #df=original.copy()
    #df=df.astype({'uno':float,'dos':int,'tres':float,'cuatro':int,'uno':float,'dos':int,}).dtypes
    ####################################################################################################
    df1=pd.to_numeric(df.uno)
    print("df: con los datos cambiados x to_numeric(df.uno) \n",df1)
    print("df.describe:\n",df.describe())
    print("df.dtypes:\n",df.dtypes)
    pausa()
    print("-"*50)
    ####################################################################################################
    df1=pd.to_numeric(df.cuatro, downcast='float')
    print("df: con los datos cambiados x to_numeric(df.cuatro, downcast='float') \n",df1)
    print("df.describe:\n",df.describe())
    print("df.dtypes:\n",df.dtypes)
    pausa()
    print("-"*50)
    ####################################################################################################
    df1=pd.to_numeric(df.cinco, downcast='signed')
    print("df: con los datos cambiados x to_numeric(df.cinco, downcast='signed') \n",df1)
    print("df.describe:\n",df.describe())
    print("df.dtypes:\n",df.dtypes)
    pausa()
    print("-"*50)
    ####################################################################################################
    df1=pd.to_numeric(df.cuatro, errors='ignore')
    print("df: con los datos cambiados x to_numeric(df.cuatro, errors='ignore') \n",df1)
    print("df.describe:\n",df.describe())
    print("df.dtypes:\n",df.dtypes)
    pausa()
    print("-"*50)
    ####################################################################################################
    df1=pd.to_numeric(df.tres, errors='coerce')
    print("df: con los datos cambiados x to_numeric(df.tres, errors='coerce') \n",df1)
    print("df.describe:\n",df.describe())
    print("df.dtypes:\n",df.dtypes)
    pausa()
    print("-"*50)
    ####################################################################################################
    df1=pd.to_numeric(df.tres, errors='coerce').fillna(0)
    print("df: con los datos cambiados x to_numeric(df.tres, errors='coerce') \n",df1)
    print("df.describe:\n",df.describe())
    print("df.dtypes:\n",df.dtypes)
    pausa()
    print("-"*50)
    ####################################################################################################
    df1=pd.to_numeric(df.tres, errors='coerce')
    print("df: con los datos cambiados x to_numeric(df.tres, errors='coerce') \n",df1)
    print("df.describe:\n",df.describe())
    print("df.dtypes:\n",df.dtypes)
    pausa()
    limpiar()
    print("*"*50)
    ####################################################################################################
    dfDtypes = pd.DataFrame(
        {
            "a": pd.Series([1, 2, 3], dtype=np.dtype("int32")),
            "b": pd.Series(["x", "y", "z"], dtype=np.dtype("O")),
            "c": pd.Series([True, False, np.nan], dtype=np.dtype("O")),
            "d": pd.Series(["h", "i", np.nan], dtype=np.dtype("O")),
            "e": pd.Series([10, np.nan, 20], dtype=np.dtype("float")),
            "f": pd.Series([np.nan, 100.5, 200], dtype=np.dtype("float")),
        })
    print("df: con los datos originales puestos por dtype() \n",dfDtypes)
    print("df.describe:\n",dfDtypes.describe())
    print("df.dtypes:\n",dfDtypes.dtypes)
    dfDtypes = dfDtypes.convert_dtypes()
    print("df: con los datos cambiados por convert_dtype() \n",dfDtypes)
    print("df.describe:\n",dfDtypes.describe())
    print("df.dtypes:\n",dfDtypes.dtypes)
    pausa()
    print("*"*50)
    ####################################################################################################
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                              Seleccionando datos                            ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
    dict_series = {	
                    'uno' : [1,2,3,4,1,2,3,4],
                    'dos' : [4,3,2,1,0,9,8,7],
                    'tres': [5,6,7,8,9,10,11,12]
                    }
    df = pd.DataFrame(data=dict_series , index=[1,2,3,4,5,6,7,8])
    print("\nDF desde  dict :\n",df)
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                              to_numeric (series)                            ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
    pausa()
    print("*"*50)
    print("df:index | columna 'dos'\n",df['dos'])
    print("df.mean:",df['uno'].mean())
    print("Selecciono datos")
    print("\ndf ['nombre_columna']['nombre_fila']\ndf['uno']['a']:\n",df['uno'][2])
    print("\ndf ['nombre_columnas']\ndf[['uno','dos']]:\n", df[['uno','dos']])
    print("\ndf ['nombre_filas']\ndf[:] [1:4]:\n", df[:] [1:4])
    print("\ndf ['nombre_columnas']['nombre_filas']\ndf[['uno','dos']] [1:4]:\n", df[['uno','dos']] [1:4])
    pausa()
    limpiar()
    print("*"*50)
    ####################################################################################################
    dict_ = {	
            'uno' : [1,2,3,4,1,2,3,4],
            'dos' : [4,3,2,1,0,9,8,7],
            'tres': [5,6,7,8,9,10,11,12]
            }
    df = pd.DataFrame(data=dict_, index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
    print("\nindice dict_ indice alfa:\n",df)
    pausa()
    print("*"*50)
    print("df:index | columna 'dos'\n",df['dos'])
    print("df.mean:",df['uno'].mean())
    print("Selecciono datos")
    print("\ndf ['nombre_columna']['nombre_fila']\ndf['uno']['a']:\n",df['uno']['a'])
    print("\ndf ['nombre_columnas']\ndf[['uno','dos']]:\n", df[['uno','dos']])
    print("\ndf ['nombre_filas']\ndf[:] [1:4]:\n", df[:] [1:4])
    print("\ndf ['nombre_columnas']['nombre_filas']\ndf[['uno','dos']] [1:4]:\n", df[['uno','dos']] [1:4])
    pausa() 
    print("*"*50)
    ####################################################################################################
    df = pd.DataFrame(data=dict_, index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
    df = df >= 2
    print (f"\ndf =df >= 2:\n\n{df}\n") 
    df = pd.DataFrame(data=dict_, index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
    df =df[ df >= 2]
    print (f"\ndf =df[ df >= 2]:\n\n{df}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    df = pd.DataFrame(data=dict_, index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
    print("df:index | columna 'uno'\n",df['uno'])
    print("df:index | columna 'dos'\n",df['dos'])
    print("df.mean:",df['uno'].mean())
    pausa()
    print("*"*50)
    ####################################################################################################
    print("Selecciono datos")
    print("\ndf ['nombre_columna']['nombre_fila']\ndf['uno']['a']:\n",df['uno']['a'])
    pausa() 
    print("*"*50)
    ####################################################################################################
    #PIDO UNA LISTA DE COLUMNAS
    print("\ndf ['nombre_columnas']\ndf[['uno','dos']]:\n", df [['uno','dos']])
    pausa() 
    print("*"*50)
    ####################################################################################################
    print("\ndf ['nombre_filas']\ndf[:] [1:4]:\n", df [:] [1:4])
    pausa() 
    print("*"*50)
    ####################################################################################################
    print("\ndf ['nombre_columnas']['nombre_filas']\ndf[['uno','dos']] [1:4]:\n", df [['uno','dos']] [1:4])
    pausa() 
    print("*"*50)
    ####################################################################################################
    df1 = df [['uno','dos']]
    print (f"\ndf = df [['uno','dos']]:\n\n{df1}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    df1 = df [['uno','dos']] [1:4]
    print (f"\ndf = df [['uno','dos']] [1:4]:\n\n{df1}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    df1 = df[df['tres'] >= 9 ][df['uno'] >= 2]
    print("df:\n",df1,"\n.")
    pausa()
    limpiar()
    print("*"*50)
    ####################################################################################################
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                  PANDAS                                     ║
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║                                 Bucles  for df.items                        ║
    ║                                 Bucles  for df.itertuples                   ║
    ║                                 Bucles  for df.iterrows                     ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
    dict_ = {	
            'uno' : [1,2,3,4,1,2,3,4],
            'dos' : [4,3,2,1,0,9,8,7],
            'tres': [5,6,7,8,9,10,11,12]
            }
    df = pd.DataFrame(data=dict_, index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])

    print ("for label, content in df.items():")
    for label, content in df.items():
        print(f'Item: {label} \n{content}\n')
    pausa()
    print("*"*50)
    ####################################################################################################

    print("for content in df.itertuples ():")
    for content in df.itertuples ():
        print(f'fila {content}\n')
    pausa()
    print("-"*50)

    for content in df.itertuples ():
        print(f'dato Nota 1 = {content.uno} | Nota 2 = {content.dos} | Nota 3 = {content.tres} || promedio = {(content.uno+content.dos+content.tres)/3}\n')
    print("-"*50)
    a,b,c,d=content
    print (f"ultima: fila {a} col1{b} col2{c} col3 {d}")
    pausa()
    print("*"*50)
    ####################################################################################################
    print ("for Index, content in df.iterrows ():")
    for Index, content in df.iterrows ():
        print(f'fila {Index} \n columnas-valor\n{content}\n')
    pausa()
    print("-"*50)
    for Index, content in df.iterrows ():
        print(f'dato {Index} Nota 1 = {content.uno} | Nota 2 = {content.dos} | Nota 3 = {content.tres} || promedio = {(content.uno+content.dos+content.tres)/3}\n')
    pausa()
    limpiar()
    print("*"*50)
    ####################################################################################################
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                  PANDAS                                     ║
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║                                    LOC                                      ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
    print("""Trabajo por los nombres de fila-columnas
    loc[Nombre fila,Nombre columna]
    loc[Nombre fila origen: Nombre fila fin , Nombre columna origen : Nombre columna fin]
    loc[[Nombre lista filas seleccionadas], [Nombre lista columnas seleccionadas]]
    """)
    dict_ = {	
            'uno' : [1,2,3,4,1,2,3,4],
            'dos' : [4,3,2,1,0,9,8,7],
            'tres': [5,6,7,8,9,10,11,12]
            }
    df = pd.DataFrame(data=dict_, index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
    print("original:\n",df)
    pausa() 
    print("*"*50)
    ####################################################################################################
    print("original:\n",df)
    print("-"*50)
    print("df:index | fila 'loc['b']'\n",df.loc['b'])
    df.loc['b']= 333
    print("-"*50)
    print("original:\n",df)
    pausa() 
    print("*"*50)
    ####################################################################################################
    print("df:index | fila 'loc[['b']]'\n",df.loc[['b']])
    pausa()
    print("*"*50)
    ####################################################################################################
    df = df
    print ('original:\n',df)
    df.loc[df['tres'] > 10] = 0
    print("df:index busco en col 'tres' valores > 10 reemplazo por 0'\n",df)
    pausa()
    print("*"*50)
    ####################################################################################################
    print("df.columna dos sin loc:\n",df[['dos']])
    pausa() 
    print("*"*50)
    ####################################################################################################
    print("df.columna dos con loc:\n",df.loc[:,"dos"])
    pausa() 
    print("*"*50)
    ####################################################################################################
    df=df.loc[:, df.columns != "dos"]
    print("df.loc[:, df.columns != 'dos']:\n",df)
    pausa() 
    print("*"*50)
    ####################################################################################################
    dict_ = {	
            'uno' : [1,2,3,4,1,2,3,4],
            'dos' : [4,3,2,1,0,9,8,7],
            'tres': [5,6,7,8,9,10,11,12]
            }
    df = pd.DataFrame(data=dict_, index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
    '''
    original:
        uno  dos  tres
    a    1    4     5
    b    2    3     6
    c    3    2     7
    d    4    1     8
    e    1    0     9
    f    2    9    10
    g    3    8    11
    h    4    7    12
    '''
    print("original:\n",df)
    print("-"*50)
    print("df.index | fila 'loc['b',:'tres']\n",df.loc['b',:'tres'])
    print("-"*50)
    df.loc['b','tres']=9999
    print("-"*50)
    print("cambio:\n",df)
    pausa() 
    print("*"*50)
    ###################################################################################################
    df = pd.DataFrame(data=dict_, index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
    print("df.index | fila 'loc[['b'],:'tres']\n",df.loc[['b'],:'tres'])
    pausa()
    print("*"*50)
    ####################################################################################################
    df = pd.DataFrame(data=dict_, index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
    print("df:index | fila 'loc['b':'d','dos']'\n",df.loc['b':'d',"dos"])	
    pausa() 
    print("*"*50)
    ####################################################################################################
    print("df:index | fila 'loc['b':'d',:'tres']'\n",df.loc['b':'d',:'tres'])
    pausa() 
    print("*"*50)
    ####################################################################################################
    print("df:index | fila 'loc['b':'d','uno':'tres']'\n",df.loc['b':'d','uno':'tres'])
    pausa() 
    print("*"*50)
    ####################################################################################################
    print (f"\ndf = df.loc[['b','d'],['uno','dos'] ]:\n\n{df.loc[['b','d'],['uno','dos'] ]}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    print (f"\ndf = df.loc[::]:\n\n{df.loc[::]}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    print (f"\ndf = df.loc[::-1]:\n\n{df.loc[::-1]}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    print("original:\n",df)
    print (f"\ndf = df.describe().loc[['min','max']]:\n\n{df.describe().loc[['min','max']]}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    print("original:\n",df)
    print (f"\ndf = df.describe().loc[['min','max'],'uno':'tres']:\n\n{df.describe().loc[['min','max'],'uno':'tres']}\n") 
    pausa() 
    limpiar()
    print("*"*50)
    ####################################################################################################
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                  PANDAS                                     ║
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║                                   ILOC                                      ║
    ║              Las filas y columnas son referidas por posición                ║
    ║                 con números enteros comenzando desde el 0                   ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
    print("""Trabajo por cordenadas numericas fila-columnas
    iloc[fila,columna]
    iloc[fila origen: fila fin , columna origen : columna fin]
    iloc[[lista filas seleccionadas], [lista columnas seleccionadas]]
    """)
    dict_series = {	
                'uno' : [1,2,3,4,1,2,3,4],
                'dos' : [4,3,2,1,0,9,8,7],
                'tres': [5,6,7,8,9,10,11,12],
                }
    df = pd.DataFrame(data=dict_series)#, index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
    df['Nombre']=['Ariel','Ana','Daniel','Paula','Jose','Juan','Gabriel','Lucia']
    print("\n shape :",df.shape)
    print("\n describe :\n",df.describe())
    print("original:\n",df)
    pausa() 
    print("*"*50)
    ####################################################################################################
    #print (f"\ndf.iloc[:, lambda df: [0, 2]]:\n\n{df.iloc[:, lambda df: [0, 2]]}\n") 
    print (f"\ndf.iloc[:, [0, 2]]:\n\n{df.iloc[:, [0, 2]]}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    # Primera fila
    print (f"\ndf.iloc[0]:\n\n{df.iloc[0]}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    print("original:\n",df)
    print("-"*50)
    print("df:index | fila 'iloc[1]'\n",df.iloc[1]) # Segunda fila
    df1=df.copy()
    df1.iloc[1]= 333
    print("-"*50)
    print("original:\n",df1)
    pausa() 
    print("*"*50)
    ####################################################################################################
    df1 = df.iloc[1] # Segunda fila
    print (f"\ndf.iloc[1]:\n\n{df1}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    df1 = df.iloc[-1] # Última fila
    print (f"\ndf.iloc[-1]:\n\n{df1}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    print("original:\n",df)
    print (f"\ndf.iloc[lambda x: x.index % 2 == 0]:\n\n{df.iloc[lambda x: x.index % 2 == 0]}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    df1 = df.iloc[:, 0] # Primera columna
    print (f"\ndf.iloc[:, 0]:\n\n{df1}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    df1 = df.iloc[:, 1] # Segunda columna
    print (f"\ndf.iloc[:, 1]:\n\n{df1}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    df1 = df.iloc[:, -1] # Última columna
    print (f"\ndf.iloc[:, -1]:\n\n{df1}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    df1 = df.iloc[0:5] # Primeras cinco filas
    print (f"\ndf.iloc[0:5]:\n\n{df1}\n") 
    pausa() 
    print("*"*50)
    print("original:\n",df)
    ####################################################################################################
    df1 = df.iloc[-2:]  # ante Última columna al final
    print (f"\ndf.iloc[-2:]:\n\n{df1}\n") 
    pausa() 
    print("*"*50)
    print("original:\n",df)
    ####################################################################################################
    print("-"*50)
    print("df.index | fila 'iloc[5,:3]\n",df.iloc[5,0:3])
    print("-"*50)
    ####################################################################################################
    df1= df.copy()
    df1.iloc[5,2]=9999
    print("-"*50)
    print("cambio:\n",df1)
    pausa() 
    print("*"*50)	
    ####################################################################################################
    df1 = df.iloc[:, 0:5] # Primeras cinco columnas
    print (f"\ndf.iloc[:, 0:5]:\n\n{df1}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    df1 = df.iloc [1:4, :] # Primera a cuarta fila todas las  columnas
    print (f"\ndf.iloc [1:4, :]:\n\n{df1}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    df1 = df.iloc [1:4, 1:3]# Primera a cuarta fila, columnas uno a la tres
    print (f"\ndf.iloc [1:4, 1:3]:\n\n{df1}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    df1 = df.iloc[2:5,1:3]# segunda a quinta fila, columnas uno a la tres
    print (f"\ndf.iloc[2:5,1:3]:\n\n{df1}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    df1 = df.iloc[1:5,0:2]
    print (f"\ndf.iloc[1:5,0:2]:\n\n{df1}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    df1 = df.iloc[[0,2,1]]  # Primera, tercera y segunda filas
    print (f"\ndf.iloc[[0,2,1]]:\n\n{df1}\n")
    pausa() 
    print("*"*50)
    ####################################################################################################
    df1 = df.iloc[:, [0,2,1]]  # Primera, tercera y segunda columnas
    print (f"\ndf.iloc[:, [0,2,1]]:\n\n{df1}\n") 
    pausa() 
    print("*"*50)
    df.iloc[[0, 2], [1, 3]]
    ####################################################################################################
    df1 = df.iloc[[5,6,7], [0,2,1]]  # Primera, tercera y segunda filas // Primera, tercera y segunda columnas
    print (f"\ndf.iloc[[5,6,7], [0,2,1]]:\n\n{df1}\n") 
    print("*"*50)
    ####################################################################################################
    df = df.iloc[::]
    print (f"\ndf = df.loc[::]:\n\n{df}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    df = df.iloc[::-1]
    print (f"\ndf = df.loc[::-1]:\n\n{df}\n") 
    pausa() 
    print("*"*50)
    ####################################################################################################
    df = df.iloc[:,::-1]
    print (f"\ndf = df.iloc[::-1]:\n\n{df}\n") 
    pausa() 
    limpiar()
    print("*"*50)
    ####################################################################################################
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                  PANDAS                                     ║
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║                                    AT                                       ║
    ║                Funciona de la misma forma que el método loc,                ║
    ║                siendo at un método de acceso rápido a un dato               ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
    ####################################################################################################
    #df = pd.DataFrame(data=dict_serie, index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
    dict_series = {	
                'uno' : [1,2,3,4,1,2,3,4],
                'dos' : [4,3,2,1,0,9,8,7],
                'tres': [5,6,7,8,9,10,11,12],
                }
    df = pd.DataFrame(data=dict_series, index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])

    print("original:\n",df)
    print("en at['c','dos'] encontraras :",df.at['c','dos'])
    print("Sobrescribimos el valor at['c','dos']= 9 ")
    df.at['c','dos']=9
    print("en at['c','dos'] ahora :",df.at['c','dos'])
    pausa()
    print("*"*50)
    ####################################################################################################
    print("en at['a','uno'] encontraras :",df.at['a','uno'])
    print("Sobrescribimos el valor at['a','uno']=222 ")
    df.at['a','uno']=222
    print("en at['a','uno'] ahora :",df.at['a','uno'])
    pausa()
    print("*"*50)
    ####################################################################################################
    dict_listas = {'uno' : [1, 2, 3, 4], 'dos' : [4, 3, 2, 1]}
    df2 = pd.DataFrame(data=dict_listas)
    print("total:\n",df2)
    print("en at[1,'dos'] encontraras :",df2.at[1,'dos'])
    pausa()
    print("*"*50)
    ####################################################################################################
    print("Cambio de index de numero a letras")
    df2 = pd.DataFrame(data=dict_listas, index=['a', 'b', 'c', 'd'])
    print("total:\n",df2)
    print("en at['c','dos'] encontraras :",df2.at['c','dos'])
    pausa()
    print("*"*50)
    ####################################################################################################
    dict_series = {
                    'uno' : [1, 2, 3, 4],
                    'dos' : [4, 3, 2, 1]
                    }
    df2 = pd.DataFrame(data=dict_series)
    print("total index automatico:\n",df2)
    df2 = pd.DataFrame(data=dict_series, index=['a', 'b', 'c', 'd'])
    print("total indice alfabetico:\n",df2)
    print("en at['c','dos'] encontraras :",df2.at['c','dos'])
    pausa()
    limpiar()
    print("*"*50)
    ####################################################################################################
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                  PANDAS                                     ║
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║                                    IAT                                      ║
    ║                Funciona de la misma forma que el método iloc,               ║
    ║                siendo IAT un método de acceso rápido a un dato              ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
    ####################################################################################################
    print("original:\n",df)
    print("en iat[2,2] encontraras :",df.iat[2,2])
    print("Sobrescribimos el valor iat[2,2]= 9 ")
    df.iat[2,2]=999
    print("en iat[2,2] ahora :",df.iat[2,2])
    print("cambios:\n",df)
    pausa()
    print("*"*50)
    ####################################################################################################
    print("original:\n",df)
    print("en iat[0,1] encontraras :",df.iat[0,1])
    print("Sobrescribimos el valor iat[0,1]=222 ")
    df.iat[0,1]=222
    print("en iat[0,1] ahora :",df.iat[0,1])
    print("cambios:\n",df)
    pausa()
    print("*"*50)
    ####################################################################################################
    dict_listas = {
                    'uno' : [1, 2, 3, 4],
                    'dos' : [4, 3, 2, 1]
                    }
    df2 = pd.DataFrame(data=dict_listas)
    print("total:\n",df2)
    print("en iat[0,1] encontraras :",df2.iat[0,1])
    pausa()
    print("*"*50)
    ####################################################################################################
    print("Cambio de index de numero a letras")
    df2 = pd.DataFrame(data=dict_listas, index=['a', 'b', 'c', 'd'])
    print("total:\n",df2)
    print("en iat[3,1] encontraras :",df2.iat[3,1])
    pausa()
    print("*"*50)

    ####################################################################################################

    df2 = pd.DataFrame({
                    'uno' : [1, 2, 3, 4],
                    'dos' : [4, 3, 2, 1]
                    })
    print("total index automiatico:\n",df2)
    serie_uno = df2.uno
    print("serie_uno:\n",df2)
    serie_uno = df2['uno']
    print("serie_uno:\n",df2)
    df2 = pd.DataFrame(data=dict_series, index=['a', 'b', 'c', 'd'])
    print("total indice alfabetico:\n",df2)
    print("en iat[2,0] encontraras :",df2.iat[2,0])
    limpiar()
    print("*"*50)

####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                   TAKE                                      ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
dict_series = {
                'uno'   :["1","28",np.nan,"0"],
                'dos'   :["2","12","53",""],
                'tres'  :["3","","43",np.nan],
                'cuatro':["4","32","33","5"],
                'cinco' :["5","52","23","3"],
                'seis'  :["6","42","13","4"],
                'siete' :[None,"22","73","6"],
                'ocho'  :["8","12","","5"],
                'nueve' :["9",np.nan,"21","4"],
                'diez'  :["10","31","100",""],
                }
df = pd.DataFrame(data=dict_series, index=['0', '1', '2', '3'])
print("original:\n",df)
print("en df.take([1,3], axis=0) encontraras :\n",df.take([1,3], axis=0))
pausa()
print("*"*50)
print("en df.take([1,2], axis=1) encontraras :\n",df.take([1,2], axis=1))
pausa()
limpiar()
print("*"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.RED}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                      "IX" DEPRECATED / DESACTUALIZADO                       ║
║               Funcionaba de la misma forma que el método loc,               ║
║               siendo at un método de acceso rápido a un dato                ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')

# ~ print ("Este método facilita la selección de datos, puesto que permite filtrar con valores que no se encuentran en el df. 
# ~ Los datos de la columna fecha fueron creados desde '2012-4-10' hasta '2015-1-4' con el formato aaaa-mm-dd. 
# ~ Si se necesita hacer un filtro con dos fechas que tienen la hora, los métodos anteriores no son de utilidad puesto que estos valores 
# ~ no se encuentran en el índice.")
# ~ print("""
# ~ Indexer is a hybrid of .loc and .iloc. Generally, ix is label based and acts just as the .loc indexer. However, 
# ~ .ix also supports integer type selections (as in .iloc) where passed an integer. This only works where the index of 
# ~ the DataFrame is not integer based. ix will accept any of the inputs of .loc and .iloc.
# ~ Slightly more complex, I prefer to explicitly use .iloc and .loc to avoid unexpected results.
# ~ .ix[] supports mixed integer and label based access. It is primarily label based, but will fall back to integer positional 
# ~ access unless the corresponding axis is of integer type.
# ~ .ix is the most general indexer and will support any of the inputs in .loc and .iloc. .ix also supports floating point label schemes. 
# ~ .ix is exceptionally useful when dealing with mixed positional and label based hierarchical indexes.
# ~ """)
print(F'''{Fore.WHITE+Back.RED}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                  "set_value" DEPRECATED / DESACTUALIZADO                    ║
║             Funcionaba para establecer datos en alguna posición             ║
║            del DF siendo "at" un método de acceso rápido a un dato          ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
# ~ """)
pausa()
limpiar()
print("*"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                 Groupby                                     ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')

####################################################################################################
dict_series = {	
            'uno' : [1,2,3,4,1,2,3,4],
            'dos' : [4,3,2,1,0,9,8,7],
            'tres': [5,6,7,8,9,10,11,12],
            }
df = pd.DataFrame(data=dict_series, index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
print("original:\n",df)
grupo_sum = df.groupby('uno').apply(sum)
print("df.groupby('uno').apply(sum)")
print("suma de los valores del grupo segun del index 'uno' :\n",grupo_sum)
print("como veras hay en la columna 'uno' agrupado un solo 111, pero dos 2 = 4 y un 4")
print("como veras hay en la columna 'dos' no estan agrupados asi q los valores seran 6-(3+4)- ,9-4 y 3-111")
pausa()
print("*"*50)
####################################################################################################
grupo = df.groupby('uno')
print("original:\n",df)
print("Objeto del grupo a :\n",grupo)
print("Agrupados x los datos de la columna 'uno' en un bucle")
for nombre, datos in grupo:
    print (nombre)
    print (datos)
print ("Como veras agrupa los datos segun los valores de 'uno', dentro de un for podemos ver las filas separadas") 
pausa()
print("*"*50)
####################################################################################################
grupo = df.groupby('uno').sum()
print("suma de todos los datos col UNO:\n", grupo)
pausa()
print("*"*50)
####################################################################################################
grupo = df.groupby('uno').mean()
print("Promedio de todos los datos agrupados por los val col UNO :\n", grupo)
pausa()
print("*"*50)
####################################################################################################
dict_series = {	
                'uno' : [1,2,3,4,1,2,3,4],
                'dos' : [4,3,2,1,0,9,8,7],
                'tres': [5,6,7,8,9,10,11,12],
                }
df = pd.DataFrame(data=dict_series, index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
df['Nombre']=['Ariel','Ana','Daniel','Paula','Jose','Juan','Gabriela','Lucia']
df['profesor']=['Maria','Jorge','Maria','Jorge','Maria','Jorge','Lucas','Lucas']
df['sexo']=['M','F','M','F','M','M','F','F']
original2=df.copy()
print("original:\n",df)
grupo = df.groupby('profesor').agg({"uno":"max",
                                        "dos":"min",
                                        "tres":"mean"
                                        })
print('grupo de todos los datos agrupados "uno":"max","dos":"min","tres":"mean" :\n', grupo)
# ~ import matplotlib.pyplot as plt
grupo.plot(kind='line')
plt.show()

pausa()
print("-"*50)

####################################################################################################
df = pd.DataFrame(data=
                {
                    'turno':	["M","M","M","M","M","M","T","T","T","T"],
                    'nombre': 	['Juan', 'Ricardo', 'Ana', 'Luis', 'Laura', 'Marta', 'Andrea', 'Jose', 'Pedro', 'Ines'],
                    'apellido': ['Perez', 'Garcia', 'Gonzalez', 'Gomez', 'Lujan', 'Martinez', 'Molina', 'Costa', 'Gilar', 'Mendez'],
                    'puesto':	['Administracion', 'Marketing', 'Contable', 'Produccion', 'Mantenimiento', 'Produccion','Produccion', 'Mantenimiento', 'Produccion', 'Mantenimiento'],
                    'nota_1C':	[10,9,5,7,8,9,6,7,8,9],
                    'nota_2C':	[8,9,10,9,5,7,8,9,6,7],
                    'Final':	[9,6,7,8,9,10,9,5,7,8]
                }, 
                columns=['turno','nombre', 'apellido', 'puesto','nota_1C','nota_2C','Final'], 
                )
print ("Original:\n",df)
grupo = df.groupby('turno').Final.mean()
print("grupo = df.groupby('turno').Final.mean():\n", grupo)
pausa()
print("-"*50)
####################################################################################################
grupo1 = df.groupby('turno').Final.min()
print("grupo = df.groupby('turno').Final.min():\n", grupo1)
pausa()
print("-"*50)
####################################################################################################
grupo2 = df.groupby('turno').Final.max()
print("grupo = df.groupby('turno').Final.max():\n", grupo2)
pausa()
print("-"*50)
####################################################################################################
grupo3 = df.groupby('turno').Final.agg(['sum','count'])
print("grupo = df.groupby('turno').Final.agg(['sum','count']):\n", grupo3)
pausa()
print("-"*50)
####################################################################################################
print ("Original:\n",df)
grupo4 = df.groupby('turno')[['nota_1C','nota_2C']].mean()
print("grupo = df.groupby('turno').Final.mean():\n", grupo4)
pausa()
print("-"*50)
####################################################################################################
grupo5 = df.groupby('turno').Final.sum()
print("grupo = df.groupby('turno').Final.sum():\n", grupo5)
print (len(grupo5))
pausa()
print("-"*50)
####################################################################################################
print ("Original:\n",df)
grupo6 = df.groupby('turno').Final.transform('sum')
print("grupo = df.groupby('turno').Final.transform('sum'):\n", grupo6)
df['promedio']=(df['nota_1C']+df['nota_2C'])/2
print ("Original:\n",df)
pausa()
print("-"*50)
####################################################################################################
grupo_ = df.Final.mean()
print("grupo_ = df.Final.mean():\n", grupo_)
pausa()
print("-"*50)
####################################################################################################
grupo7 = df.groupby('turno').Final.mean()
print("grupo = df.groupby('turno').Final.mean():\n", grupo7)
pausa()
print("-"*50)
####################################################################################################
grupo8 = df.groupby(['turno','promedio']).Final.mean()
print("grupo = df.groupby(['turno','promedio']).Final.mean():\n", grupo8)
pausa()
print("-"*50)
####################################################################################################
grupo9 = df.groupby(['turno','promedio']).Final.mean().unstack()
print("grupo = df.groupby(['turno','promedio']).Final.mean().unstack():\n", grupo9)	
print("*"*50)
####################################################################################################
grupo = grupo[grupo["tres"]>9]
print('grupo de los grupos de los datos=> grupo[grupo["tres"]>5]: \n', grupo)
pausa()
print("*"*50)

# ~ import matplotlib.pyplot as plt
grupo.plot(kind='bar')
plt.show()

#while True:pass
####################################################################################################
df=base.copy()
print ("Original:\n",df)
grupo = df.groupby(['uno']).size().reset_index(name='repeticiones')
print("df.groupby(['uno']).size().reset_index(name='repeticiones'):\n", grupo)
pausa()
print("*"*50)
####################################################################################################
df=base.copy()
print ("Original:\n",df)
grupo = df.groupby('uno')['uno'].count()
print("df.groupby('uno')['uno'].count():\n", grupo)
pausa()
limpiar()
print("*"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                              pivot tables                                   ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
####################################################################################################
dfPivot = pd.DataFrame(data=
                {
                    'turno':	["M","M","M","M","M","M","T","T","T","T"],
                    'nombre': 	['Juan', 'Ricardo', 'Ana', 'Luis', 'Laura', 'Marta', 'Andrea', 'Jose', 'Pedro', 'Ines'],
                    'apellido': ['Perez', 'Garcia', 'Gonzalez', 'Gomez', 'Lujan', 'Martinez', 'Molina', 'Costa', 'Gilar', 'Mendez'],
                    'sexo':		["M","M","F","M","F","F","F","M","M","F"],
                    'puesto':	['Administracion', 'Marketing', 'Contable', 'Produccion', 'Mantenimiento', 'Produccion','Produccion', 'Mantenimiento', 'Produccion', 'Mantenimiento'],
                    'nota_1C':	[10,9,5,7,8,9,6,7,8,9],
                    'nota_2C':	[8,9,10,9,5,7,8,9,6,7],
                    'Final':	[9,6,7,8,9,10,9,5,7,8],
                }, 
                columns=['turno','nombre','apellido','sexo','puesto','nota_1C','nota_2C','Final'], 
                )
dfPivot['promedio']=(dfPivot['nota_1C']+dfPivot['nota_2C'])/2
#tablas dinamicas rerequieren las filas, columnas, valores y filtro


df=dfPivot.copy()
print ("Original:\n",df)

pt_1=df.pivot_table(index='turno',columns='nombre',values='promedio',aggfunc='mean')

print("pivot_table.:\n", pt_1)

pt_2=df.pivot_table(index='turno',columns='nombre',values='sexo',aggfunc='count')
# ~ https://www.youtube.com/watch?v=RlIiVeig3hc
# ~ 22:30

print("pivot_table.:\n", pt_2)
pausa()
#limpiar()
print("*"*50)



####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                         filtros / condicionales                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')

print("""
Parametros:

path_or_buf: El objeto Archivo para escribir los datos CSV. Si no se proporciona este argumento de ruta, los datos CSV se devuelven como una cadena y podemos imprimir la cadena para ver cómo se ven nuestros datos CSV.
sep: Es el delimitador de los datos CSV. Debe ser la cadena de longitud 1 y el valor predeterminado es una coma.
na_rep: Es una cadena que representa valores nulos o perdidos; el valor predeterminado es una cadena vacía
columns: Es la secuencia para especificar las columnas que se incluirán en la salida CSV.
header: Los valores permitidos son booleanos o la lista de cadenas, el valor predeterminado es True. Si es False, los nombres de las columnas no se escriben en la salida. Si es la lista de cadenas, se usa para escribir los nombres de las columnas. La longitud de la lista de la cadena debe ser la misma que la cantidad de columnas que se escriben en el archivo CSV.
index: Si es True, el índice se incluye en los datos CSV. Si se establece en False, el valor del índice no se escribe en la salida CSV.
index_label: Se utiliza para especificar el nombre de la columna del índice.
""")
print("df_0 total:\n",df_0)
pausa()
print("*"*50)
serie = df_0 ['uno']> 2
print("serie = df_0 ['uno']> 2")
print("\nSerie de datos bool (True/False)de cada fila en la columna 'uno':\n",serie)
pausa()
print("*"*50)
####################################################################################################
df = df_0 [df_0['uno']> 2]
print("df_0 [df_0['uno']> 2]")
print("\nFiltro los datos en un nuevo 'df' donde la salida es True:\n",df)
pausa()
print("*"*50)
####################################################################################################
df = df_0 [df_0['tres']< 8]
print("df_0 [df_0['tres']< 8]")
print("\nFiltro los datos en un nuevo 'df' donde la salida es True:\n",df)
pausa()
print("*"*50)
####################################################################################################
#df = df_0 [df_0['uno']!= 2]
df = df_0 [df_0.uno != 2]
print("df_0 [df_0.uno  !=2]")
print("\nFiltro los datos en un nuevo 'df' donde la salida es True:\n",df)
pausa()
print("*"*50)
####################################################################################################
df = df_0 [(df_0['uno']> 2)&(df_0['tres'] <10)] # logic y
print("df_0 [(df_0['uno']> 2)&(df_0['tres'] <10)]")
print("\nFiltro los datos en un nuevo 'df' donde la salida es True:\n",df)
pausa()
print("-"*50)

df = df_0 [~(df_0['uno']> 2)&(df_0['tres'] <10)] # logic y
print("df_0 [(df_0['uno']> 2)&(df_0['tres'] <10)]")
print("\nFiltro los datos en un nuevo 'df' donde la salida NO (~) es True:\n",df)
pausa()
print("*"*50)
####################################################################################################
df = df_0 [(df_0['uno']> 2)|(df_0['tres'] <8)] # lógica o
print("df_0 [(df_0['uno']> 2)|(df_0['tres'] <8)] # lógica o")
print("\nFiltro los datos en un nuevo 'df' donde la salida es True:\n",df)
pausa()
print("*"*50)
####################################################################################################
print ("df_0['uno'] == 2:\n", df_0['uno'] == 2)
print("busco la condicion de que en 'uno' tenga el valor ==2 y devuelvo una booleana de la fila")
pausa()
print("*"*50)
####################################################################################################
print ("df_0.loc[(df_0['uno'] == 2),['dos','tres']]:\n",df_0.loc[(df_0['uno'] == 2),['dos','tres']])
print("busco la condicion de que en 'uno' tenga el valor ==2 y x .loc las valores encontrados en la fila pero en la columna dos y tres")
pausa()
print("*"*50)
####################################################################################################
print ("df_0.loc[(df_0['uno'] == 2),['dos','tres']]:\n",df_0.loc[~(df_0['uno'] == 2),['dos','tres']])
print("busco la condicion de que en 'uno' NO(~) tenga el valor ==2 y x .loc las valores encontrados en la fila pero en la columna dos y tres")
pausa()
print("*"*50)
####################################################################################################
df = df [(df['uno']!= 2)] # lógica no
print("\nFiltro los datos en un nuevo 'df' donde la salida son todos los datos diferente a 2 como True:\n",df)
pausa()
print("*"*50)
####################################################################################################
df = df [~(df['uno']!= 2)] # lógica no
print("\nFiltro los datos en un nuevo 'df' donde la salida no (~) son todos los datos diferente a 2 como True:\n",df)
pausa()
print("*"*50)
####################################################################################################
print ("original:\n",df)
df = df ['uno'][df['dos']> 2] 
print("\nFiltro los datos en un nuevo 'df' donde la salida es la columna1 sobre la condicion de la columna2 :\n",df)
pausa()
print("*"*50)
####################################################################################################
print ("original:\n",df)
df = df ['uno'][df['dos']<= 5]*100 
print("\nFiltro los datos en un nuevo 'df' donde la salida es la columna1 *100 sobre la condicion de la columna2 :\n",df)
pausa()
print("*"*50)
####################################################################################################
df_0.loc[df_0['uno'] < 2, 'Es menor que dos?'] = 'True' 
df_0.loc[df_0['uno'] != 2, 'Es diferente que dos?'] = 'False' 
print ("creo d columnas nuevas como resultado de la condicion y cargo el estado en c/una:\n",df_0)
pausa()
print("*"*50)
####################################################################################################
names = {'First_name': ['Jon','Bill','Maria','Emma']}
df = pd.DataFrame(data=names,columns=['First_name'])
df.loc[(df['First_name'] == 'Bill') | (df['First_name'] == 'Emma'), 'name_match'] = 'Match'  
print (df)
df.loc[(df['First_name'] != 'Bill') & (df['First_name'] != 'Emma'), 'name_match'] = 'Mismatch'  
print ( df)
pausa()
limpiar()
print("*"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║            'transform' aplica una funcion a todos los elementos             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
df =base.copy()
df=df.drop(['Nombre'], axis=1)
df=df[['uno','dos','tres']].astype(int)

print ("original:\n",df,"\n",df.dtypes)

pausa()

print("-"*50)
def funcion (dato):
    print (dato)
    return dato * 2
df = df.transform (funcion) # actualiza cada entrada de un DataFrame sin ningún bucle
print("\ntransform x funcion los datos en un nuevo 'df' donde las salidas son las columnas al cuadrado :\n",df)
pausa()
print("-"*50)
df = df.transform (lambda dato: dato ** 2) # actualiza cada entrada de un DataFrame sin ningún bucle
print("\ntransform x lambda los datos en un nuevo 'df' donde las salidas son las columnas al cuadrado :\n",df)
pausa()
limpiar()
print("*"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║               'apply'  aplica una funcion a todos los elementos             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
df = baseN.copy()

pd.set_option('max_rows',99999)
pd.set_option('max_columns',99999)
print ("original:\n",df)
####################################################################################################
df["len"] = df.Nombre.apply(len)
print(f"\napply x funcion len a la columna 'Nombre' :\n{df.loc[:,['Nombre','len']]}")
pausa()
print("-"*50)

####################################################################################################
df = baseN.copy()
print("-"*50)
def funcion (dato):
    return (type(dato),dato)
df = df.apply (funcion, axis=0) # actualiza cada entrada de un DataFrame sin ningún bucle
print(f"\napply x funcion los datos en un nuevo 'df' donde las salidas son los datos y typo axis=0:\n{df}\n")
pausa()
df = df.apply (funcion, axis=1) # actualiza cada entrada de un DataFrame sin ningún bucle
print(f"\napply x funcion los datos en un nuevo 'df' donde las salidas son los datos y tipo axis=1:\n{df}\n")

####################################################################################################

pausa()
print("-"*50)
df = base.copy()
print ("original:\n",df)
pausa()
print("-"*50)
def funcion (dato):
    return dato ** 2
df = df.apply (funcion, axis=0) # actualiza cada entrada de un DataFrame sin ningún bucle
print("\napply x funcion los datos en un nuevo 'df' donde las salidas son las columnas al cuadrado axis=0:\n",df)
pausa()
df = df.apply (funcion, axis=1) # actualiza cada entrada de un DataFrame sin ningún bucle
print("\napply x funcion los datos en un nuevo 'df' donde las salidas son las columnas al cuadrado axis=1:\n",df)

####################################################################################################

pausa()
print("-"*50)
df = base.copy()
df = df.apply (lambda dato: dato ** 2, axis=0) # actualiza cada entrada de un DataFrame sin ningún bucle
print("\napply x lambda los datos en un nuevo 'df' donde las salidas son las columnas al cuadrado axis=0:\n",df)
pausa()
df = df.apply (lambda dato: dato ** 2, axis=1) # actualiza cada entrada de un DataFrame sin ningún bucle
print("\napply x lambda los datos en un nuevo 'df' donde las salidas son las columnas al cuadrado axis=1:\n",df)
pausa()
print("-"*50)

####################################################################################################
df = base.copy()
print ("original:\n",df)
df = df.apply (np.sqrt)
print ("cambio df.apply (np.sqrt):\n",df)
pausa()
print("-"*50)
####################################################################################################
df = base.copy()
print ("original:\n",df)
df = df.apply (np.sum, axis=0)
print ("cambio df.apply (np.sum, axis=0):\n",df)
pausa()
print("-"*50)
####################################################################################################
df = base.copy()
print ("original:\n",df)
df = df.apply (np.sum, axis=1)
print ("cambio df.apply (np.sum, axis=1):\n",df)
pausa()
print("-"*50)
####################################################################################################
df = base.copy()
print ("original:\n",df)
df = df.applymap (lambda x: float(x) )
print("-"*50)
print ("cambio applymap de int a float:\n",df)
pausa()
print("-"*50)
####################################################################################################
df = base.copy()
print ("original:\n",df)
df = df.applymap (lambda x: x**2 )
print("-"*50)
print ("cambio applymap de x**2:\n",df)
pausa()
print("-"*50)

####################################################################################################
dfRandom = pd.DataFrame(np.random.rand(4,2),columns=['UNO','DOS'])

print(f"dfRandom:\n",dfRandom)
print(f"dfRandom:\n",dfRandom.rename({"UNO":"Col_A","DOS":"Col_B"},axis=1))
pausa()
print("-"*50)
####################################################################################################

print(f"dfRandom:\n",dfRandom.rename({"UNO":"Col_I","DOS":"Col_II"},axis='columns'))
pausa()
print("-"*50)
####################################################################################################

print(f"dfRandom:\n",dfRandom.rename(columns={"UNO":"Col_1","DOS":"Col_2"}))
pausa()
print("-"*50)
####################################################################################################

dfRandom.columns=["COLUMN ONE","COLUMN TWO"]
print(f"dfRandom:\n",dfRandom)
pausa()
print("-"*50)
####################################################################################################

dfRandom.columns=dfRandom.columns.str.replace(' ', '_')
print(f"dfRandom:\n",dfRandom)
pausa()
print("-"*50)
####################################################################################################

dfRandom.columns=["I","II"]
print(f"dfRandom:\n",dfRandom)
pausa()
print("-"*50)
####################################################################################################

dfRandom=dfRandom.add_prefix('Col_')
dfRandom=dfRandom.add_suffix('_2023')
print(f"dfRandom:\n",dfRandom)
####################################################################################################
    
bebedores = pd.read_csv('http://bit.ly/drinksbycountry')
pd.set_option('max_rows',99999)
pd.set_option('max_columns',99999)
print (f"bebedores:\n{bebedores}")
pausa()

print (f"bebedores:\n{bebedores.loc[:,['total_litres_of_pure_alcohol']].apply(max,axis=0)}")#['country','total_litres_of_pure_alcohol','continent']
pausa()
print("-"*50)
####################################################################################################

print (f"bebedores:\n{bebedores.loc[:,['total_litres_of_pure_alcohol']].apply(min,axis=0)}")#['country','total_litres_of_pure_alcohol','continent']
pausa()
print("-"*50)
####################################################################################################
#print (f"bebedores:\n{bebedores.loc[:,['beer_servings','spirit_servings','wine_servings']].apply(np.argmax,axis=1)}")#['country','total_litres_of_pure_alcohol','continent']

print (f"bebedores:\n{bebedores.loc[:,'beer_servings':'wine_servings'].applymap(float)}")
pausa()
print("-"*50)
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║             uso de memoria df.info(memory_usage='deep')                     ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
        
bebedores = pd.read_csv('http://bit.ly/drinksbycountry')
print (f"bebedores:\n{bebedores.head(5)}")
print (f"{ bebedores.info(memory_usage='deep')}\n")
pausa()
bebedores = pd.read_csv('http://bit.ly/drinksbycountry')
columnasElejidas=['beer_servings','spirit_servings','wine_servings']
bebedores = pd.read_csv('http://bit.ly/drinksbycountry',usecols=columnasElejidas)
print (f"bebedores:\n{bebedores.head(5)}")
print (f"{ bebedores.info(memory_usage='deep')}\n")
pausa()
bebedores = pd.read_csv('http://bit.ly/drinksbycountry')
Tipos = {'continent':'category'}
bebedores = pd.read_csv('http://bit.ly/drinksbycountry',usecols=columnasElejidas, dtype=Tipos)
print (f"bebedores:\n{bebedores.head(5)}")
print (f"{ bebedores.info(memory_usage='deep')}\n")

pausa()
limpiar()
print("*"*50)

####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                  query                                      ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
print("""
pd.DataFrame.query es una forma muy elegante / intuitiva de realizar esta tarea, pero a menudo es más lenta.
Sin embargo, si presta atención a los siguientes tiempos, para datos grandes, la consulta es muy eficiente.
Más que el enfoque estándar y de similar magnitud como mi mejor sugerencia.""")
df = baseN.copy()
print ("original:\n",df)
df = df.query('uno > dos')
print("\nFiltro query con los datos donde uno sea mayor que dos:\n",df)
df = df[df.uno > df.dos]
print("\nFiltro slice los datos donde uno sea mayor que dos:\n",df)


print("Tiene una gran utilidad sobretodo cuando el nombre de las columnas tienen espacios\nEj.:'Nombre y Apellido' == 'Perez'")
print("The query() method uses a slightly modified Python syntax by default. For example, the & and | (bitwise) operators have the precedence of their boolean cousins, and and or. This is syntactically valid Python, however the semantics are different.")
pausa()
limpiar()
print("*"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                   eval                                      ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
####################################################################################################
df = df.eval('uno < dos <= tres != uno')
print (" df.eval('uno < dos <= tres != uno':\n",df)
pausa()
print("*"*50)
####################################################################################################
df = df.loc[(df.eval('uno < dos <= tres != uno')),['uno','dos','tres']]
print (" df.eval('uno < dos <= tres != uno':\n",df)
pausa()
print("*"*50)
####################################################################################################
df = df.loc[(df.eval('uno > 2 and dos >= 2 or tres > 10')),['uno','dos','tres']]
print (" df.eval('uno > 2 and dos >= 2 or tres > 10'):\n",df)
pausa()
print("*"*50)
####################################################################################################
df = df.loc[(df.eval('uno > 2 & dos >= 2 | tres > 10')),['uno','dos','tres']]
print (" df.eval('uno > 2 & dos >= 2 | tres > 10'):\n",df)
pausa()
print("*"*50)
####################################################################################################
df = pd.DataFrame(data={'A': range(1, 6),
                   'B': range(10, 0, -2),
                   'C C': range(10, 5, -1)})
print ("We can use query function with backticks quoting as shown in Pandas documentation.")
df2=df.query("B == `C C`")
print (df2)
# ~ df.query('B == `C C`',inplace = True)
# ~ print (df)
pausa()
print("*"*50)
####################################################################################################
df2=df[df['A'] > 3]
print (df2)
pausa()
print("*"*50)
#			igual
df2=df.query('A > 3')
print (df2)
pausa()
print("*"*50)
####################################################################################################
df = pd.DataFrame(data={'dato 1': range(1, 6),
                   'dato 2': range(10, 0, -2),
                   'dato 3': range(10, 5, -1)})
print ("comparo ojo con la comilla `   .")
df=df.query('`dato 2` == `dato 3`')
print (" donde 'dato 2 == dato 3':\n",df)
pausa()
limpiar()
print("*"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                   isin                                      ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
####################################################################################################
df = base.copy()
print("Original:\n",df)
salida = df.isin([1,4])
salida2 = df.isin({'uno':[1,4]})
print ("En todas las columnas:\n", salida)
print ("Solo en la columna 'uno':\n",salida2)
print ("Solo en la columna 'uno':\n",df[salida2])
####################################################################################################
lista = [4, 2]
resultado = df[(df['uno'] == 1) &  df['dos'].isin(lista)] 
print("\nFiltro df[(df['uno'] == 1) &  df['dos'].isin(lista)]:\n",resultado)
pausa()
print("*"*50)
####################################################################################################
lista_ = [1, 3]
lista = [4, 2]
resultado = df[(df['uno'].isin(lista_)) &  (df['dos'].isin(lista))] 
#resultado = df[(df['uno'] == 1) &  df['dos'].isin(lista)] 
print("\nFiltro df[(df['uno'] == 1) &  df['dos'].isin(lista)]:\n",resultado)
print("""
DataFrame.isin(values)[source]
Permite filtrar comparando contra un array .
""")

pausa()
print("*"*50)
####################################################################################################

lista = ["A","J"]
df = df[df['Nombre'].str[0].isin(lista)] 
df = df.sort_values('Nombre')
df = df.reset_index()
print("\nFiltro df[df['Nombre'].str[0].isin(lista)] :\n",resultado)
pausa()
print("*"*50)

lista = ["A","J"]
df = df[df['Nombre'].str[0].isin(lista)] 
df = df.sort_values('Nombre')
df = df.reset_index()
print("\nFiltro df[df['Nombre'].str[0].isin(lista)] :\n",resultado)
pausa()
print("*"*50)
##lista
print ("isin lista")
salida = df.isin(lista)
print('DataFrame\n-----------\n',df)
print('\lista\n-----------\nlista\n',lista)
print('\nDataFrame.isin(lista)\n-----------\n',salida)
pausa()
print("*"*50)
#series
print ("isin series")
serie_ = pd.Series([ 2,1])
salida = df.isin(serie_)
print('DataFrame\n-----------\n',df)
print('\nSeries\n-----------\nindes\serie\n',serie_)
print('\nDataFrame.isin(series)\n-----------\n',salida)
pausa()
print("*"*50)
#diccionario
print ("isin diccionario")
dic_ = {"uno":[1, 2]}
salida = df.isin(dic_)

print('DataFrame\n-----------\n',df)
print('\diccionario\n-----------\n',dic_)
print('\nDataFrame.isin(diccionario)\n-----------\n',df[salida])
#DataFrame
print ("isin DataFrame_")
DataFrame_ =pd.DataFrame ({"uno":[2, 1],"dos":[3,4]})
salida = df.isin(DataFrame_)

print('DataFrame\n-----------\n',df)
print('\DataFrame_\n-----------\n',DataFrame_)
print('\nDataFrame.isin(DataFrame_)\n-----------\n',df[salida])

####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                  Between                                    ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
####################################################################################################
df=original.copy()
print("df original:\n",df)
df=df[df['uno'].between('b','d')]
print("df between: \n",df)
print("df.describe:\n",df.describe())
print("df.dtypes:\n",df.dtypes)
pausa()
limpiar()
print("*"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                    Map                                      ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')

df=original2.copy()
df["sexo_bool"] = df.sexo.map({'M':0 , 'F':1})
print("df df.sexo.map({'M':0 , 'F':1}):\n",df)	
print("df df.sexo.map({'M':0 , 'F':1}):\n",df.loc[:,["Nombre","sexo", "sexo_bool"]])
pausa()
print("-"*50)
####################################################################################################

df=original.copy()
df = df.max(axis=1)
print("df maximo de cada fila:\n",df)	
pausa()
print("-"*50)
####################################################################################################
df = df.max(axis=0)#   = df = df.max()
print("df maximo de cada columna:\n",df)	
pausa()
print("-"*50)
####################################################################################################
print("df original:\n",df)
df['uno']=df['uno'].map({1:"insuficiente",2:"regular",3:"aceptable",4:"aprobado"})
print("df cambio:\n",df)	
pausa()
print("-"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                   Split                                     ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
dframe = pd.DataFrame({'nombre':['Ariel Horacio Garcia','Maria Laura Gonzalez','Juan Manuel Perez'],
                        'email':['cursos.agt@gmail.com','MLG@hotmail.com','JMG@yahoo.com'],
                        'horarios':[[8,16],[12,18],[16,24]]})
print ('df\n:',dframe)
pausa()
print("-"*50)
####################################################################################################
dframe[['Nombre','2do','Apellido']] = dframe.nombre.str.split(" ", expand=True)
print("dframe:\n",dframe)
pausa()
print("-"*50)
####################################################################################################

dframe_series= dframe.horarios.apply(pd.Series)
print("dframe:\n",dframe_series)
pausa()
print("-"*50)
####################################################################################################

dframe= pd.concat([dframe,dframe_series], axis=1)
print("dframe:\n",dframe)
pausa()
limpiar()
print("*"*50)
####################################################################################################
df=original.copy()
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                  replace                                    ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
print("df original:\n",df)
print("-"*50)
df['uno']=df['uno'].replace(1,"insuficiente")
print("df cambio:\n",df)
pausa()
####################################################################################################
print("-"*50)
df['uno']=df['uno'].replace([1,2,3,4],value=["insuficiente","regular","aceptable","aprobado"])
print("df cambio:\n",df)
pausa()
####################################################################################################

print("-"*50)
df['uno']=df['uno'].replace({1:"insuficiente",2:"regular",3:"aceptable",4:"aprobado"})
print("df cambio:\n",df)
pausa()
####################################################################################################
print("-"*50)
df = pd.DataFrame(data={
                    'A': ['bat', 'foo', 'bait'],
                    'B': ['abc', 'bar', 'xyz']
                    })
print("df original:\n",df)			
print("-"*50)
df= df.replace(to_replace=r'^ba.$', value='new', regex=True)
print("df cambio:\n",df)
pausa()
limpiar()
print("*"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                  Resumen                                    ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
####################################################################################################
print("df.info:\n",df.describe())
print("""
df.describe(percentiles=None, include=None, exclude=None, datetime_is_numeric=False)[source]
Generate descriptive statistics.
Descriptive statistics include those that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values.
Analyzes both numeric and object series, as well as DataFrame column sets of mixed data types. The output will vary depending on what is provided. Refer to the notes below for more detail.
""")
pausa()
print("*"*50)
####################################################################################################
print("df.info:\n",df.info)
print ("""
df.info(verbose=None, buf=None, max_cols=None, memory_usage=None, show_counts=None, null_counts=None)[source]
Print a concise summary of a DataFrame.
This method prints information about a df including the index dtype and columns, non-null values and memory usage.""")
pausa()
print("*"*50)
####################################################################################################
print("df.select_dtypes:\n",df.select_dtypes,"\nDataFrame.select_dtypes(include=None, exclude=None)[source]\nReturn a subset of the DataFrame’s columns based on the column dtypes.")
pausa()
print("*"*50)

####################################################################################################
print("df.memory_usage:\n",df.memory_usage())
print("""DataFrame.memory_usage(index=True, deep=False)[source]
Return the memory usage of each column in bytes.
The memory usage can optionally include the contribution of the index and elements of object dtype.
This value is displayed in DataFrame.info by default. This can be suppressed by setting""")
pausa()
print("*"*50)
####################################################################################################
print("df.astype:\n",df.astype,"\nCast a pandas object to a specified dtype")

pausa()
print("*"*50)
####################################################################################################
print("df.convert_dtypes:\n",df.convert_dtypes,"""\n
DataFrame.convert_dtypes(infer_objects=True, convert_string=True, convert_integer=True, convert_boolean=True, convert_floating=True)[source]
Convert columns to best possible dtypes using dtypes supporting pd.NA.
""")
df_NaN = pd.DataFrame(data=
    {
        "a": pd.Series([1, 2, 3], dtype=np.dtype("int32")),
        "b": pd.Series(["x", "y", "z"], dtype=np.dtype("O")),
        "c": pd.Series([True, False, np.nan], dtype=np.dtype("O")),
        "d": pd.Series(["h", "i", np.nan], dtype=np.dtype("O")),
        "e": pd.Series([10, np.nan, 20], dtype=np.dtype("float")),
        "f": pd.Series([np.nan, 100.5, 200], dtype=np.dtype("float")),
    }
)
print ('df_NaN original:\n',df_NaN)
pausa()
print("-"*50)
print ('df_NaN.isna:\n',df_NaN.isna())
pausa()
print("-"*50)
print ('df_NaN.notna:\n',df_NaN.notna())
pausa()
print("-"*50)
print (df_NaN[df_NaN['d'].isnull()])#print (df_NaN[df_NaN[['a','b','c','d']].isnull()])
pausa()
print("-"*50)
print ("ver el archivo 015_Python_Intro_Pandas_03_Conversion como convertir los NaN")
pausa()
print("*"*50)
####################################################################################################

print ("df original:\n",df_NaN)
print ("df:\n",df_NaN.dtypes)

dfn = df_NaN.convert_dtypes()
print ("df convert_dtypes:\n",dfn)
print ("df:\n",dfn.dtypes)
pausa()
print("*"*50)

####################################################################################################
print("df.infer_objects:\n Attempt to infer better dtypes for object columns")

dfn = df.infer_objects()
print ("df:\n",dfn)
print ("df:\n",dfn.dtypes)

pausa()
print("*"*50)
####################################################################################################
print("df.copy:\nhace una copia el df")
df_copia = df.copy()
print ("df_copia:\n",df_copia)
pausa()
print("*"*50)
####################################################################################################
print("df.bool:\n",df.bool,"\nRegreso una bool como elemento unico Series or DataFrame.")
# ~ pd.DataFrame(data={'col': [True]}).bool()#True
# ~ pd.DataFrame(data={'col': [False]}).bool()#False
pausa()
print("*"*50)
####################################################################################################
print("original:\n",df_copia)
print("df.bool:\n",df_copia.pop('uno'),"\nRegresa los items y borra (drop) del frame.")
pausa()
print("*"*50)
####################################################################################################
print("df.head:\n",df.head(5),"\nAccede a los valores del inicio del df - default = 5 ")
pausa()
print("*"*50)
####################################################################################################
print("df.tail:\n",df.tail(5),"\nAccede a los valores del final del df  - default = 5 ")
pausa()
print("*"*50)
####################################################################################################
print("df.at['c','dos']:\n",df.at['c','dos'],"\nAccede a un solo valor para un par de etiquetas de fila / columna.")
pausa()
print("*"*50)
####################################################################################################
print("df:\n",df)
print("df.iat[2,2]:\n",df.iat[2,2],"\nAccede a un valor único para un par de filas / columnas por posición entera.")
pausa()
print("*"*50)
####################################################################################################
print("df.attrs:\n",df.attrs,"\nDiccionario de atributos globales de este objeto.")
pausa()
print("*"*50)
####################################################################################################
print("df.axes:\n",df.axes,"\nDevuelve una lista que representa los ejes del DataFrame.")
pausa()
print("*"*50)
####################################################################################################
print("df.columns:\n",df.columns,"\nLas etiquetas de columna del DataFrame.")
pausa()
print("*"*50)
####################################################################################################
print("df.dtypes:\n",df.dtypes,"\nDevuelve los dtypes en el DataFrame.")
pausa()
print("*"*50)
####################################################################################################
print("df.empty:\n",df.empty,"\nIndicador de si DataFrame está vacío.")
pausa()
print("*"*50)
####################################################################################################
print("df.loc['c','dos']:\n",df.loc['c','dos'],"\nAcceda a un grupo de filas y columnas por etiqueta (s) o una matriz booleana.")
pausa()
print("*"*50)
####################################################################################################
print("df.iloc[2,2]:\n",df.iloc[2,2],"\nIndexación basada puramente en la ubicación de números enteros para la selección por posición.")
pausa()
print("*"*50)
####################################################################################################
print("df.index:\n",df.index,"\nEl índice (etiquetas de fila) del DataFrame.")
pausa()
print("*"*50)
####################################################################################################
print("df.ndim:\n",df.ndim,"\nDevuelve un entero que representa el número de ejes / dimensiones de matriz.")
pausa()
print("*"*50)
####################################################################################################
print("df.shape:\n",df.shape,"\nDevuelve una tupla que representa la dimensionalidad del DataFrame.")
pausa()
print("*"*50)
####################################################################################################
print("df.size:\n",df.size,"\nDevuelve un ententero que representa el número de elementos de este objeto..")
pausa()
print("*"*50)
####################################################################################################

df = df.copy()
df=df[['uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez']].astype(int)
print ("original:\n",df,'\n',df.dtypes )
pares = df % 2 == 0
print ("pares en booleana:\nEs par?\n",pares)

pausa()
limpiar()
print("*"*50)

# ~ np.random.seed(seed=41)
# ~ df2 = pd.DataFrame(data=np.random.randint(0,10,(4,3)), columns=('Nota1', 'Nota2', 'Nota3'), index=['Ariel', 'Ana', 'Juan', 'Maria']  )
# ~ print (df2)
####################################################################################################
dict_ = {	
        'uno' : [1,2,3,4,1,2,3,4],
        'dos' : [4,3,2,1,0,9,8,7],
        'tres' : [5,6,7,8,9,10,11,12]
        }
dframe = pd.DataFrame(data=dict_, index=['a', 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h'])
print("\nindice dict_ indice alfa:\n",dframe)
print ("dframe[dframe.uno == 1].tres.sum()):\n",dframe[dframe.uno == 1].tres.sum())
pausa()
print ("dframe[dframe.tres >= 9].uno.mean():\n",dframe[dframe.tres >= 9].uno.mean())
pausa()

####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                WHERE toma los elementos que cumplen la condicion            ║
║   mask marca con NaN o un valor los elementos que no cumplen la condicion   ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
print('pd.DataFrame.where(cond=condition_to_check, other="Value To Fill")')
####################################################################################################
df = original.copy()
print (df)
df=df[['uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez']].astype(int)
pares = df % 2 == 0
df1=df.where(pares, 0)
print("df.where():\n",df1,"\nreemplaza los datos que no son True x 0.")
print("DataFrame.where(cond, other=nan, inplace=False, axis=None, level=None, errors='raise', try_cast=False)[source]")
pausa()
print("-"*50)

df1=df.where( cond=(df % 2 == 0), other=~df )

print("df.where():\n",df1,"\nreemplaza los datos que no son True x (-) ~ el valor anterior.")
pausa()
print("-"*50)
####################################################################################################

df1 = df.where(lambda x: x>6, "Ok")

print("df.where():\n",df1,"\nreemplaza los datos que no son True x por 'ok'.")
pausa()
print("-"*50)
####################################################################################################
pares = df % 2 == 0
df2=df.mask(pares, 1)
print("df.mask:\n",df2,"\nDevuelve function inversa a la condicion where.")
print("DataFrame.mask(self, cond, other=nan, inplace=False, axis=None, level=None, errors='raise', try_cast=False)")
pausa()
print("-"*50)
df1 = df.mask(lambda x: x<=6, "nop")

print("df.mask():\n",df1,"\nreemplaza los datos que son True x por 'nop'.")
pausa()
print("*"*50)
####################################################################################################
salida = df.where(df >= 7, "desaprobado") 
salida = salida.mask(df >= 7, "aprobado") 
print ("aprobados / desaprobados:\n", salida)
pausa()
print("-"*50)
####################################################################################################
pares = df % 2 == 0
salida = df.where(pares, -df)
print ("Una presentacion:\n", salida.to_markdown())
pausa()
print("-"*50)
####################################################################################################
print("Una mejor presentacion:\n", df.to_markdown(tablefmt="grid"))
pausa()
print("-"*50)
####################################################################################################
pares = df % 2 == 0
salida = df.where(pares, "impar")
print ("invertimos los impares:\n", salida)
pausa()
print("-"*50)
####################################################################################################
pares = df % 2 == 0
salida = df.where(~pares, "par")
print ("invertimos los pares:\n", salida)
# ~ pausa()
# ~ print("-"*50)
####################################################################################################
pares = df % 2 == 0
# ~ salida =  df.where(pares, -df) == df.mask(~pares, df)
# ~ print ("Salida:\n", salida)
# ~ pausa()
# ~ print("-"*50)
####################################################################################################
pausa()
limpiar()
print("*"*50)
#####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                  values                                     ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
print("df.values:\n",df.values,"\nDevuelve una representación Numpy del DataFrame.")
pausa()
limpiar()
print("*"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                  operaciones ej.sum() product() o prod()                    ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')

####################################################################################################
df = original.copy()
print ("Original:\n",df)
print("df.suma columna:\n",df.sum(axis=0))
pausa()
print("*"*50)
####################################################################################################
print("df.suma columna 'uno' :\n",df['uno'] .sum(axis=0))
print("df.suma columna 'dos' :\n",df['dos'] .sum(axis=0))
print("df.suma columna 'tres':\n",df['tres'].sum(axis=0))
pausa()
print("*"*50)
####################################################################################################
# ~ print ("original:\n",df)
# ~ df['suma'] =df['uno'].sum()
# ~ print ("cambio:\n",df)

# ~ pausa()
# ~ print("-"*50)
####################################################################################################
print("df.suma fila:\n",df.sum(axis=1))
print("-"*50)
print("df.producto fila:\n",df.product(axis=1))
print("-"*50)
pausa()
print("-"*50)
####################################################################################################
df.loc['total_suma_x_Col']=df.sum(axis=0)
print("df.suma columna:\n",df)
pausa()
limpiar()
print("-"*50)
####################################################################################################

df.loc[:,'total_suma_x_fila']=df.sum(axis=1)
print("df.suma fila:\n",df)
pausa()
# ~ limpiar()
print("^"*50)
####################################################################################################
df.loc['total_producto_x_Col']=df.product(axis=0)
print("df.product columna:\n",df)
pausa()
print("-"*50)
####################################################################################################

df.loc[:,'total_producto_x_Fila']=df.product(axis=1)
print("df.producto fila:\n",df)
pausa()
limpiar()
print("*"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                           operaciones ej.mean                               ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')

####################################################################################################
df = original.copy()
print("df.original:\n",df)
print("df.mean columna:\n",df.mean(axis=0))
pausa()
print("*"*50)

####################################################################################################
print("df.mean columna 'uno' :\n",df['uno'] .mean(axis=0))
print("df.mean columna 'dos' :\n",df['dos'] .mean(axis=0))
print("df.mean columna 'tres':\n",df['tres'].mean(axis=0))
pausa()
print("*"*50)

####################################################################################################
# ~ print ("original:\n",df)
# ~ df['mean'] =df['uno'].mean()
# ~ print ("cambio:\n",df)

# ~ pausa()
# ~ print("-"*50)
####################################################################################################
df.loc['promedio_x_Col']=df.mean(axis=0)
print("df.mean columna:\n",df)
pausa()
print("*"*50)
####################################################################################################
print("df.mean fila:\n",df.mean(axis=1))
df.loc[:,'promedio_x_fila']=df.mean(axis=1)
print("df.mean fila:\n",df)
pausa()
limpiar()
print("*"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                        operaciones ej.min /  max                            ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
####################################################################################################
print("df.min columna:\n",df.min(axis=0))
pausa()
print("-"*50)
print("df.min fila:\n",df.min(axis=1))
pausa()
print("-"*50)
print("df.max columna:\n",df.max(axis=0))
pausa()
print("-"*50)
print("df.max fila:\n",df.max(axis=1))
pausa()
limpiar()
print("*"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                   insert agrega fila en ultimo lugar                        ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
# ~ df=original.T.copy()
# ~ ####################################################################################################
# ~ print("df original:\n",df)
df = pd.DataFrame()
print ('df:', df,'\nsize:',  df.size)
FilaAingresar = {'uno':[99,0],'dos':[88,1],'tres':[77,2]}
df=df.append(pd.DataFrame(data=FilaAingresar))
print("df cambio append :\n",df)
pausa()
print("*"*50)
NuevosFilaAingresar = {'uno':999,'dos':888,'tres':777}
df=df.append(NuevosFilaAingresar, ignore_index=True)
print("df cambio append :\n",df)
pausa()
limpiar()
print("*"*50)

####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║               insert agrega columnas en el lugar deseado                    ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
df=original.T.copy()
####################################################################################################
print("df original:\n",df)
ColAingresar = [9,8,7,6,5,4,3,2,1,0]

#                lugar   
df.insert(loc = 3,column="nuevo",value=ColAingresar)
print("df cambio:\n",df)

ColAingresar.sort()
#                lugar  
df.insert( 0,"orden",ColAingresar)
print("df cambio:\n",df)
pausa()
limpiar()
print("*"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                       agrega filas en el lugar deseado                      ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
df=original.T.copy()
####################################################################################################
print("df original:\n",df)
FilaAingresar = [99,88,77,66]
#                lugar   
df.loc['dos'] =  FilaAingresar
df.loc['cuatro'] =  [0,999,0,999]
print("df cambio:\n",df)
pausa()
limpiar()
print("*"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                    drop Borro filas/col en el lugar deseado                 ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')

df=original.copy()
####################################################################################################
print("df original:\n",df)
print("-"*50)
df=df.drop('b', axis=0)
nombre=['Ariel','Ana','Juan','Mariela','Pedro','Vicky']
apellido=['Garcia','Perez','Gonzalez','Franco','Fernandez','Klein']
edad=[18,19,20,21,19,18]
indice=["A","B","C","D","E","F"]
nota1=[7,8,9,7,8,9]
nota2=[3,8,7,3,8,7]
final=[5,8,8,5,8,8]
clase = {'nombre':nombre, 'apellido':apellido, 'edad':edad, 'indice':indice, 'nota1':nota1, 'nota2':nota2, 'final':final }
df=pd.DataFrame(data=clase,index=indice)

print(f"\nDesde listas a diccionatio a df:\n\n{df}")
#limpiar()
df.plot(kind='line', y='final' , color = 'blue') 
plt.show()
df.plot(kind='scatter', x='final', y='apellido')
plt.show()
pausa()
print("*"*50)
####################################################################################################

df=base.copy()
print ("Original:\n",df)
grupo = df.groupby('uno')['uno'].count()
print("df.groupby('uno')['uno'].count():\n", grupo)
pausa()
print ("Original:\n",df)
grupo = df.groupby('uno')['uno','dos','tres'].plot(kind='line' , color = 'blue') 
plt.show()
pausa()
print("*"*50)

print("df drop fila 'b':\n",df)
pausa()
print("-"*50)
df=df.drop(['c','a'], axis=0)
print("df drop filas 'c' y 'a':\n",df)
pausa()
print("-"*50)
df=df.drop(['dos'], axis=1)
print("df drop colum 'dos':\n",df)
pausa()
print("-"*50)
df=original.copy()
print("df original:\n",df)
pausa()
print("-"*50)
df = df.drop(df.index[[1, 3]], axis=0)  # df.index is zero-based pd.Index 
print("df drop index '1'(d) y '3'(e) :\n",df)
pausa()
print("-"*50)
df = df.drop(df.columns[[0, 1]], axis=1)  # df.columns is zero-based pd.Index 
print("df drop colum '0' y '1':\n",df)
pausa()
# ~ limpiar()
print("*"*50)

####################################################################################################
df=original.copy()
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║             pop extraigo y remuevo columna en el lugar deseado              ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
print("df original:\n",df)
print("-"*50)
dfpop= df.pop("uno")
print ("df.pop:\n",dfpop)
print("df cambio:\n",df)
pausa()
limpiar()
print("*"*50)

####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                    sort ordenar por columna o index                         ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
dict_series = {
                'uno' :[1,28,63,0],
                'dos'   :[2,12,53,1],
                'tres'  :[3,22,43,2],
                'cuatro':[4,32,33,5],
                'cinco' :[5,52,23,3],
                'seis'  :[6,42,13,4],
                'siete' :[7,22,73,6],
                'ocho'  :[8,12,np.nan,5],
                'nueve' :[9,21,np.nan,4],
                'diez'  :[10,31,100,6],
                }
df= pd.DataFrame(data=dict_series, index=['a', 'b', 'c', 'd'])
df= df.copy()
####################################################################################################
print("df original:\n",df)
pausa()
print("-"*50)
####################################################################################################
df = df.sort_values(by='dos')
print("df df.sort_values(by='dos'):\n",df)
pausa()
print("-"*50)
####################################################################################################
df = df.sort_values(by='dos' , ascending=False)
print("df df.sort_values(by='dos', ascending=False):\n",df)
pausa()
print("-"*50)
####################################################################################################
df = df.sort_values(by='ocho' , na_position='first')
#df.sort_values(by="ocho", ascending = True, na_position ='last')
print("df df.sort_values(by='ocho' , na_position='first') :\n",df)
pausa()
print("-"*50)
####################################################################################################
df = df.sort_values(by=['uno','tres'])
print("df df.sort_values(by=['uno','tres']):\n",df)
pausa()
print("-"*50)
####################################################################################################
df = df.sort_values(by=['uno','tres'], ascending=[False,True])
print("df df.sort_values(by=['uno','tres'], ascending=[False,True]):\n",df)
pausa()
print("-"*50)
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
df = df.sort_index()
print("df df.sort_index():\n",df)
pausa()
print("-"*50)
####################################################################################################
df = df.sort_index(ascending=False)
print("df df.sort_index(ascending=False):\n",df)
pausa()
print("-"*50)
####################################################################################################
df=df.reset_index()
df = df.sort_index()
print("df.reset_index() // df.sort_index():\n",df)
pausa()
print("-"*50)
####################################################################################################
df.index=['I','II','III','IV']
df = df.sort_index()
print("df.index=['I','II','III','IV'] // df.sort_index():\n",df)
pausa()
print("-"*50)
####################################################################################################
df= df.copy()
df.index=[1,2,3,4]
print("df original:\n",df)
pausa()
print("-"*50)
####################################################################################################
df = pd.DataFrame.from_dict({
                             "500 Club"      : ["Bar"       ,  34.64],
                             "Liho Liho"     : ["Restaurant", 200.45], 
                             "Foreign Cinema": ["Restaurant", 180.45],
                             "The Square"    : ["Bar"       ,  45.54]
                            }, orient='index', columns=['tipo', 'total'])
df.sort_values(by=['tipo', 'total'], ascending=[True, False])
print("df.sort_values(by=['tipo', 'total'], ascending=[True, False]):\n",df)

pausa()
print("-"*50)
####################################################################################################

dict_series = {
                'col1' :[np.nan,28,63,0],
                'col2' :[1,12,53,0],
                'col3' :[3,34,43,2],
                'col4' :[4,32,33,5],
                'col5' :[5,None,23,3],
                'col6' :[6,42,13,6],
                'col7' :[5,22,73,6],
                'col8' :[4,32,26,5],
                'col9' :[3,21,np.nan,4],
                'col10':[1,31,11,0],
                }
df = pd.DataFrame(data=dict_series, index=['a', 'b', 'c', 'd'])
print("df original:\n",df)
print("-"*50)
print("df.sort_values(by='col7', axis=0):\n",df.sort_values(by='col7', axis=0))
pausa()
print("-"*50)
print("df.sort_values(by='a', axis=1):\n",df.sort_values(by='a', axis=1))
pausa()
print("-"*50)
print("df.sort_values(by='a', axis=1, ascending=False)):\n",df.sort_values(by='a', axis=1, ascending=False))
pausa()
print("-"*50)
print("df.sort_values(by=['col1','col2','col3'], axis=0):\n",df.sort_values(by=['col1','col2','col3'], axis=0))
print('primero hago un sort por col1, de los que sean iguales selecciono por col2 luego si son iguales selecciono por col1 ')
pausa()
print("-"*50)
print("df.sort_values(by='c', axis=1):\n",df.sort_values(by='c', axis=1))
pausa()
print("-"*50)
print("df.sort_values(by=['a','b','c'], axis=1):\n",df.sort_values(by=['a','b','c'], axis=1))
print('primero hago un sort por a, de los que sean iguales selecciono por b luego si son iguales selecciono por c ')
pausa()
print("-"*50)
print("df.sort_values(by='col9', axis=0,na_position='first'):\n",df.sort_values(by='col9', axis=0,na_position='first'))

pausa()
print("-"*50)
print("df.sort_values(by='col4', inplace=True):\n",df.sort_values(by='col4' , inplace=True))#inplace : If True, perform operation in-place in Dataframe

pausa()
print("-"*50)
print("df.sort_values(by='b', axis=1, ascending=False):\n",df.sort_values(by='b', axis=1, ascending=False),"\n")
#https://thispointer.com/pandas-sort-rows-or-columns-in-df-based-on-values-using-df-sort_values/
pausa()
print("*"*50)
####################################################################################################

pausa()
limpiar()
print("*"*50)

####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                            to_numpy refresh                                 ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
####################################################################################################
#		https://www.youtube.com/watch?v=bmM_RhjuT3k
df = original.copy()
print("df cambio:\n",df)
df["uno"] =df.uno.astype(float)
df["dos"] =df.dos.astype(float)
df["tres"]=df.dos.astype(float)


print ("paso a paso. Ya llegaremos a numpy")
aNumpy= df.to_numpy()
print("pasamos nuestro Dataframe a un array Numpy",aNumpy)
print("-"*50)
aNumpy= df[['uno']].to_numpy()
funcion=lambda dato: dato**2
aNumpy=funcion(aNumpy)
print("pasamos una columna del Dataframe a un array Numpy",aNumpy)
df.loc[:,'Cuadrado UNO']=aNumpy
print("df.cuadrado columna:\n",df)
pausa()
limpiar()
print("*"*50)
####################################################################################################
for x in df.index:
    print("df.index:",x,df.loc[x,"uno"],df.loc[x,"dos"])
    
    if df.loc[x,"uno"]>df.loc[x,"dos"]:
        df.loc[x,"mayor"]=df.loc[x,"uno"]
        print ("cambio mayor x uno")
    else:
        df.loc[x,"mayor"]=df.loc[x,"dos"]
        print ("cambio mayor x dos")
print("-"*50)
print("df.mayor columna:\n",df)
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("creo un datafreme desde numpy con dtypes predeterminados")
dtypes = [('dato_num_1','float64'),('dato_num_2','float32'),('dato_num_3','int'),('dato_num_4','int32')]
array_1=np.zeros(15,dtype=dtypes)
print("array_1:\n",array_1, array_1.dtype)
indices = ['index{}'.format(i) for i in range (1 , len(array_1)+1)]
df =pd.DataFrame(data=array_1, index= indices)
print ("df creado:\n",df)
pausa()
limpiar()
print("*"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                 juguemos                                    ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
print("Juguemos........................")
cantidad = 24
#cambiar
df_1 = pd.DataFrame(data={"Genero": np.random.choice(["M", "F"], size=cantidad), "Edad": np.random.randint(0, 100, size=cantidad)})

#cambiar x este
# ~ df_1 = pd.DataFrame(data=
                            # ~ {
                            # ~ "Genero":["M", "F" , "M", "F", "F", "F", "F"],
                            # ~ "Edad":[18, 15, 20, 9, 28, 2, 56]
                            # ~ })
print ("Boliche:\n",df_1)
print("*"*50)
print ("Boliche Edad:\n",df_1['Edad'] >= 18)
print ("Boliche Edad:\n",df_1[df_1['Edad'] >= 18]['Genero'])
pausa()
limpiar()
print("*"*50)
df_1["Boliche"] = df_1.apply(lambda x: "Menor" if x["Edad"] < 18 else x["Genero"], axis=1)
print ("Boliche Edad:\n",df_1["Boliche"])
pausa()
limpiar()
print("*"*50)
####################################################################################################

df = pd.DataFrame(data=
                    {
                        'turno':	["M","M","M","M","M","M","T","T","T","T"],
                        'nombre': 	['Juan', 'Ricardo', 'Ana', 'Luis', 'Laura', 'Marta', 'Andrea', 'Jose', 'Pedro', 'Ines'],
                        'apellido': ['Perez', 'Garcia', 'Gonzalez', 'Gomez', 'Lujan', 'Martinez', 'Molina', 'Costa', 'Gilar', 'Mendez'],
                        'puesto':	['Administracion', 'Marketing', 'Contable', 'Produccion', 'Mantenimiento', 'Produccion','Produccion', 'Mantenimiento', 'Produccion', 'Mantenimiento'],
                        'nota_1C':	[10,9,5,7,8,9,6,7,8,9],
                        'nota_2C':	[8,9,10,9,5,7,8,9,6,7],
                        'Final':	[9,6,7,8,9,10,9,5,7,8]
                    }, 
                    columns=['turno','nombre', 'apellido', 'puesto','nota_1C','nota_2C','Final'], 
                    )

print (f"\n\n{df}\n")
pausa()
limpiar()
print("*"*50)
####################################################################################################
df['index']=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]#le agregamos un index numérico
#df.set_index("index",inplace=True)	#actualizamos el inice de busqueda
df = df.set_index('index')#actualizamos el inice de busqueda
print (f"df.set_index('index')\n{df}\n")
print (f"df.loc[1,2,3,4]\n{df.loc[[1,2,3,4]]}\n")
pausa()
limpiar()
print("*"*50)
df = df.set_index("Final")#actualizamos el inice de busqueda
print (f"df.set_index('Final')\n{df}\n")
pausa()
limpiar()
print("*"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                              df['turno'].count())                           ║
║                              df['turno'].nunique())                         ║
║                              df['turno'].unique())                          ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
df_turno_M=df.loc[(df['turno']=='M')]
df_turno_T=df.loc[(df['turno']=='T')]
print ("\n\ndf_turno_Mañana:\n:",df_turno_M)
print("-"*50)
print ("\n\ndf_turno_Tarde:\n:",df_turno_T)
print("*"*50)
####################################################################################################
pausa()
print("-"*50)
print ("\n\ndf_cantidad turno:",df['turno'].count())
print("-"*50)
print ("\n\ndf_Unicos turno:" , df['turno'].unique())
####################################################################################################
pausa()
print("-"*50)
print ("\n\ndf_cant-Unicos  axis=1:\n",df.nunique(axis=1))
####################################################################################################
pausa()
print("-"*50)
print ("\n\ndf_cant-Unicos  axis=0:\n",df.nunique(axis=0))
print("-"*50)
####################################################################################################
pausa()
limpiar()
print("*"*50)
####################################################################################################
print ("\n\ndf_turno_Mañana:\n:",df[(df['turno']=='M')].iloc[:]['nombre'])
print("*"*50)
print ("\n\ndf_turno_Tarde:\n:" ,df[(df['turno']=='T')].iloc[:]['nombre'])
pausa()
limpiar()
print("*"*50)
####################################################################################################
print ("\n\ndf_turno_MC:\n:turno mañana:",df.loc[(df['turno']=='M')].count()['turno'])
print("*"*50)
print ("\n\ndf_turno_TC:\n:turno tarde :",df.loc[(df['turno']=='T')].count()['turno'])
pausa()
limpiar()
print("*"*50)
####################################################################################################
df=df.reset_index()
# ~ df = df.reset_index(level=0)
df_aprobado=df.loc[(df['nota_1C']>=7)&(df['nota_2C']>=7)]

print ("\n\df_aprobado:\n",df_aprobado,"\nindex/final")
pausa()
print("-"*50)
print ("\n\df_aprobado:\n",df.loc[(df['nota_1C']>=7)&(df['nota_2C']>=7)]['Final'])
pausa()
print("-"*50)
print ("\n\df_aprobado:\n",df.loc[(df['nota_1C']>=7)&(df['nota_2C']>=7)]['nombre'])
pausa()
print("-"*50)
print ("\n\df_aprobado:\n",df.loc[(df['nota_1C']>=7)&(df['nota_2C']>=7)][['Final','nombre','apellido','turno']])
pausa()
limpiar()
print("*"*50)
####################################################################################################
df['promedio'] = (df ['nota_1C']+df ['nota_2C'])/2
print (f"\nnueva columna df['promedio']\n{df}\n")
pausa()
limpiar()
print("*"*50)
####################################################################################################

print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                               Correlacion                                   ║
║                       df['final'].corr(df['promedio'])                      ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
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
#My_dic= {'cero':[0,'zero'],'uno':[1,'one'],'dos':[2,'two'],'tres':[3,'three'],'cuatro':[4,'four'],'cinco':[5,'five'],'seis':[6,'six'],'siete':[7,'seven'],'ocho':[8,'eight'],'nueve':[9,'nine'],'diez':[10,'ten']}
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                               Correlacion                                   ║
║                       df['final'].corr(df['promedio'])                      ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
print("""
                    DataFrame.add		        Add DataFrames.
                    DataFrame.sub		        Subtract DataFrames.
                    DataFrame.mul		        Nultiply DataFrames.
                    DataFrame.div		        Divide DataFrames (float division).
                    DataFrame.truediv	        Divide DataFrames (float division).
                    DataFrame.floordiv	        Divide DataFrames (integer division).
                    DataFrame.mod		        Calculate modulo (remainder after division).
                    DataFrame.pow		        Calculate exponential power.
""")
My_dic= {'A':[0,50],'B':[1,51],'C':[2,52],'D':[3,53],'E':[4,54],'F':[5,55],'G':[6,56],'H':[7,57],'I':[8,58],'J':[9,59],'K':[10,60]}
#df = pd.DataFrame ([My_dic])
#df = pd.DataFrame(data=list(My_dic.items()),columnas = ['columna1','columna2']) 
df = pd.DataFrame.from_dict(My_dic, orient ='index')   
print (f"\n\noriginal:\n{df}\n")
print("*"*50)
####################################################################################################
print("df.mean() Muestra el promedio de cada columna.")
print (f"\ndf.mean()\n{df.mean()}\n")
pausa()
#limpiar()
print("*"*50)
####################################################################################################
print("df.add(100) Agrega un escalar(100) con la versión del operador que devuelve los mismos resultados.")
print (f"\n\n{df.add(100)}\n")
pausa()
#limpiar()
print("*"*50)
####################################################################################################
print("df.div(2) Dividir por constante con versión inversa")
print (f"\n\n{df.div(2)}\n")
pausa()
#limpiar()
print("*"*50)
####################################################################################################
print("df.rdiv(2) Restar una lista y una serie por eje con la versión del operador.")
print("Get Floating division of df and other, element-wise (binary operator rtruediv).")
print (f"\n\n{df.rdiv(2)}\n")
print("?????????????????????????")
pausa()
#limpiar()
print("*"*50)
####################################################################################################
print ("\n\n{df - [1, 25]} resto la lista cada valor en su columna\n")
print (f"\n\n{df}\n")
print (f"\ndf - [1, 25]\n{df - [1, 25]}\n")
#               o
print ("\n\n{df.sub([1, 25], axis='columnas')}\n")
print (f"\n\n{df.sub([1, 25], axis='columns')}\n")
pausa()
limpiar()
print("*"*50)
####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                         plot  un ejemplo de un grafico                      ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
####################################################################################################


df=original.copy()
print ("Original:\n",df)
df=df[['uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez']].astype(int)
print ("original:\n",df,'\n',df.dtypes )
df.plot() 
plt.show()
pausa()
print("*"*50)
####################################################################################################

My_dic= {'cero':0,'uno':1,'dos':2,'tres':3,'cuatro':4,'cinco':5,'seis':6,'siete':7,'ocho':8,'nueve':9,'diez':10}
df=pd.DataFrame(data=My_dic ,index=['uno'])
df=df.T
print (df)
df['Final']=df.loc[:,'uno']*8
print (df)
df.Final.plot(kind='pie',labels=My_dic.keys())

pausa()
limpiar()
print("*"*50)
####################################################################################################
nombre=['Ariel','Ana','Juan','Mariela','Pedro','Vicky']
apellido=['Garcia','Perez','Gonzalez','Franco','Fernandez','Klein']
edad=[18,19,20,21,19,18]
indice=["A","B","C","D","E","F"]
nota1=[7,8,9,7,8,9]
nota2=[3,8,7,3,8,7]
final=[5,8,8,5,8,8]
clase = {'nombre':nombre, 'apellido':apellido, 'edad':edad, 'indice':indice, 'nota1':nota1, 'nota2':nota2, 'final':final }
df=pd.DataFrame(data=clase,index=indice)

print(f"\nDesde listas a diccionatio a df:\n\n{df}")
#limpiar()
df.plot(kind='line', y='final' , color = 'blue') 
plt.show()
df.plot(kind='scatter', x='final', y='apellido')
plt.show()
pausa()
print("*"*50)
####################################################################################################

df=base.copy()
print ("Original:\n",df)
grupo = df.groupby('uno')['uno'].count()
print("df.groupby('uno')['uno'].count():\n", grupo)
pausa()
print ("Original:\n",df)
grupo = df.groupby('uno')['uno','dos','tres'].plot(kind='line' , color = 'blue') 
plt.show()
pausa()
print("*"*50)
####################################################################################################
df = pd.DataFrame(data=
                    {
                        'turno':	["M","M","M","M","M","M","T","T","T","T"],
                        'nombre': 	['Juan', 'Ricardo', 'Ana', 'Luis', 'Laura', 'Marta', 'Andrea', 'Jose', 'Pedro', 'Ines'],
                        'apellido': ['Perez', 'Garcia', 'Gonzalez', 'Gomez', 'Lujan', 'Martinez', 'Molina', 'Costa', 'Gilar', 'Mendez'],
                        'puesto':	['Administracion', 'Marketing', 'Contable', 'Produccion', 'Mantenimiento', 'Produccion','Produccion', 'Mantenimiento', 'Produccion', 'Mantenimiento'],
                        'nota_1C':	[10,9,5,7,8,9,6,7,8,9],
                        'nota_2C':	[8,9,10,9,5,7,8,9,6,7],
                        'Final':	[9,6,7,8,9,10,9,5,7,8]
                    }, 
                    columns=['turno','nombre', 'apellido', 'puesto','nota_1C','nota_2C','Final'], 
                    )
print ("Original:\n",df)
grupo4 = df.groupby('turno')[['nota_1C','nota_2C']].mean()
print("grupo = df.groupby('turno').Final.mean():\n", grupo4)
grupo = df.groupby('turno')['nota_1C','nota_2C'].plot(kind='line' , color = 'blue') 
plt.show()
pausa()
print("*"*50)
####################################################################################################
print("""
DataFrame.plot is both a callable method and a namespace attribute for specific plotting methods of the form DataFrame.plot.<kind>.
DataFrame.plot([x, y, kind, ax, ….])	DataFrame plotting accessor and method
DataFrame.plot.area(self[, x, y])	Draw a stacked area plot.
DataFrame.plot.bar(self[, x, y])	Vertical bar plot.
DataFrame.plot.barh(self[, x, y])	Make a horizontal bar plot.
DataFrame.plot.box(self[, by])	Make a box plot of the DataFrame columns.
DataFrame.plot.density(self[, bw_method, ind])	Generate Kernel Density Estimate plot using Gaussian kernels.
DataFrame.plot.hexbin(self, x, y[, C, …])	Generate a hexagonal binning plot.
DataFrame.plot.hist(self[, by, bins])	Draw one histogram of the DataFrame’s columns.
DataFrame.plot.kde(self[, bw_method, ind])	Generate Kernel Density Estimate plot using Gaussian kernels.
DataFrame.plot.line(self[, x, y])	Plot Series or DataFrame as lines.
DataFrame.plot.pie(self, \*\*kwargs)	Generate a pie plot.
DataFrame.plot.scatter(self, x, y[, s, c])	Create a scatter plot with varying marker point size and color.
DataFrame.boxplot(self[, column, by, ax, …])	Make a box plot from DataFrame columns.
DataFrame.hist(data[, column, by, grid, …])	Make a histogram of the DataFrame’s.""")
limpiar()
