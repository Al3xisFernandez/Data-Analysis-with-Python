from __init__ import *
import pandas as pd
def ya_hechos():
    pass
    print ("inicio")
    
    

print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                             Pandas Series                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                            Attributes (11)                                  ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m 

array                                                   El ExtensionArray de los datos que respaldan esta serie o índice.at                                                      Acceda a un solo valor para un par de etiquetas de fila/columna.attrs                                                   Diccionario de atributos globales de este conjunto de datos.axes                                                    Devuelve una lista de las etiquetas del eje de fila.dtype                                                   Devuelve el objeto dtype de los datos subyacentes.dtypes                                                  Devuelve el objeto dtype de los datos subyacentes.flags                                                   Obtenga las propiedades asociadas con este objeto pandas.hasnans                                                 Devuelve True si hay NaN.iat                                                     Acceda a un valor único para un par de filas/columnas por posición de número entero.iloc                                                    Indexación puramente basada en la ubicación de enteros para la selección por posición.index                                                   El índice (etiquetas de eje) de la Serie.is_monotonic_decreasing                                 Retorna booleano si los valores en el objeto están decreciendo monótonamente.is_monotonic_increasing                                 Devuelve booleano si los valores en el objeto aumentan monótonamente.is_unique                                               Retorna booleano si los valores en el objeto son únicos.loc                                                     Acceda a un grupo de filas y columnas por etiqueta(s) o una matriz booleana.name                                                    Devuelve el nombre de la Serie.nbytes                                                  Devuelve el número de bytes en los datos subyacentes.ndim                                                    Número de dimensiones de los datos subyacentes, por definición 1.shape                                                   Devuelve una tupla de la forma de los datos subyacentes.size                                                    Devuelve el número de elementos en los datos subyacentes.values                                                  Devuelve Series como ndarray o similar a ndarray dependiendo del tipo de d.T                                                       Devuelve el DF Transpuesto (filas x columnas y columnas x filas) .""")
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                             Pandas Series                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                             Methods (191)                                   ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m 
abs()                                                   Devuelve una serie/marco de datos con el valor numérico absoluto de cada elemento.add(otro[, nivel, valor_de_relleno, eje])               Retorno Suma de series y otras, por elementos (operador binario sumar ).add_prefix(prefijo)                                     Etiquetas de prefijo con prefijo de cadena .add_suffix(sufijo)                                      Etiquetas de sufijo con sufijo de cadenaagg([función, eje])                                     Agregue usando una o más operaciones sobre el eje especificado.aggregate([función, eje])                               Agregue usando una o más operaciones sobre el eje especificado.align(otro[, unión, eje, nivel, copia, ...])            Alinee dos objetos en sus ejes con el método de unión especificado.all([eje, bool_only, skipna, nivel])                    Devuelve si todos los elementos son verdaderos, potencialmente sobre un eje.any(*[, eje, bool_only, skipna, nivel])                 Devuelve si algún elemento es Verdadero, potencialmente sobre un eje.apply(func[, convert_dtype, args])                      Invocar función en valores de Series.argmax([eje, skipna])                                   Devuelve la posición int del mayor valor de la Serie.argmin([eje, skipna])                                   Devuelve la posición int del valor más pequeño de la Serie.argsort([eje, tipo, orden])                             Devuelve los índices enteros que ordenarían los valores de Serie.asfreq(frecuencia[, método, cómo, normalizar, ...])     Convierte series de tiempo a la frecuencia especificada.asof(donde[, subconjunto])                              Devuelve la(s) última(s) fila(s) sin NaN antes de where .astype(dtype[, copiar, errores])                        Transmita un objeto pandas a un tipo de d especificado dtype.at_time(tiempo[, a partir de, eje])                     Seleccione valores a una hora determinada del día (p. ej., 9:30 a. m.).autocorr([retraso])                                     Calcule la autocorrelación lag-N.backfill(*[, eje, en el lugar, límite, abatido])        Sinónimo de DataFrame.fillna()con method='bfill'.between(izquierda, derecha[, inclusive])                Devuelve la serie booleana equivalente a la izquierda <= serie <= derecha.between_time(hora_inicio, hora_fin[, ...])              Seleccione valores entre momentos particulares del día (p. ej., 9:00-9:30 a. m.).bfill(*[, eje, en el lugar, límite, abatido])           Sinónimo de DataFrame.fillna()con method='bfill'.bool()                                                  Devuelve el valor booleano de un solo elemento Series o DataFrame.cat                                                     alias depandas.core.arrays.categorical.CategoricalAccessorclip([inferior, superior, eje, en su lugar])            Ajuste los valores en los umbrales de entrada.combine(otro, func[, fill_value])                       Combinar la Serie con una Serie o escalar según func .combine_first(otro)                                     Actualizar elementos nulos con valor en la misma ubicación en 'otro'.compare(otro[, alinear_eje, mantener_forma, ...])       Compare con otra Serie y muestre las diferencias.convert_dtypes([objetos_inferidos, ...])                Convierta columnas a los mejores dtypes posibles usando dtypes compatibles con pd.NA.copy([profundo])                                        Haga una copia de los índices y datos de este objeto.corr(otro[, método, min_periods])                       Calcule la correlación con otras series, excluyendo los valores faltantes.count([nivel])                                          Devuelve el número de observaciones no NA/nulas en la Serie.cov(otro[, min_períodos, dof])                          Calcule la covarianza con Serie, excluyendo los valores faltantes.cummax([eje, skipna])                                   Devuelve el máximo acumulativo sobre un eje DataFrame o Series.cummin([eje, skipna])                                   Devuelve el mínimo acumulativo sobre un eje DataFrame o Series.cumprod([eje, skipna])                                  Devuelve el producto acumulativo sobre un eje DataFrame o Series.cumsum([eje, skipna])                                   Devuelve la suma acumulada sobre un eje DataFrame o Series.describe([percentiles, incluir, excluir, ...])          Genera estadísticas descriptivas.iff([puntos])                                           Primera diferencia discreta de elemento.div(otro[, nivel, valor_de_relleno, eje])               Retorna División flotante de series y otras, por elementos (operador binario truediv ).divide(otro[, nivel, valor_de_relleno, eje])            Retorna División flotante de series y otras, por elementos (operador binario truediv ).divmod(otro[, nivel, valor_de_relleno, eje])            Devuelve la división de enteros y el módulo de series y otros elementos (operador binario divmod ).dot(otro)                                               Calcule el producto escalar entre la Serie y las columnas de otra.drop([etiquetas, eje, índice, columnas, nivel, ...])    Serie de retorno con las etiquetas de índice especificadas eliminadas.drop_duplicates(*[, mantener, en su lugar])             Serie de retorno con valores duplicados eliminados.droplevel(nivel[, eje])                                 Devolver serie/marco de datos con el índice o los niveles de columna solicitados eliminados.dropna(*[, eje, en el lugar, cómo])                     Devuelve una nueva serie con los valores faltantes eliminados.dt                                                      alias depandas.core.indexes.accessors.CombinedDatetimelikePropertiesduplicated([mantener])                                  Indique valores de serie duplicados.eq(otro[, nivel, valor_de_relleno, eje])                Retorna Igual a de serie y otro, elemento-sabio (operador binario eq ).equals(otro)                                            Prueba si dos objetos contienen los mismos elementos.ewm([com, intervalo, vida media, alfa, ...])            Proporcione cálculos ponderados exponencialmente (EW).expanding([min_periods, centro, eje, método])           Proporcionar cálculos de ventana en expansión.explode([ignorar_índice])                               Transforma cada elemento de una lista como una fila.factorize([clasificar, a_centinela, usar_a_centinela])  Codifique el objeto como un tipo enumerado o una variable categórica.ffill(*[, eje, en el lugar, límite, abatido])           Sinónimo de DataFrame.fillna()con method='ffill'.fillna([valor, método, eje, en el lugar, ...])          Rellene los valores NA/NaN utilizando el método especificado.filter([elementos, me gusta, expresión regular, eje])   Subconjunto de las filas o columnas del marco de datos de acuerdo con las etiquetas de índice especificadas.first(compensar)                                        Seleccione períodos iniciales de datos de series temporales en función de un desplazamiento de fecha.first_valid_index()                                     Índice de retorno para el primer valor no NA o Ninguno, si no se encuentra ningún valor no NA.floordiv(otro[, nivel, valor_de_relleno, eje])          Devuelve la división entera de series y otras, por elementos (operador binario floordiv ).ge(otro[, nivel, valor_de_relleno, eje])                Devuelve Mayor o igual que de series y otros, por elementos (operador binario ge ).get(clave[, predeterminado])                            Obtenga el elemento del objeto para la clave dada (por ejemplo: columna DataFrame).groupby([por, eje, nivel, as_index, ordenar, ...])      Serie de grupos usando un mapeador o por una Serie de columnas.gt(otro[, nivel, valor_de_relleno, eje])                Devuelve Mayor que de serie y otro, elemento-sabio (operador binario gt ).head([norte])                                           Devuelve las primeras n filas.hist([por, hacha, rejilla, xlabelsize, xrot, ...])      Dibuje el histograma de la serie de entrada usando matplotlib.idxmax([eje, skipna])                                   Devuelve la etiqueta de fila del valor máximo.idxmin([eje, skipna])                                   Devuelve la etiqueta de la fila del valor mínimo.infer_objects()                                         Intente inferir mejores dtypes para columnas de objetos.info([verbose, buf, max_cols, memory_usage, ...])       Imprime un resumen conciso de una Serie.interpolate([método, eje, límite, en el lugar, ...])    Rellene los valores de NaN utilizando un método de interpolación.isin(valores)                                           Si los elementos de Series están contenidos en valores .isna()                                                  Detectar valores faltantes.isnull()                                                Series.isnull es un alias de Series.isna.item()                                                  Devuelve el primer elemento de los datos subyacentes como un escalar de Python.items()                                                 Iterar perezosamente sobre tuplas (índice, valor).keys()                                                  Devuelve el alias para index.kurt([eje, skipna, nivel, numeric_only])                Devuelve la curtosis imparcial sobre el eje solicitado.kurtosis([eje, skipna, nivel, numeric_only])            Devuelve la curtosis imparcial sobre el eje solicitado.last(compensar)                                         Seleccione períodos finales de datos de series temporales en función de un desplazamiento de fecha.last_valid_index()                                      Índice de retorno para el último valor no NA o Ninguno, si no se encuentra ningún valor no NA.le(otro[, nivel, valor_de_relleno, eje])                Devuelve Menor o igual que de serie y otros elementos (operador binario le ).lt(otro[, nivel, valor_de_relleno, eje])                Retorna Menos que de serie y otro, por elementos (operador binario lt ).map(arg[, na_action])                                   Asigne valores de Serie de acuerdo con una función o asignación de entrada.mask(cond[, otro, en el lugar, eje, nivel, ...])        Reemplace los valores donde la condición sea Verdadera.max([eje, skipna, nivel, numeric_only])                 Devuelve el máximo de los valores sobre el eje solicitado.mean([eje, skipna, nivel, numeric_only])                Devuelve la media de los valores sobre el eje solicitado.median([eje, skipna, nivel, numeric_only])              Devuelve la mediana de los valores sobre el eje solicitado.memory_usage([índice, profundo])                        Devuelve el uso de memoria de la Serie.min([eje, skipna, nivel, numeric_only])                 Devuelve el mínimo de los valores sobre el eje solicitado.mod(otro[, nivel, valor_de_relleno, eje])               Módulo de retorno de serie y otros, por elementos (operador binario mod ).mode([caer])                                            Devuelve el(los) modo(s) de la Serie.mul(otro[, nivel, valor_de_relleno, eje])               Retorno Multiplicación de series y otras, por elementos (operador binario mul ).multiply(otro[, nivel, valor_de_relleno, eje])          Retorno Multiplicación de series y otras, por elementos (operador binario mul ).ne(otro[, nivel, valor_de_relleno, eje])                Retorna No es igual a de serie y otra, elemento-sabio (operador binario ne ).nlargest([n, mantener])                                 Devuelve los n elementos más grandes.notna()                                                 Detectar valores existentes (no perdidos).notnull()                                               Series.notnull es un alias de Series.notna.nsmallest([n, mantener])                                Devuelve los n elementos más pequeños.nunique([caer])                                         Devuelve el número de elementos únicos en el objeto.pad(*[, eje, en el lugar, límite, abatido])             Sinónimo de DataFrame.fillna()con method='ffill'.pct_change([períodos, método_relleno, límite, frec])    Cambio porcentual entre el elemento actual y el anterior.pipe(función, *args, **kwargs)                          Aplicar funciones encadenables que esperan Series o DataFrames.plot                                                    alias depandas.plotting._core.PlotAccessorpop(artículo)                                           Devolver artículo y gotas de serie.pow(otro[, nivel, valor_de_relleno, eje])               Retorno Potencia exponencial de serie y otra, por elementos (operador binario pow ).prod([eje, skipna, nivel, numeric_only, ...])           Devuelve el producto de los valores sobre el eje solicitado.product([eje, skipna, nivel, numeric_only, ...])        Devuelve el producto de los valores sobre el eje solicitado.quantile([q, interpolación])                            Valor de retorno en el cuantil dado.radd(otro[, nivel, valor_de_relleno, eje])              Retorno Suma de series y otras, por elementos (operador binario radd ).rank([eje, método, numeric_only, ...])                  Calcule rangos de datos numéricos (1 a n) a lo largo del eje.ravel([ordenar])                                        Devuelve los datos subyacentes aplanados como un ndarray.rdiv(otro[, nivel, valor_de_relleno, eje])              Devolver División flotante de series y otras, por elementos (operador binario rtruediv ).rdivmod(otro[, nivel, valor_de_relleno, eje])           Devuelve la división de enteros y el módulo de series y otros elementos (operador binario rdivmod ).reindex(*args, **kwargs)                                Serie conforme al nuevo índice con lógica de llenado opcional.reindex_like(otro[, método, copia, límite, ...])        Devuelve un objeto con índices coincidentes como otro objeto.rename([índice, eje, copia, en el lugar, nivel, ...])   Alterar las etiquetas de índice o el nombre de la serie.rename_axis([carpeta, en el lugar])                     Establezca el nombre del eje para el índice o las columnas.reorder_levels(ordenar)                                 Reorganizar los niveles de índice utilizando el orden de entrada.repeat(repeticiones[, eje])                             Repetir elementos de una Serie.replace([para_reemplazar, valor,lugar, límite, ...])    Reemplace los valores dados en to_replace con value .resample(regla[, eje, cerrado, etiqueta, ...])          Vuelva a muestrear datos de series temporales.reset_index([nivel, gota, nombre, en el lugar, ...])    Genere un nuevo marco de datos o serie con el restablecimiento del índice.rfloordiv(otro[, nivel, valor_de_relleno, eje])         Devuelve la división entera de series y otras, por elementos (operador binario rfloordiv ).rmod(otro[, nivel, valor_de_relleno, eje])              Módulo de retorno de serie y otro, por elementos (operador binario rmod ).rmul(otro[, nivel, valor_de_relleno, eje])              Retorno Multiplicación de series y otras, por elementos (operador binario rmul ).rolling(ventana[, min_períodos, centro, ...])           Proporcione cálculos de ventana móvil.round([decimales])                                      Redondea cada valor de una serie al número dado de decimales.rpow(otro[, nivel, valor_de_relleno, eje])              Retorno Potencia exponencial de serie y otra, por elementos (operador binario rpow ).rsub(otro[, nivel, valor_de_relleno, eje])              Devolver Resta de series y otras, por elementos (operador binario rsub ).rtruediv(otro[, nivel, valor_de_relleno, eje])          Devolver División flotante de series y otras, por elementos (operador binario rtruediv ).sample([n, frac, reemplazar, pesos, ...])               Devuelve una muestra aleatoria de elementos de un eje de objeto.searchsorted(valor[, lado, clasificador])               Encuentre índices donde se deben insertar elementos para mantener el orden.sem([eje, skipna, nivel, dof, numeric_only])            Devuelve el error estándar imparcial de la media sobre el eje solicitado.set_axis(etiquetas, *[, eje, en su lugar, copiar])      Asigne el índice deseado al eje dado.set_flags(*[, copiar, allow_duplicate_labels])          Devuelve un nuevo objeto con banderas actualizadas.shift([períodos, frecuencia, eje, valor_relleno])       Desplace el índice por el número deseado de períodos con una frecuencia de tiempo opcional .skew([eje, skipna, nivel, numeric_only])                Devuelve un sesgo imparcial sobre el eje solicitado.sort_index(*[, eje, nivel, ascendente, ...])            Ordenar series por etiquetas de índice.sort_values(*[, eje, ascendente, en el lugar, ...])     Ordenar por los valores.sparse                                                  alias depandas.core.arrays.sparse.accessor.SparseAccessorsqueeze([eje])                                          Comprime objetos de un eje dimensional en escalares.std([eje, skipna, nivel, dof, numeric_only])            Devuelve la desviación estándar de la muestra sobre el eje solicitado.str                                                     alias depandas.core.strings.accessor.StringMethodssub(otro[, nivel, valor_de_relleno, eje])               Retorno Resta de series y otros, por elementos (operador binario sub ).subtract(otro[, nivel, valor_de_relleno, eje])          Retorno Resta de series y otros, por elementos (operador binario sub ).sum([eje, skipna, nivel, numeric_only, ...])            Devuelve la suma de los valores sobre el eje solicitado.swapaxes(eje1, eje2[, copiar])                          Intercambie ejes e intercambie ejes de valores apropiadamente.swaplevel([i, j, copiar])                               Intercambie los niveles i y j en a MultiIndex.tail([norte])                                           Devuelve las últimas n filas.take(índices[, eje, es_copia])                          Devuelve los elementos en los índices posicionales dados a lo largo de un eje.to_clipboard([sobresalir, septiembre])                  Copie el objeto al portapapeles del sistema.to_csv([ruta_o_buf, sep, na_rep, ...])                  Escriba el objeto en un archivo de valores separados por comas (csv).to_dict([en])                                           Convierta Series en {etiqueta -> valor} dict u objeto similar a dict.to_excel(excel_writer[, sheet_name, na_rep, ...])       Escribir objeto en una hoja de Excel.to_frame([nombre])                                      Convertir Serie a DataFrame.to_hdf(path_or_buf, key[, mode, complevel, ...])        Escriba los datos contenidos en un archivo HDF5 usando HDFStore.to_json([path_or_buf, orient, date_format, ...])        Convierta el objeto en una cadena JSON.to_latex([buf, columnas, col_space, encabezado, ...])   Representar objeto en una tabla tabular, longtable o anidada de LaTeX.to_list()                                               Devuelve una lista de los valores.to_markdown([buf, modo, índice, opciones_de_almac])     Imprimir series en formato compatible con Markdown.to_numpy([dtype, copia, na_value])                      Un NumPy ndarray que representa los valores de esta serie o índice.to_period([frecuencia, copia])                          Convierta series de DatetimeIndex a PeriodIndex.to_pickle(ruta[, compresión, protocolo, ...])           Pickle (serializar) objeto para archivar.to_sql(nombre, contra[, esquema, si_existe, ...])       Escriba registros almacenados en un DataFrame en una base de datos SQL.to_string([buf, na_rep, float_format, ...])             Renderice una representación de cadena de la Serie.to_timestamp([frecuencia, cómo, copia])                 Transmitir a DatetimeIndex de marcas de tiempo, al comienzo del período.to_xarray()                                             Devuelve un objeto xarray del objeto pandas.tolist()                                                Devuelve una lista de los valores.transform(función[, eje])                               Llame funca la autoproducción de una serie con la misma forma de eje que la propia.transpose(*args, **kwargs)                              Devuelve la transposición, que es por definición propia.truediv(otro[, nivel, valor_de_relleno, eje])           Retorna División flotante de series y otras, por elementos (operador binario truediv ).truncate([antes, después, eje, copia])                  Trunca una serie o trama de datos antes y después de algún valor de índice.tz_convert(tz[, eje, nivel, copia])                     Convierta el eje tz-aware a la zona horaria de destino.tz_localize(tz[, eje, nivel, copia, ...])               Localice el índice tz-naive de una serie o marco de datos para la zona horaria de destino.unique()                                                Devuelve valores únicos del objeto Serie.unstack([nivel, valor_de_relleno])                      Desapilar, también conocido como pivote, Series con MultiIndex para producir DataFrame.update(otro)                                            Modifique Series en su lugar usando valores de Series pasadas.value_counts([normalizar, ordenar, ascender, ...])      Devuelve una serie que contiene recuentos de valores únicos.var([eje, skipna, nivel, dof, numeric_only])            Devuelve la varianza imparcial sobre el eje solicitado.view([tipod])                                           Cree una nueva vista de la Serie.where(cond[, otro, en el lugar, eje, nivel, ...])       Reemplace los valores donde la condición sea Falsa.xs(clave[, eje, nivel, drop_level])                     Devuelva la sección transversal de la Serie/Marco de datos.





append(para_añadir[, ignorar_índice, ...])              (DEPRECATED) Concatenar dos o más Series
mad([eje, skipna, nivel])                               (DEPRECATED) Devuelve la desviación absoluta media de los valores sobre el eje solicitado.
iteritems()                                             (DEPRECATED) Iterar perezosamente sobre (índice, valor) tuplas.
s_monotonic                                             (DEPRECATED) Devuelve boolean si los valores en el objeto aumentan monótonamente.
slice_shift([puntos, eje])                              (DEPRECATED) Equivalente a turno sin copiar datos.
tshift([períodos, frecuencia, eje])                     (DEPRECATED) Cambia el índice de tiempo, usando la frecuencia del índice si está disponible.                                """)    
    

limpiar()
print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║             generamos series desde vectores  (listas / tuplas)              ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
#################################################################################################
lista_Tupla = [111,33,40404]
print("lista o Tupla:",lista_Tupla)
PD_serie = pd.Series(data = lista_Tupla)
print("objeto:\nindex\n  |  dato\n  |  |\n",PD_serie,"<-------------ver el tipo de dato\n\n")
print("objeto tipo:",type(PD_serie))
print("objeto index:",PD_serie.index)
pausa()
print("-"*50)
print("primeros datos head():\nindex\n  |  dato\n  |  |\n",PD_serie.head(2)) #primeros dos
print("-"*50)
print("datos finales tail():\nindex\n  |  dato\n  |  |\n",PD_serie.tail(2))  #últimos dos
pausa()
print("-"*50)
print("objeto tamaño:--------------------------------->",PD_serie.size)
print("objeto descripcion:\n",PD_serie.describe())
print("-"*50)
print("\nEn el indice 2 hay:",PD_serie[2])
print ("rehacer este ejercicio con tuplas reemplazando [] por ()")

pausa()
print("*"*50)

####################################################################################################

lista = ["A","B","C","D"]

print ("En lugar 2:",lista[2])
PD_serie = pd.Series(lista)
print("objeto:\nindex\n  |  dato\n  |  |\n",PD_serie,"<-------------ver el tipo de dato\n\n")
pausa()
print("-"*50)
print("objeto tipo:",type(PD_serie))
print("objeto index:",PD_serie.index)
print("objeto tamaño:",PD_serie.size)
print("objeto descripcion:\n",PD_serie.describe())
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                      generamos series desde diccionarios                    ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
dict_ = {
        'uno' : 200,
        'dos' : 97,
        'tres' : 3,
        'cuatro' :230,
        'cinco' : 5.9999999900000000000000000000000000000009,
        'seis' :  89,
        'siete' : 3,
        'ocho' :  8,
        'nueve' : 280,
        'diez' : 10,
        'once' : 8.79,
        'doce' : 4.9,
        'trece' : 320,
        'catorce' : 9999914,
        }
original= PD_serie.copy()
PD_serie = pd.Series(data = dict_, name="datos")
print("objeto:\nindex\n  |\t\tdato\n  |\t\t|\n",PD_serie,"<-------------ver el tipo de dato\n\n")
pausa()
print("-"*50)
print("objeto tipo:",type(PD_serie))
print("objeto desviacion estandar--------------------->:",PD_serie.std())
print("objeto media----------------------------------->:",PD_serie.mean())
print("objeto Minimo---------------------------------->:",PD_serie.min())
print("objeto Maximo---------------------------------->:",PD_serie.max())
print("objeto tamaño---------------------------------->:",PD_serie.size)
tamanion = PD_serie.size
print ("tamanio:",tamanion)
print("objeto descripcion:\n",PD_serie.describe())
print("\n\n\nen el indice 'cuatro' hay:",PD_serie['cuatro'],"<---------el index, referencia del dato, ya no es un numero entero correlativo,\n sino  una clave (key) alfanumerico")
pausa()
PD_serie = pd.Series(data = dict_, name="datos", index =['cuatro', 'ocho', 'trece', 'uno', 'dos', 'tres', 'seis', 'siete', 'diez', 'once', 'doce', 'cinco', 'nueve', 'catorce'])
print("objeto:\nindex\n  |  	dato\n  |	  |\n",PD_serie,"<-------------ver el tipo de dato\n\n")
print("los datos vienen en un orden aleatoreo o definido por alguna relacion")
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                              tipos de datos                                 ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
lista1 = [1, 8, 7, 9]
lista2 = ['8', '3', '7', '5']
lista3 = ['10.9', 2, 'cinco', 'siete']

PD_serie1 = pd.Series(lista1)
PD_serie2 = pd.Series(lista2)
PD_serie3 = pd.Series(lista3)

print("objeto:\nindex\n  |	  dato\n  |	  |\n",PD_serie1,"<-------------ver el tipo de dato\n\n")
print("objeto tipo:", type(PD_serie1))
pausa()
print("-" * 50)
print("objeto descripcion:\n", PD_serie1.describe())
pausa()
print("-" * 50)

####################################################################################################
print("objeto:\nindex\n  |  dato\n  |  |\n",PD_serie2,"<-------------ver el tipo de dato\n\n")
print("objeto tipo:", type(PD_serie2))
pausa()
print("-" * 50)
print("objeto descripcion:\n", PD_serie2.describe())
pausa()
print("-" * 50)

####################################################################################################
print("objeto:\nindex\n  |	  dato\n  |	  |\n",PD_serie3,"<-------------ver el tipo de dato\n\n")
print("objeto tipo:", type(PD_serie3))
print("objeto descripcion:\n", PD_serie3.describe())
pausa()
limpiar()
print("*"*50)
####################################################################################################
PD_serie1 = pd.to_numeric(PD_serie1)
PD_serie2 = pd.to_numeric(PD_serie2)
PD_serie3 = pd.to_numeric(PD_serie3, errors='coerce')#coerce omite los errores
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                   pd.concat                                 ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)

df = pd.concat([PD_serie1,PD_serie2,PD_serie3], sort=False , ignore_index=True)
print(f"df={df}\ntype(df)={type(df)}<-------------ver el tipo de dato\n\n")
print(f"df.describe()={df.describe()}")
# ~ dic = {"uno":1,"dos":2,"tres":3,"cuatro" :4, "cinco":5,"seis":6,  "siete":7  "ocho":8, "nueve":9 , "cero":0}
# ~ for dato in lista_3:
    # ~ if dato in dic.keys():
        # ~ dato = lista_3[dato]		

pausa()
limpiar()
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                   to_numeric                                ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
'''
lista1 = [1, 8, 7, 9]
lista2 = ['8', '3', '7', '5']#string   - str //object
lista3 = ['10', 2, 'cinco', 'siete']#string   - str //object
'''
print("*"*50)
print("objeto:PD_serie1\nindex\n  |	  dato\n  |	  |\n",PD_serie1,"<-------------ver el tipo de dato\n\n")
print("objeto tipo:", type(PD_serie1))
pausa()
print("-" * 50)
print("objeto descripcion:\n", PD_serie1.describe())
pausa()
print("-" * 50)

####################################################################################################
print("objeto:PD_serie2\nindex\n  |  dato\n  |  |\n",PD_serie2,"<-------------ver el tipo de dato\n\n")
print("objeto tipo:", type(PD_serie2))
pausa()
print("-" * 50)
print("objeto descripcion:\n", PD_serie2.describe())
pausa()
print("-" * 50)

####################################################################################################
print("objeto:PD_serie3\nindex\n  |  dato\n  |  |\n",PD_serie3,"<-------------ver el tipo de dato\n\n")
print("objeto tipo:", type(PD_serie3))
pausa()
print("-" * 50)
print("objeto descripcion:\n", PD_serie3.describe())
limpiar()



dict_ = {
        'uno' : 200,
        'dos' : "97",
        'tres' : 3.01,
        'cuatro' :"230",
        'cinco' : 5.99999999,
        'seis' :  -89,
        'siete' : 3,
        'ocho' :  -8,
        'nueve' : 28.0,
        'diez' : None,
        'once' : 8.79,
        'doce' : 4.9,
        'trece' : '8',
        'catorce' : 9999914,
        }
print (f"{dict_=}")
original = pd.Series(data = dict_, name="datos")


####################################################################################################

PD_serie=original.copy()
print (f"Original:\n",PD_serie,"<-------------ver el tipo de dato\n\n")
print("serie.describe:\n",PD_serie.describe())
print("serie.dtypes:\n",PD_serie.dtypes)
PD_serie=PD_serie.astype(int, errors='ignore')

pausa()
print("-"*50)
print("serie: con los datos cambiados x astype() \n",PD_serie,"<-------------ver el tipo de dato\n\n")
print("serie.describe:\n",PD_serie.describe())
print("serie.dtypes:\n",PD_serie.dtypes)
pausa()
print("-"*50)
print ("Convertimos to_numeric")
print ("PD_serie=pd.to_numeric(original.copy())")
PD_serie=pd.to_numeric(original.copy())
print("serie: con los datos cambiados x pd.to_numeric(PD_serie)() \n",PD_serie,"<-------------ver el tipo de dato\n\n")
print("serie.describe:\n",PD_serie.describe())
print("serie.dtypes:\n",PD_serie.dtypes)
pausa()
print("-"*50)
print ("PD_serie=pd.to_numeric(original.copy(), downcast='float')")
PD_serie=pd.to_numeric(original.copy(), downcast='float')
print("serie: con los datos cambiados x to_numeric(PD_serie, downcast='float')() \n",PD_serie,"<-------------ver el tipo de dato\n\n")
print ('\n\t\t\tse reconose que se pueden perder datos')
print("serie.describe:\n",PD_serie.describe())
print("serie.dtypes:\n",PD_serie.dtypes)
pausa()
print("-"*50)
print ("PD_serie=pd.to_numeric(original.copy(), downcast='unsigned')")
PD_serie=pd.to_numeric(original.copy(), downcast='unsigned')
print("serie: con los datos cambiados x to_numeric(PD_serie, downcast='unsigned'() \n",PD_serie,"<-------------ver el tipo de dato\n\n")
print ('\n\t\t\tse reconose que se pueden perder datos')
print("serie.describe:\n",PD_serie.describe())
print("serie.dtypes:\n",PD_serie.dtypes)
print("-"*50)
print ("PD_serie=pd.to_numeric(original.copy(), downcast='signed')")
PD_serie=pd.to_numeric(original.copy(), downcast='signed')
print("serie: con los datos cambiados x to_numeric(PD_serie, downcast='signed'() \n",PD_serie,"<-------------ver el tipo de dato\n\n")
print ('\n\t\t\tse reconose que se pueden perder datos')
print("serie.describe:\n",PD_serie.describe())
print("serie.dtypes:\n",PD_serie.dtypes)
pausa()
print("-"*50)
print ("PD_serie=pd.to_numeric(original.copy(), errors='ignore')")

PD_serie=pd.to_numeric(original.copy(), errors='ignore')
print("serie: con los datos cambiados x to_numeric() errors='ignore' \n",PD_serie,"<-------------ver el tipo de dato\n\n")
print ('\n\t\t\tse ignora en la convercion un object')
print("serie.describe:\n",PD_serie.describe())
print("serie.dtypes:\n",PD_serie.dtypes)
pausa()
print("-"*50)
print ("PD_serie=pd.to_numeric(original.copy(), errors='coerce')")
PD_serie=pd.to_numeric(original.copy(), errors='coerce')
print("serie: con los datos cambiados x to_numeric() errors='coerce' \n",PD_serie,"<-------------ver el tipo de dato\n\n")
print ('\n\t\t\tSe convierte en NAN')
print("serie.describe:\n",PD_serie.describe())
print("serie.dtypes:\n",PD_serie.dtypes)
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                     HASNANS                                 ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
        
    
lista3 = ['10.9', 2, 'cinco', None,'siete']
PD_serie3 = pd.Series(lista3)		
        
print("objeto:\nindex\n  |  dato\n  |  |\n",PD_serie3,"<-------------ver el tipo de dato\n\n")
print("objeto tipo:", PD_serie3.hasnans, "<=====tienen NAN")
PD_serie3=pd.to_numeric(PD_serie3, errors='coerce')
print("serie: con los datos cambiados x to_numeric() errors='coerce' \n",PD_serie3)# se convierte en NAN
print("objeto tipo:", PD_serie3.hasnans, "<=====tienen NAN")
PD_serie3=pd.to_numeric(PD_serie3)
print("objeto descripcion:\n", PD_serie3.describe())
print(" reemplazo los NaN por 0")
pausa()
print("-"*50)
PD_serie3 = PD_serie3.fillna(0)
print("objeto:\nindex\n  |  dato\n  |  |\n",PD_serie3,"<-------------ver el tipo de dato\n\n")
print("objeto tipo:", PD_serie3.hasnans, "<=====tienen NAN")
PD_serie3.fillna(0)
print(f"{PD_serie3=}")


pausa()
limpiar()
print("*" * 50)

####################################################################################################
lista1 = [8, None, 7, 5]
lista2 = [10, 2, None, 9]

PD_serie1 = pd.Series(lista1)
PD_serie2 = pd.Series(lista2)

print(f"serie1 =\n {PD_serie1}")
print("-" * 50)
print(f"serie2 =\n {PD_serie2}")
print("^" * 50)
PD_serie1=PD_serie1.fillna(0)
PD_serie2=PD_serie2.fillna(99999)
print(f"serie1 =\n {PD_serie1}")
print("-" * 50)
print(f"serie2 =\n {PD_serie2}")
####################################################################################################


pausa()
limpiar()
print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                         stack     aplano las listas                         ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
lista = [
            ['uno',
             'dos',
             'tres',
             'cuatro'],
            'cinco',
            'seis',
            ['siete',
             'ocho'],
            ['nueve',
             'diez',
             'once',
             'doce',
             'trece',
             'catorce', ]
        ]	
PD_serie = pd.Series(lista)
print("objeto:\nindex\n  |				  dato\n  |				  |\n",PD_serie,"<-------------ver el tipo de dato\n\n")
print("objeto tipo:", type(PD_serie))
print("objeto descripcion:\n", PD_serie.describe())
pausa()
print("-"*50)
PD_serie = PD_serie.apply(pd.Series).stack()
print("objeto:\nindex\n  |	  dato\n  |	  |\n",PD_serie,"<-------------ver el tipo de dato\n\n")
PD_serie = PD_serie.apply(pd.Series).stack().reset_index(drop=False)
print("objeto:\nindex\n  |	  dato\n  |	  |\n",PD_serie,"<-------------ver el tipo de dato\n\n")
PD_serie = PD_serie.apply(pd.Series).stack().reset_index(drop=True)
print("objeto:\nindex\n  |	  dato\n  |	  |\n",PD_serie,"<-------------ver el tipo de dato\n\n")


print("objeto tipo:", type(PD_serie))
print("objeto descripcion:\n", PD_serie.describe())

pausa()
limpiar()
print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║             generamos series desde Matrices  (listas / tuplas)              ║		
║                      listas como elementos de serie                         ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
print ("Los elementos de una serie pueden introducirse desde listas y cada elemento a su ves pueden ser listas.\n Tambien el index puede introducirse desde una lista")

matriz = [[1, 4], [2, "Hola"], [3, True], [4, 3.14159]]#lista con listas como elementos
print (f"{matriz=}")
indice = ["A","B","C","D"]#lista como index
PD_serie = pd.Series(data = matriz, name="datos", index =indice)

# ~ PD_serie = pd.Series(lista1)
print("objeto:\nindex\n  |	  dato\n  |	  |\n",PD_serie,"<-------------ver el tipo de dato\n\n")
print("objeto tipo:", type(PD_serie))
print("objeto index:", PD_serie.index)
print("objeto tamaño:", PD_serie.size)
print("objeto descripcion:\n", PD_serie.describe())
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                        diccionacios con listas como values                  ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
dict_ = {
                'uno' : [1, 200, 99, 1],
                'dos' : [2, 210, 97, 2],
                'tres' : [3, 220, 95, 3],
                'cuatro' : [4, 230, 93, 4],
                'cinco' : [5, 240, 91, 5],
                'seis' : [6, 250, 89, 4],
                'siete' : [7, 260, 87, 3],
                'ocho' : [8, 270, 85, 2],
                'nueve' : [9, 280, 83, 1],
                'diez' : [10, 290, 81, 2],
                'once' : [11, 300, 79, 3],
                'doce' : [12, 310, 77, 4],
                'trece' : [13, 320, 75, 5],
                'catorce' : [14, 330, 73, 6]
                }
PD_serie = pd.Series(dict_, name="Cursor-2023")



print("objeto:\nindex\n  |		  dato\n  |		  |\n",PD_serie,"<-------------ver el tipo de dato\n\n")
print("index:",PD_serie.index)
pausa()
print("-"*50)
print("array:",PD_serie.array)
pausa()
print("-"*50)
print("values:",PD_serie.values)
pausa()
print("-"*50)
print("dtype:",PD_serie.dtype)
pausa()
print("-"*50)
print("shape:--------------------------->",PD_serie.shape)
print("nbytes:-------------------------->",PD_serie.nbytes)
print("ndim:---------------------------->",PD_serie.ndim)
print("size:---------------------------->",PD_serie.size)
pausa()
print("-"*50)
print("objeto:\nindex\n  |		  dato\n  |		  |\n",PD_serie,"<-------------ver el tipo de dato\n\n")
print("Transponer la tabla:")
print("objeto:\nindex\n  |		  dato\n  |		  |\n",PD_serie.T,"<-------------ver el tipo de dato\n\n")
print ("en una serie no tiene sentido. pero...")
pausa()
print("-"*50)
print("name:\n",PD_serie.name)
pausa()
print("que hay en 'nueve'\nPD_serie['nueve']\n",PD_serie['nueve'])
pausa()
print("-"*50)
print("que hay entre 'cinco' y 'doce'\nPD_serie['cinco':'doce']\n",PD_serie['cinco':'doce'])
pausa()
print("-"*50)
print("que hay entre '4' y '12'\nPD_serie[4:12]\n",PD_serie[4:12])
pausa()
print("-"*50)
listaBuscada = ['cinco', 'doce', 'dos', 'once',  'nueve']
print("que hay en 'cinco', 'doce', 'dos', 'once' y 'nueve'\nPD_serie['cinco', 'doce', 'dos', 'once',  'nueve']\n",PD_serie[listaBuscada])
print (PD_serie.loc['cinco'])
pausa()
limpiar()
print("*"*50)








####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                   INDEX                                     ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)

lista = [
        'uno',
        'dos',
        'tres',
        'cuatro',
        'cinco',
        'seis',
        'siete',
        'ocho',
        'nueve',
        'diez',
        'once',
        'doce',
        'trece',
        'catorce',
]
PD_serie = pd.Series(lista)

print("-" * 50)
print("objeto:\nindex\n  |	  dato\n  |	  |\n", PD_serie, "<-------------ver el tipo de dato")
print("  ^")
print("  L________index numerico x default")
original = PD_serie.copy()
pausa()
print("-" * 50)
####################################################################################################
Index_Alfa = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
PD_serie = pd.Series(lista)
PD_serie.index = Index_Alfa
print("objeto:\nindex\n  |	  dato\n  |	  |\n", PD_serie, "<-------------ver el tipo de dato")
print("  ^")
print("  L________index AlfaNumerico x default")
pausa()
print("-" * 50)
####################################################################################################
Index_Romanos = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV"]
PD_serie = pd.Series(data=lista, index=Index_Romanos, name="datos")
print("objeto:\nindex\n  |	  dato\n  |	  |\n", PD_serie, "<-------------ver el tipo de dato")
print("  ^")
print("  L________index Romanos")
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                     REINDEX                                 ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
print ("PD_serie = PD_serie.reset_index()")
PD_serie = PD_serie.reset_index()
print("objeto:\n", PD_serie)
print("  ^    ^")
print("  |    L__index RomanosaNumerico x default")
print("  L_ reset_index")
pausa()
print("-" * 50)
####################################################################################################


print ("PD_serie = pd.Series(data=lista, name='datos')")
PD_serie = pd.Series(data=lista, name="datos")
print ("PD_serie.index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']")
Index_Alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
PD_serie.index = Index_Alfa
print("recreo la serie:\n", PD_serie)
print("  ^    ^")
print("  |    L__Datos")
print("  L__index Alfa")
pausa()
print("-" * 50)
print ("PD_serie= PD_serie.reset_index()")
PD_serie = PD_serie.reset_index()
print("objeto:\n", PD_serie)
print("  ^    ^")
print("  |    L__index Alfa")
print("  L_ reset_index")
pausa()
print("-" * 50)
####################################################################################################

Index_Romanos = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV']
print ("PD_serie.index = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV']")
PD_serie.index = Index_Romanos
print("objeto:\n", PD_serie)
print("  ^    ^")
print("  |    L__index Alfanum")
print("  L_ index Romanos")
pausa()
print("-" * 50)
####################################################################################################
PD_serie = PD_serie.reset_index(drop=False)
print ("PD_serie.reset_index(drop=False)")
print("objeto:\n", PD_serie)
print("  ^    ^      ^")
print("  |    |      L__index Alfa")
print("  |    L_ index Romanos")
print("  L_ reset_index")
completa =PD_serie.copy()
pausa()
limpiar()
print("-" * 50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                             sort   ordeno la lista                          ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)

lista = [
    'uno',
    'dos',
    'tres',
    'cuatro',
    'cinco',
    'seis',
    'siete',
    'ocho',
    'nueve',
    'diez',
    'once',
    'doce',
    'trece',
    'catorce',
    ]

print ("PD_serie = pd.Series(lista).sort_values()")
PD_serie = pd.Series(lista).sort_values()
print("Ordeno x datos  alfabeticamente")
print("objeto:\nindex\n  |	  dato (orden alfabético)\n  |	  |\n",PD_serie,"<-------------ver el tipo de dato\n\n")

pausa()
limpiar()
print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                  append    agrego datos al final de la serie                ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
PD_serie = original.copy()
print("objeto:\nindex\n  |	  dato\n  |	  |\n",PD_serie,"<-------------ver el tipo de dato\n\n")
pausa()
print("-" * 50)
print ("agreguemos ['quince','dieciseis','siecisiete','diesiocho','diecinueve','veinte']")
print ("PD_serie.append(pd.Series(['quince','dieciseis','siecisiete','diesiocho','diecinueve','veinte']))")
PD_serie2 = PD_serie.append(pd.Series(['quince','dieciseis','siecisiete','diesiocho','diecinueve','veinte']))
print("objeto:\nindex\n  |	  dato\n  |	  |\n",PD_serie2,"<-------------ver el tipo de dato\n\n")
pausa()
print("-" * 50)
print ("agreguemos ['quince','dieciseis','siecisiete','diesiocho','diecinueve','veinte']")
print ("reset_index(drop=True)")
print("PD_serie.append(pd.Series(['quince','dieciseis','siecisiete','diesiocho','diecinueve','veinte'])).reset_index(drop=True)")
PD_serie2 = PD_serie.append(pd.Series(['quince','dieciseis','siecisiete','diesiocho','diecinueve','veinte'])).reset_index(drop=True)
print("objeto:\nindex\n  |	  dato\n  |	  |\n",PD_serie2,"<-------------ver el tipo de dato\n\n")
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                        DROP    borramos columnas                            ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
# axis  // columns - rows
####################################################################################################
PD_serie = completa.copy()
print ("Serie completa:\n",PD_serie)
pausa()
print("-" * 50)
print (f"PD_serie = PD_serie.drop(columns=['level_0', 'index'])")
PD_serie = PD_serie.drop(columns=['level_0', 'index'])
print("PD_serie.drop(['level_0', 'index'], axis=1):\n", PD_serie2, "<-------------ver el tipo de dato")
print("  ^    ^")
print("  |    L__index Alfanum")
print("  L_ index Numerico")
pausa()
print("-" * 50)
####################################################################################################
PD_serie = completa.copy()
print ("Serie completa:\n",PD_serie)
pausa()
print("-" * 50)
print (f"PD_serie = PD_serie.drop(columns=['level_0', 'index'], axis=1)")
PD_serie = PD_serie.drop(['level_0', 'index'], axis=1)
print("PD_serie.drop(['level_0', 'index'], axis=1):\n", PD_serie2, "<-------------ver el tipo de dato")
print("  ^    ^")
print("  |    L__index Alfanum")
print("  L_ index Numerico")
pausa()
limpiar()

print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                        DROP    borramos registros / filas                   ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
# axis  // columns - rows
####################################################################################################
PD_serie = completa.copy()
print ("Serie completa:\n",PD_serie)

pausa()
print("-" * 50)
PD_serie3 = PD_serie.drop([1, 3, 5, 7, 9, 11, 13], axis=0)
print("PD_serie3 = PD_serie.drop([1, 3, 5, 7, 9, 11, 13], axis=0):\n", PD_serie3, "<-------------ver el tipo de dato")
print("  ^    ^      ^")
print("  |    |      L__index Alfa")
print("  |    L_ index Romanos")
print("  L_ reset_index")
print()
pausa()
limpiar()
print("-" * 50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                        DROP    borramos columans y registros / filas        ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
# axis  // columns - rows
####################################################################################################print("Cambio de index y borro")
PD_serie = lista = [
            'uno',
            'dos',
            'tres',
            'cuatro',
            'cinco',
            'seis',
            'siete',
            'ocho',
            'nueve',
            'diez',
            'once',
            'doce',
            'trece',
            'catorce',
    ]
PD_serie = pd.Series(lista)
print ("Serie completa:\n",PD_serie)
pausa()
print("-" * 50)
PD_serie = PD_serie.drop(['level_0', 'index'], axis=1)
print(" PD_serie.drop(['level_0', 'index'], axis=1):\n", PD_serie, "<-------------ver el tipo de dato")
pausa()
print("-" * 50)
PD_serie = PD_serie.drop(["A", "B", "C", "D", "E"], axis=0)
print(" PD_serie.drop(['A', 'B', 'C', 'D', 'E'], axis=0):\n", PD_serie, "<-------------ver el tipo de dato")
print("  ^")
print("  L________index RomanosaNumerico x default")
pausa()
print("-" * 50)
PD_serie = original.copy()
print ("Serie completa:\n",PD_serie)
pausa()
PD_serie = PD_serie.drop(['level_0', 'index'], axis=1).drop(['A', 'B', 'C', 'D', 'E'], axis=0)
print("PD_serie.drop(['level_0', 'index'], axis=1).drop(['A', 'B', 'C', 'D', 'E'], axis=0):\n", PD_serie, "<-------------ver el tipo de dato")
pausa()
####################################################################################################
lista = [
		'diez',
		'dos',
		'tres',
		'cuatro',
		'cinco',
		'seis',
		'uno',
		'ocho',
		'dos',
		'cinco',
		'tres',
		'ocho',
		'seis',
		'cuatro',
]
PD_serie = pd.Series(lista)
print("objeto:\nindex\n  |  dato\n  |  |\n",PD_serie,"<-------------ver el tipo de dato\n\n")
pausa()
print("-" * 50)
###################################################################################################
PD_serie1 = PD_serie.drop_duplicates()
print("drop duplicado:\n")
print("objeto:\nindex\n  |  dato\n  |  |\n",PD_serie1,"<-------------ver el tipo de dato\n\n")
pausa()
print("-" * 50)
####################################################################################################
PD_serie2 = PD_serie.drop_duplicates(keep='last')
print("drop duplicado:\n")
print("objeto:\nindex\n  |  dato\n  |  |\n",PD_serie2,"<-------------ver el tipo de dato\n\n")
pausa()
limpiar()
print("-" * 50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                            filtrando de datos                               ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                    Filter                                   ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
dict_2 = {
		'uno' : 99,
		'dos' : 88,
		'tres' : 77,
		'cuatro' : 66,
		'cinco' : 55,
		'seis' : 44,
		'siete' : 33,
		'ocho' : 22,
		'nueve' : 11,
		'diez' : 9,
		'once' : 8,
		'doce' : 7,
		'trece' : 6,
		'catorce' : 5
		}
PD_serie2 = pd.Series(dict_2, name="Cursor-2023")
####################################################################################################
PD_serie2 = PD_serie.filter(items=['uno','tres','cinco','siete','nueve','once','trece'])
print("objeto filter\nPD_serie.filter(items=['uno','tres','cinco','siete','nueve','once','trece'])\n")
print("objeto:\nindex\n  |  dato\n  |  |\n",PD_serie2,"<-------------ver el tipo de dato\n\n")
pausa()
print("-"*50)
####################################################################################################
PD_serie2 = PD_serie.filter(regex='o')
print("objeto filter\nPD_serie.filter(regex='o')\n")
print("objeto:\nindex\n  |  dato\n  |  |\n",PD_serie2,"<-------------ver el tipo de dato\n\n")
pausa()
print("-"*50)
####################################################################################################
PD_serie2 = PD_serie.filter(like='ce')
print("objeto filter\nPD_serie.filter(like='ce')\n")
print("objeto:\nindex\n  |  dato\n  |  |\n",PD_serie2,"<-------------ver el tipo de dato\n\n")
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                    Where                                    ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
dict_2 = {
		'uno' : 99,
		'dos' : 88,
		'tres' : 77,
		'cuatro' : 66,
		'cinco' : 55,
		'seis' : 44,
		'siete' : 33,
		'ocho' : 22,
		'nueve' : 11,
		'diez' : 9,
		'once' : 8,
		'doce' : 7,
		'trece' : 6,
		'catorce' : 5
		}
PD_serie = pd.Series(dict_2, name="Cursor-2023")
####################################################################################################
print("objeto:\nindex\n  |  dato\n  |  |\n",PD_serie,"<-------------ver el tipo de dato\n\n")
print("objeto media----------------------------------->:",PD_serie.mean())
print("-"*50)
PD_serie2= PD_serie.where(PD_serie < PD_serie.median(),'mayor a la media')
print("respecto a la media \n",PD_serie2)
PD_serie2= PD_serie.where(PD_serie > PD_serie.median(),'menor a la media')
print("respecto a la media \n",PD_serie2)
pausa()
####################################################################################################
print("-"*50)
PD_serie2= PD_serie.where(PD_serie > 25,'menor a 25')
print("respecto a > 25 \n",PD_serie2)
pausa()
####################################################################################################
print("-"*50)
PD_serie2= PD_serie.where(PD_serie > 25)
print("respecto a > 25a \n",PD_serie2)
print("objeto tipo:",PD_serie2.hasnans,"<=====tienen NAN???????")
print("Borro los datos NaN")
PD_serie2= PD_serie.where(PD_serie > 25).dropna()
print("respecto a > 25 \n",PD_serie2)
print("objeto tipo:",PD_serie2.hasnans,"<=====tienen NAN???????")
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  Between                                    ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
print("Sin incluir los limites 22,66")
PD_serie2= PD_serie.between(22, 66)
print("PD_serie.between(10, 60) \n",PD_serie2)
pausa()
####################################################################################################
print("-"*50)
print("incluyo los limites 22,66")
PD_serie2= PD_serie.between(22, 66, inclusive = False)
print("PD_serie.between(10, 60) \n",PD_serie2)
pausa()
####################################################################################################
print("-"*50)
dict_2 = {
			'uno' : 99,
			'dos' : 88,
			'tres' : 99,
			'cuatro' : 88,
			'cinco' : 55,
			'seis' : 77,
			'siete' : 33,
			'ocho' : 99,
			'nueve' : 55,
			'diez' : 99,
			'once' : 88,
			'doce' : 77,
			'trece' : 88,
			'catorce' : 55
			}
PD_serie1 = pd.Series(dict_2, name="Cursor-2023")
PD_serie2= PD_serie1.value_counts()
print("respecto a la repet de valores \n",PD_serie2)
print("  ^    ^")
print("  |    L__ cant.repeticion")
print("  L_ dato repetido")
pausa()
####################################################################################################
print("-"*50)
print("mayores a la media \n", PD_serie1[PD_serie1 > PD_serie1.median()])
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                       series: operaciones basicas                           ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
lista1 = [1,8,3,9]
lista2 = [8,3,7,5]
lista_resul = lista1 + lista2
PD_serie1 = pd.Series(lista1)
PD_serie2 = pd.Series(lista2)
PD_resul = PD_serie1+PD_serie2
print('                   SUMA')
print('lista1:',lista1)
print('lista2:',lista2)
print("suma de listas:\n",lista_resul,"<-------------ver el tipo de dato tras la operacion\n\n")
print("-"*50)
print('PD_serie1:',PD_serie1,"\n\n")
print('PD_serie2:',PD_serie2,"\n\n")
print("suma de series:\n",PD_resul,"<-------------ver el tipo de dato tras la operacion\n\n")
print ("notese la diferencia q la suma de dos listas solo genera una tercera con todos los datos de ambas listas concatenadas")
print ("la suma de dos series dan una tercer serie con la suma de cada lugar - index de ambas series, suma índice a índice.")
print("objeto tipo:",type(PD_resul))
print("objeto index:",PD_serie.index)
print("objeto tamaño:",PD_resul.size)
print("objeto descripcion:\n",PD_resul.describe())
print("\n\n\nen el indice 2 hay:",PD_resul[2])
pausa()
####################################################################################################
print("-"*50)
PD_serie1 = pd.Series(lista1)
PD_serie2 = pd.Series(lista2)
PD_resul = PD_serie1 - PD_serie2
print('                   RESTA')
print("objeto:\n",PD_resul,"<-------------ver el tipo de dato tras la operacion\n\n")
print("objeto tipo:",type(PD_resul))
print("objeto index:",PD_serie.index)
print("objeto tamaño:",PD_resul.size)
print("objeto descripcion:\n",PD_resul.describe())
pausa()
####################################################################################################
print("-"*50)
PD_serie1 = pd.Series(lista1)
PD_serie2 = pd.Series(lista2)
PD_resul = PD_serie1*PD_serie2
print('                   MULTIPLICACION')
print("objeto:\n",PD_resul,"<-------------ver el tipo de dato tras la operacion\n\n")
print("objeto tipo:",type(PD_resul))
print("objeto index:",PD_serie.index)
print("objeto tamaño:",PD_resul.size)
print("objeto descripcion:\n",PD_resul.describe())
pausa()
####################################################################################################
print("-"*50)
PD_serie1 = pd.Series(lista1)
PD_serie2 = pd.Series(lista2)
PD_resul = PD_serie1/PD_serie2
print('                   DIVISION')
print("objeto:\n",PD_resul,"<-------------ver el tipo de dato tras la operacion\n\n")
print("objeto tipo:",type(PD_resul))
print("objeto index:",PD_serie.index)
print("objeto tamaño:",PD_resul.size)
print("objeto descripcion:\n",PD_resul.describe())
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                       series: operaciones >,>=,<,<=, ==, !=                 ║
║                              index a index                                  ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
lista = [1,8,7,9]
lista2 = [8,3,7,5]
PD_serie = pd.Series(lista)
PD_serie2 = pd.Series(lista2)
PD_resul = PD_serie>PD_serie2
print('                   ">"')
print("objeto:\n",PD_resul,"<-------------ver el tipo de dato tras la operacion\n\n")
print("objeto tipo:",type(PD_resul))
print("objeto index:",PD_resul.index)
print("objeto tamaño:",PD_resul.size)
print("objeto descripcion:\n",PD_resul.describe())
pausa()
print("*"*50)
####################################################################################################
PD_serie1 = pd.Series(lista)
PD_serie2 = pd.Series(lista2)
PD_resul = PD_serie1==PD_serie2
print('                   "=="')
print("objeto:\n",PD_resul,"<-------------ver el tipo de dato tras la operacion\n\n")
print("objeto tipo:",type(PD_resul))
print("objeto index:",PD_resul.index)
print("objeto tamaño:",PD_resul.size)
print("objeto descripcion:\n",PD_resul.describe())
pausa()
limpiar()
print("*"*50)
# ~ ####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                  Operadores                                 ║
║                                                                             ║
║                              add suma series                                ║
║                              subtract resta series                          ║
║                              multiply multiplica series                     ║
║                              divide divide series                           ║
║                              lt menor que series                            ║
║                              le menor igual series                          ║
║                              eq igual series                                ║
║                              gt mayor que series                            ║
║                              ge mayor igual series                          ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)


lista = [1,8,3,9]
lista2 = [8,3,7,5]

PD_serie1 = pd.Series(lista)
PD_serie2 = pd.Series(lista2)
print ("Serie 1:\n",PD_serie1,'\n',PD_serie1.dtype) 
print ("Serie 2:\n",PD_serie2,'\n',PD_serie2.dtype)
print("-"*50)
print ("add")
PD_serie3 =PD_serie1.add(PD_serie2)
print("objeto PD_serie1.add(PD_serie2):\n",PD_serie3," dato\n\n")
pausa()
####################################################################################################
print("-"*50)
print("subtract")
PD_serie3 =PD_serie1.subtract(PD_serie2)
print("objeto PD_serie1.subtract(PD_serie2):\n",PD_serie3," dato\n\n")
pausa()
####################################################################################################
print("-"*50)
print("multiply")
PD_serie3 =PD_serie1.multiply(PD_serie2)
print("objeto PD_serie1.multiply(PD_serie2):\n",PD_serie3," dato\n\n")
pausa()
####################################################################################################
print("-"*50)
print("divide")
PD_serie3 =PD_serie1.divide(PD_serie2)
print("objeto PD_serie1.divide(PD_serie2):\n",PD_serie3," dato\n\n")
pausa()
####################################################################################################
print("-"*50)
print("menor que ---LT comparando uno por uno")
PD_serie3 =PD_serie1.lt(PD_serie2)
print("objeto PD_serie1.lt(PD_serie2):\n",PD_serie3," dato\n\n")
pausa()
####################################################################################################
print("-"*50)
print("menor igual que ---LE comparando uno por uno")
PD_serie3 =PD_serie1.le(PD_serie2)
print("objeto PD_serie1.le(PD_serie2):\n",PD_serie3," dato\n\n")
pausa()
####################################################################################################
print("-"*50)
print("igual que ---EQ comparando uno por uno")
PD_serie3 =PD_serie1.le(PD_serie2)
print("objeto PD_serie1.le(PD_serie2):\n",PD_serie3," dato\n\n")
pausa()
####################################################################################################
print("-"*50)
print("mayor que ---GT comparando uno por uno")
PD_serie3 =PD_serie1.gt(PD_serie2)
print("objeto PD_serie1.gt(PD_serie2):\n",PD_serie3," dato\n\n")
pausa()
####################################################################################################
print("-"*50)
print("mayor igual que ---GE comparando uno por uno")
PD_serie3 =PD_serie1.ge(PD_serie2)
print("objeto PD_serie1.ge(PD_serie2):\n",PD_serie3," dato\n\n")
pausa()
limpiar()
print("-"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                           DOT producto escalar                              ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
print("DOT producto escalar")
PD_serie3 =PD_serie1.dot(PD_serie2)
print("DOT producto escalar :PD_serie1.dot(PD_serie2): ",PD_serie3)
limpiar()
print("-"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║               equals - mismo valores en el mismo index                      ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)

print("DOT producto escalar")
PD_serie3 =PD_serie1.equals(PD_serie2)
print("Equals :PD_serie3 =PD_serie1.equals(PD_serie2)): ",PD_serie3)
pausa()
####################################################################################################
print("-"*50)
print("DOT producto escalar")
PD_serie3 =PD_serie1.equals(PD_serie1)
print("Equals :PD_serie3 =PD_serie1.equals(PD_serie1)): ",PD_serie3)
pausa()
limpiar()
print("-"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  & | == !                                   ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
print("mayor igual que ---GE comparando uno por uno")
PD_serie3 =( 2<=PD_serie1) & (PD_serie2<=5)
print("objeto PD_serie1.ge(PD_serie2):\n",PD_serie3," dato\n\n")
pausa()
####################################################################################################
print("-"*50)
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lista = list(range(20,0,-1))
PD_serie = pd.Series(lista)
print("objeto PD_serie1:\n",PD_serie,"<-------------ver el tipo de dato\n\n")
pausa()
####################################################################################################
print("-"*50)
SerieResul= PD_serie [PD_serie>10]
print("objeto PD_serie1 mayores a 10:\n",SerieResul,"<-------------ver el tipo de dato\n\n")
pausa()
####################################################################################################
print("-"*50)
SerieResul= PD_serie [PD_serie%2==0]
print("objeto PD_serie1 pares:\n",SerieResul,"<-------------ver el tipo de dato\n\n")
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  Funciones                                  ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
def funcion(dato):
	return (dato ** 2)
PD_serie2 =PD_serie.apply(funcion)
print("Funcion valores \n",PD_serie2)
pausa()
####################################################################################################
print("-"*50)
PD_serie2 =PD_serie.apply(lambda dato : dato ** 2)
print("Funcion lambda valores \n",PD_serie2)
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                              pandas a listas                                ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
lista1 = [1,8,7,9]
lista2 = [8,3,7,5]

PD_serie1 = pd.Series(lista1)
PD_serie2 = pd.Series(lista2)

PD_resul = PD_serie1*PD_serie2
listaResul= PD_resul.to_list()
print('                   "serie a lista"')
print("listaResul:\n",listaResul,"<-------------ver el tipo de dato tras la operacion\n\n")
print("objeto tipo:",type(listaResul))
print("listaResul tamaño:",len(listaResul))
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                           pandas a Diccionarios                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
dict_ = {
			'uno' : 99,
			'dos' : 88,
			'tres' : 99,
			'cuatro' : 88,
			'cinco' : 55,
			'seis' : 77,
			'siete' : 33,
			'ocho' : 99,
			'nueve' : 55,
			'diez' : 99,
			'once' : 88,
			'doce' : 77,
			'trece' : 88,
			'catorce' : 55
			}
#########################################################################################################################################

PD_serie = pd.Series(data = dict_, name="datos")
PD_resul = PD_serie*100
DicResul = PD_resul.to_dict()
print('                   "serie a dic"')
print("Original:\n",PD_serie,"<-------------ver el tipo de dato tras la operacion\n\n")
print("Resultado:\n",DicResul,"<-------------ver el tipo de dato tras la operacion\n\n")
print("objeto tipo:",type(DicResul))
print("Resultado tamaño:",len(DicResul))
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                               pandas a Json                                 ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
PD_serie = pd.Series(data=dict_, name="datos")
PD_resul = PD_serie * 50
archivo = 'dePandasAJson.json'
PD_resul.to_json(archivo)
print('                   "serie a Json"')
print(f"Resultado {archivo} grabado")
pausa()
limpiar()
print("*"*50)
####################################################################################################





dict_ = {
			1:'uno',
			2:'dos',
			3:'tres',
			4:'cuatro',
			5:'cinco',
			6:'seis',
			7:'siete' ,
			8:'ocho',
			9:'nueve',
			10:'diez',
			11:'once',
			12:'doce',
			13:'trece',
			14:'catorce',
			}
###############
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                               pandas a CSV                                  ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
PD_serie = pd.Series(data=dict_, name="datos")
print("Resultado:\n", PD_serie, "<-------------ver el tipo de dato tras la operacion\n\n")
archivo = 'dePandasACSV.csv'
PD_serie.to_csv(archivo)
print('                   "serie a csv"')
print(f"Resultado {archivo} grabado")
pausa()
####################################################################################################
print("-"*50)
csvResul = PD_serie.to_csv(index=False)
print('                   "serie a csv"')
print("Resultado:\n", csvResul, "<-------------ver el tipo de dato tras la operacion\n\n")
print("objeto tipo:", type(csvResul), 'csvResul')
print("csvResul tamaño:", len(csvResul))
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                               pandas a Excel                                ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
PD_serie = pd.Series(data=dict_, name="datos")
print("Resultado:\n", PD_serie, "<-------------ver el tipo de dato tras la operacion\n\n")
archivo = 'dePandasAExcel.xlsx'

PD_serie.to_excel(archivo, sheet_name='Sheet_name_1')
PD_serie.to_excel(archivo, engine='xlsxwriter')
print('                   "serie a xlsx"')
print(f"Resultado {archivo} grabado")
pausa()
limpiar()
print("*"*50)
####################################################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                  PANDAS                                     ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                    pandas series a pandas dataframes                        ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m """)
PD_serie = pd.Series(data=dict_, name="datos")
print("DataFrameResul:\n", PD_serie, "<-------------ver el tipo de dato tras la operacion\n\n")
DataFrameResul = PD_serie.to_frame()
print('                   "serie a DataFrame"')
print("DataFrameResul:\n", DataFrameResul, "<-------------ver el tipo de dato tras la operacion\n\n")
print("objeto tipo:", type(DataFrameResul))
print("DataFrameResul tamaño:", len(DataFrameResul))
pausa()
limpiar()
print("*" * 50)

####################################################################################################
