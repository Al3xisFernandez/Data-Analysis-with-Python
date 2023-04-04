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

array                                                   El ExtensionArray de los datos que respaldan esta serie o índice.
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                             Pandas Series                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                             Methods (191)                                   ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m 






append(para_añadir[, ignorar_índice, ...])              (DEPRECATED) Concatenar dos o más Series
mad([eje, skipna, nivel])                               (DEPRECATED) Devuelve la desviación absoluta media de los valores sobre el eje solicitado.
iteritems()                                             (DEPRECATED) Iterar perezosamente sobre (índice, valor) tuplas.
s_monotonic                                             (DEPRECATED) Devuelve boolean si los valores en el objeto aumentan monótonamente.
slice_shift([puntos, eje])                              (DEPRECATED) Equivalente a turno sin copiar datos.
tshift([períodos, frecuencia, eje])                     (DEPRECATED) Cambia el índice de tiempo, usando la frecuencia del índice si está disponible.
    

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