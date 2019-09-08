import re

def condSplit(conds):
    lista=[]
    q = conds.split('OR')
    for c in q:
        x = c.split('AND')
        lista.append(x)
    return lista

"""
INSERT
--------
Entradas:
String: Nombre de la tabla donde se va a insertar.
Lista de string y/o: Lista que contiene el nombre de las columnas a insertar.
Lista de string y/o enteros: Lista que contiene los elementos a insertar en la tabla.
--------
Salida:
Void No retorna nada, solo inserta y muestra un mensaje que avisa que se ha insertado una fila.
--------
La funcion abre un archivo, en el cual inserta los elementos de la lista valores, en el orden
que se especifico en columna.
""" 
def INSERT(tabla,columna,valores):
        arch = open(tabla+'.csv','r')
        lista_col = []
        i = 1
        col_aux = []
        val_aux = []
        #---------------Creo una lista con el nombre de las columnas de la tabla---------------#
        for linea in arch:
                if i == 1:
                        lista_col = linea.strip().split(',')
                        i+=1
        arch.close()
        #---------------Ordeno la lista valores para insertarlos correctamente en la tabla---------------#
        for x in lista_col:
                for y in columna:
                        if y not in lista_col:
                                print('La columna '+str(y)+' solicitada previamente, no existe.')
                                arch.close()
                                return
                        if y == x:
                                col_aux.append(y)
                                val_aux.append(valores[columna.index(y)].strip())
                if (x not in columna):
                        val_aux.append(' ')
        arch = open(tabla+'.csv','a')
        a = ','.join(val_aux)
        arch.write(a)
        arch.write('\n')
        
        arch.close()
        print('Se ha insertado 1 fila.')
        return

"""
UPDATE
--------
Entradas:
String: Nombre de la tabla donde se va a insertar.
Lista de string y/o enteros: Lista que contiene las columnas, y su valor a cambiar.
Lista de string y/o enteros: Lista que contiene las condiciones que debe de cumplir la columna para que se pueda actualizar.
--------
Salida:
Void No retorna nada, solo actualiza y muestra un mensaje que avisa que se ha actualizado una fila.
--------
La funcion abre un archivo, en el cual actualiza una o mas filas, por los
valores de la lista cambios, basado en que esta contenga o no los valores especificados en conds.
""" 

def UPDATE(tabla,cambios,conds):
        arch = open(tabla+'.csv','r')
        lista_arch = []
        for linea in arch:
                lista_arch.append(linea.strip().split(','))
        arch.close()
        lista_col = lista_arch[0]
        cumple = 0
        lista_cumple = []
        arch = open(tabla+'.csv','r')
        #---------------Creo una lista con las posiciones de las filas que cumplen las condiciones---------------#
        for linea in lista_arch:
                for bloqueOR in conds:
                        for elemento in linea:
                                for bloqueAND in bloqueOR:
                                        And = re.split(r'=',bloqueAND)
                                        if And[1].strip() == elemento and And[0].strip() == lista_col[linea.index(elemento)]:
                                                cumple+=1
                        if cumple == len(bloqueOR):
                                lista_cumple.append(lista_arch.index(linea))
                        cumple = 0
        if len(lista_cumple) == 0:
                print('La informacion solicitada no existe.')
                arch.close()
                return
        arch.close()
        arch = open(tabla+'.csv','w')
        #---------------Actualizo la fila correspondiente---------------#
        for x in lista_cumple:
                for linea in lista_arch:
                        for elemento in linea:
                                if lista_arch.index(linea) == x:
                                        for cambio in cambios:
                                                string = re.split(r'=',cambio)
                                                if linea.index(elemento) == lista_col.index(string[0].strip()):
                                                        linea[linea.index(elemento)] = string[1].strip()
                                                        break
        for linea in lista_arch:
                arch.write(','.join(linea))
                arch.write('\n')
        arch.close()
        print('Se ha(n) actualizado '+str(len(lista_cumple))+' fila(s).')
        return

"""
Select
--------
Entradas:
Lista: Lista que contiene las columnas de la tabla, y su valor a imprimir, si contiene un *, imprime todas las filas que cumplan
con la condicion especificada en otros.
String: Nombre de la tabla donde se va a insertar.
Lista: Lista de tamanio 3. En la primera posicion, contiene un string con el nombre de la otra tabla que se unira con el
parametro "tabla". En la segunda posicion, contiene las condiciones que debe cumplir la fila para ser imprimida. Y por ultimo
la tercera posicion, contiene un string, que especifica por cual elemento de la fila se va a ordernar, ya se de manera ascendiente
o descendiente.
--------
Salida:
Void No retorna nada, solo imprime las columnas especificadas en columnas.
--------
La funcion abre un archivo, en el cual actualiza una o mas filas, por los
valores de la lista cambios, basado en que esta contenga o no los valores especificados en conds.
""" 

def Select(columnas, tabla, otros):
        i = 1
        arch = open(tabla+'.csv','r')
        lista_col = []
        for linea in arch:
                if i == 1:
                        lista_col = linea.strip().split(',')
                        i+=1
        arch.close
        arch = open(tabla+'.csv','r')
        #---------------Casos SIN INNER JOIN---------------#
        if otros[0] == 'x':
                for x in columnas:
                        if x != '*' and x not in lista_col:
                                print('La informacion solicitada no existe.')
                                arch.close()
                                return
                #---------------Casos con WHERE---------------#
                if otros[1] != 'x':
                        #---------------Casos con ORDER BY---------------#
                        if otros[2] != 'x':
                                #---------------Se imprimen ciertas columnas---------------#
                                if '*' not in columnas:
                                        lista_elementos = []
                                        lista_filas = []
                                        lista_elementos_aux = []
                                        lista_filas_aux = []
                                        FILA = []
                                        cumple = 0
                                        lista_cumple = []
                                        FILA_N = 0
                                        #---------------Creo una lista con las posiciones de las filas que cumplen la condicion---------------#
                                        for linea in arch:
                                                FILA = linea.strip().split(',')
                                                for bloqueOR in otros[1]:
                                                        for elemento in FILA:
                                                                for bloqueAND in bloqueOR:
                                                                        And = re.split(r'=',bloqueAND)
                                                                        if And[1].strip() == elemento and And[0].strip() == lista_col[FILA.index(elemento)]:
                                                                                cumple+=1
                                                        if cumple == len(bloqueOR):
                                                                lista_cumple.append(FILA_N)
                                                        cumple = 0
                                                FILA_N += 1
                                        if len(lista_cumple) == 0:
                                                print('La informacion solicitada no existe.')
                                                arch.close()
                                                return
                                        #---------------Creo dos listas, una con los elementos que cumplen la condicion, y la otra con las filas que cumplen la condicion---------------#
                                        FILA_N = 0
                                        arch.close()
                                        arch = open(tabla+'.csv','r')
                                        lista_elementos_aux = []
                                        lista_filas_aux = []
                                        for linea in arch:
                                                FILA = linea.strip().split(',')
                                                for x in lista_cumple:
                                                        for elemento in FILA:
                                                                for col in columnas:
                                                                        if x == FILA_N and FILA.index(elemento) == lista_col.index(col):
                                                                                lista_elementos.append(elemento)
                                                                        if len(lista_elementos) == len(columnas):
                                                                                lista_filas.append(lista_elementos)
                                                                                lista_elementos = []
                                                FILA_N+=1
                                        #---------------Ordeno las listas en base a lo que haya en OrderBy---------------#
                                        for col in columnas:
                                                if col in otros[2]:
                                                        lugar = columnas.index(col)
                                                        for elementos in lista_filas:
                                                                for elemento in elementos:
                                                                        if elementos.index(elemento) == lugar:
                                                                                lista_elementos_aux.append(elemento)
                                                        if 'ASC' in otros[2]:
                                                                lista_elementos_aux = sorted(lista_elementos_aux)
                                                                for elemento in lista_elementos_aux:
                                                                        for elementos in lista_filas:
                                                                                if str(elemento) in elementos:
                                                                                        lista_filas_aux.append('  '.join(elementos))
                                                        else:
                                                                lista_elementos_aux = sorted(lista_elementos_aux,reverse=True)
                                                                for elemento in lista_elementos_aux:
                                                                        for elementos in lista_filas:
                                                                                if str(elemento) in elementos:
                                                                                        lista_filas_aux.append('  '.join(elementos))
                                        for x in lista_filas_aux:
                                                print(x)
                                #---------------Se imprimen todas las columnas---------------
                                else:
                                        lista_elementos = []
                                        lista_filas = []
                                        lista_elementos_aux = []
                                        lista_filas_aux = []
                                        FILA = []
                                        cumple = 0
                                        lista_cumple = []
                                        FILA_N = 0
                                        #---------------Creo una lista con las posiciones de las filas que cumplen la condicion---------------#
                                        for linea in arch:
                                                FILA = linea.strip().split(',')
                                                for bloqueOR in otros[1]:
                                                        for elemento in FILA:
                                                                for bloqueAND in bloqueOR:
                                                                        And = re.split(r'=',bloqueAND)
                                                                        if And[1].strip() == elemento and And[0].strip() == lista_col[FILA.index(elemento)]:
                                                                                cumple+=1
                                                        if cumple == len(bloqueOR):
                                                                lista_cumple.append(FILA_N)
                                                        cumple = 0
                                                FILA_N += 1
                                        if len(lista_cumple == 0):
                                                print('La informacion solicitada no existe.')
                                                arch.close()
                                                return
                                        FILA_N = 0
                                        arch.close()
                                        arch = open(tabla+'.csv','r')
                                        for linea in arch:
                                                FILA = linea.strip().split(',')
                                                for x in lista_cumple:
                                                        if x == FILA_N:
                                                                lista_filas.append(FILA)
                                                FILA_N += 1
                                        #---------------Ordeno las listas en base a lo que haya en OrderBy---------------#
                                        lista_elementos_aux = []
                                        lista_filas_aux = []
                                        Ordenador = re.split(r' ',otros[2])[0]
                                        lugar = lista_col.index(Ordenador)
                                        for elementos in lista_filas:
                                                for elemento in elementos:
                                                        if elementos.index(elemento) == lugar:
                                                                lista_elementos_aux.append(elemento)
                                        if 'ASC' in otros[2]:
                                                lista_elementos_aux = sorted(lista_elementos_aux)
                                                for elemento in lista_elementos_aux:
                                                        for elementos in lista_filas:
                                                                if str(elemento) in elementos:
                                                                        lista_filas_aux.append('  '.join(elementos))
                                        else:
                                                lista_elementos_aux = sorted(lista_elementos_aux,reverse=True)
                                                for elemento in lista_elementos_aux:
                                                        for elementos in lista_filas:
                                                                if str(elemento) in elementos:
                                                                        lista_filas_aux.append('  '.join(elementos))
                                        arch.close()
                                        arch = open(tabla+'.csv','r')
                                        for x in lista_filas_aux:
                                                print (x)
                        #---------------Casos sin Order By---------------
                        else:                        
                                #---------------Se imprimen ciertas columnas---------------        
                                if '*' not in columnas:
                                        lista_elementos = []
                                        lista_filas = []
                                        FILA = []
                                        cumple = 0
                                        lista_cumple = []
                                        FILA_N = 0
                                        #---------------Creo una lista con las posiciones de las filas que cumplen la condicion---------------#
                                        for linea in arch:
                                                FILA = linea.strip().split(',')
                                                for bloqueOR in otros[1]:
                                                        for elemento in FILA:
                                                                for bloqueAND in bloqueOR:
                                                                        And = re.split(r'=',bloqueAND)
                                                                        if And[1].strip() == elemento and And[0].strip() == lista_col[FILA.index(elemento)]:
                                                                                cumple+=1
                                                        if cumple == len(bloqueOR):
                                                                lista_cumple.append(FILA_N)
                                                        cumple = 0
                                                FILA_N += 1
                                        if len(lista_cumple) == 0:
                                                print('La informacion solicitada no existe.')
                                                arch.close()
                                                return
                                        FILA_N = 0
                                        arch.close()
                                        arch = open(tabla+'.csv','r')
                                        for linea in arch:
                                                FILA = linea.strip().split(',')
                                                for x in lista_cumple:
                                                        for elemento in FILA:
                                                                for col in columnas:
                                                                        if x == FILA_N and FILA.index(elemento) == lista_col.index(col):
                                                                                lista_elementos.append(elemento)
                                                                        if len(lista_elementos) == len(columnas):
                                                                                lista_filas.append('  '.join(lista_elementos))
                                                                                lista_elementos = []
                                                FILA_N += 1
                                        for x in lista_filas:
                                                print(x)
                                #---------------Se imprimen todas las columnas---------------
                                else:
                                        lista_elementos = []
                                        lista_filas = []
                                        FILA = []
                                        cumple = 0
                                        lista_cumple = []
                                        FILA_N = 0
                                        #---------------Creo una lista con las posiciones de las filas que cumplen la condicion---------------#
                                        for linea in arch:
                                                FILA = linea.strip().split(',')
                                                for bloqueOR in otros[1]:
                                                        for elemento in FILA:
                                                                for bloqueAND in bloqueOR:
                                                                        And = re.split(r'=',bloqueAND)
                                                                        if And[1].strip() == elemento and And[0].strip() == lista_col[FILA.index(elemento)]:
                                                                                cumple+=1
                                                        if cumple == len(bloqueOR):
                                                                lista_cumple.append(FILA_N)
                                                        cumple = 0
                                                FILA_N += 1
                                        FILA_N = 0
                                        if len(lista_cumple == 0):
                                                print('La informacion solicitada no existe.')
                                                arch.close()
                                                return
                                        for linea in arch:
                                                FILA = linea.strip().split(',')
                                                for x in lista_cumple:
                                                        if x == FILA_N:
                                                                lista_filas.append('  '.join(FILA))
                                                FILA_N += 1
                                        for x in lista_filas:
                                                print(x)
                #---------------Casos sin WHERE---------------                    
                else:
                        #---------------Casos con Order By---------------
                        if otros[2] != 'x':
                                #---------------Se imprimen ciertas columnas---------------
                                if '*' not in columnas:
                                        lista_elementos = []
                                        lista_filas = []
                                        FILA = []
                                        for linea in arch:
                                                FILA = linea.strip().split(',')
                                                for elemento in FILA:
                                                        for col in columnas:
                                                                if ((FILA.index(elemento) == lista_col.index(col)) and (elemento not in lista_col)):
                                                                        lista_elementos.append(elemento)
                                                                if len(lista_elementos) == len(columnas):
                                                                        lista_filas.append(lista_elementos)
                                                                        lista_elementos = []
                                        lista_filas_aux = []
                                        lista_elementos_aux = []
                                        for col in columnas: #ordeno el grupo elementos por el elemento que me pidan
                                                if col in otros[2]:
                                                        lugar = columnas.index(col)
                                                        for elementos in lista_filas:
                                                                for elemento in elementos:
                                                                        if elementos.index(elemento) == lugar:
                                                                                lista_elementos_aux.append(elemento)
                                                        if 'ASC' in otros[2]:
                                                                lista_elementos_aux = sorted(lista_elementos_aux)
                                                                for elemento in lista_elementos_aux:
                                                                        for elementos in lista_filas:
                                                                                if str(elemento) in elementos:
                                                                                        lista_filas_aux.append('  '.join(elementos))
                                                        else:
                                                                lista_elementos_aux = sorted(lista_elementos_aux,reverse=True)
                                                                for elemento in lista_elementos_aux:
                                                                        for elementos in lista_filas:
                                                                                if str(elemento) in elementos:
                                                                                        lista_filas_aux.append('  '.join(elementos))
                                        for x in lista_filas_aux:
                                                print(x)
                                #---------------Se imprimen todas las columnas---------------
                                else:
                                        lista_elementos = []
                                        lista_filas = []
                                        FILA = []
                                        for linea in arch:
                                                FILA = linea.strip().split(',')
                                                for elemento in FILA:
                                                        if elemento not in lista_col:
                                                                lista_elementos.append(elemento)
                                                        if len(lista_elementos) == len(lista_col):
                                                                lista_filas.append(lista_elementos)
                                                                lista_elementos = []
                                        lista_elementos_aux = []
                                        lista_filas_aux = []
                                        Ordenador = re.split(r' ',otros[2])[0]
                                        lugar = lista_col.index(Ordenador)
                                        for elementos in lista_filas:
                                                for elemento in elementos:
                                                        if elementos.index(elemento) == lugar:
                                                                lista_elementos_aux.append(elemento)
                                        if 'ASC' in otros[2]:
                                                lista_elementos_aux = sorted(lista_elementos_aux)
                                                for elemento in lista_elementos_aux:
                                                        for elementos in lista_filas:
                                                                if str(elemento) in elementos:
                                                                        lista_filas_aux.append('  '.join(elementos))
                                        else:
                                                lista_elementos_aux=sorted(lista_elementos_aux,reverse=True)
                                                for elemento in lista_elementos_aux:
                                                        for elementos in lista_filas:
                                                                if str(elemento) in elementos:
                                                                        lista_filas_aux.append('  '.join(elementos))
                                        for x in lista_filas_aux:
                                                print (x)
                        #---------------Casos sin Order By---------------
                        else:
                                #---------------Se imprimen ciertas columnas---------------
                                if '*' not in columnas:
                                        lista_elementos = []
                                        lista_filas = []
                                        FILA = []
                                        for linea in arch:
                                                FILA = linea.strip().split(',')
                                                for elemento in FILA:
                                                        for col in columnas:
                                                                if FILA.index(elemento) == lista_col.index(col) and elemento not in lista_col:
                                                                        lista_elementos.append(elemento)
                                                                if len(lista_elementos) == len(columnas):
                                                                        lista_filas.append('  '.join(lista_elementos))
                                                                        lista_elementos = []
                                        for x in lista_filas:
                                                print(x)
                                #---------------Se imprimen todas las columnas---------------
                                else:
                                        lista_elementos = []
                                        lista_filas = []
                                        for linea in arch:
                                                FILA = linea.strip().split(',')
                                                for elemento in FILA:
                                                        if elemento not in lista_col:
                                                                lista_elementos.append(elemento)
                                                                if len(lista_elementos) == len(lista_col):
                                                                        lista_filas.append('  '.join(lista_elementos))
                                                                        lista_elementos = []
                                        for x in lista_filas:
                                                print (x)
        #---------------Casos con INNER JOIN---------------
        else:
                arch2 = open(otros[0]+'.csv','r')
                lista_col2 = []
                j = 1
                for linea in arch2:
                        if j == 1:
                                lista_col2 = linea.strip().split(',')
                                j+=1
                arch2.close()
                arch2 = open(otros[0]+'.csv','r') 
                #---------------Casos con Order By---------------#    
                if otros[2] != 'x':
                        #---------------Se imprimen ciertas columnas---------------#
                        if '*' not in columnas:
                                lista_elementos = []
                                lista_filas = []
                                #---------------Creo una lista donde en cada posicion, estan todos las columnas de ambas tablas, que cumplen con la condicion---------------#
                                for bloqueOR in otros[1]:
                                        for bloqueAND in bloqueOR:
                                                And = re.split(r'=',bloqueAND)
                                                for x in arch:
                                                        linea = x.strip().split(',')
                                                        for elemento in linea:
                                                                for y in arch2:
                                                                        linea2 = y.strip().split(',')
                                                                        for elemento2 in linea2:
                                                                                for col in columnas:
                                                                                        if col in lista_col:
                                                                                                if elemento2 == elemento and elemento not in lista_col2 and elemento not in lista_col and linea.index(elemento) != lista_col.index(col) and linea.index(elemento) == lista_col.index(re.split(r'\.',And[0])[1].strip()) and linea2.index(elemento2) == lista_col2.index(re.split(r'\.',And[1])[1].strip()):
                                                                                                        lista_elementos.append(linea[lista_col.index(col)])
                                                                                                if len(lista_elementos) == len(columnas):
                                                                                                        lista_filas.append(lista_elementos)
                                                                                                        lista_elementos=[]
                                                                                        else:
                                                                                                if elemento2 == elemento and elemento not in lista_col and elemento not in lista_col2 and linea2.index(elemento2) != lista_col2.index(col) and linea.index(elemento) == lista_col.index(re.split(r'\.',And[0])[1].strip()) and linea2.index(elemento2) == lista_col2.index(re.split(r'\.',And[1])[1].strip()):
                                                                                                        lista_elementos.append(linea2[lista_col2.index(col)])
                                                                                                if len(lista_elementos) == len(columnas):
                                                                                                        lista_filas.append(lista_elementos)
                                                                                                        lista_elementos=[]
                                                                arch2.close()
                                                                arch2 = open(otros[0]+'.csv','r')
                                lista_filas_aux = []
                                lista_elementos_aux = []
                                for col in columnas: #ordeno el grupo elementos por el elemento que me pidan
                                        if col in otros[2]:
                                                lugar = columnas.index(col)
                                                for elementos in lista_filas:
                                                        for elemento in elementos:
                                                                if elementos.index(elemento) == lugar:
                                                                        lista_elementos_aux.append(elemento)
                                                if 'ASC' in otros[2]:
                                                        lista_elementos_aux = sorted(lista_elementos_aux)
                                                        for elemento in lista_elementos_aux:
                                                                for elementos in lista_filas:
                                                                        if str(elemento) in elementos:
                                                                                lista_filas_aux.append('  '.join(elementos))
                                                else:
                                                        lista_elementos_aux = sorted(lista_elementos_aux,reverse=True)
                                                        for elemento in lista_elementos_aux:
                                                                for elementos in lista_filas:
                                                                        if str(elemento) in elementos:
                                                                                lista_filas_aux.append('  '.join(elementos))
                                for x in lista_filas_aux:
                                        print(x)
                        #---------------Se imprimen todas las columnas---------------#
                        else:
                                lista_col2_1 = []
                                lineas = 0
                                for y in lista_col2:
                                        lista_col2_1.append(y)
                                for x in lista_col:
                                        if x in lista_col2:
                                                lista_col2_1.remove(x)
                                for linea in arch2:
                                        lineas += 1
                                arch2.close()
                                arch2 = open(otros[0]+'.csv','r')

                                lista_elementos = []
                                lista_elementos2 = []
                                lista_filas = []
                                lista_filas2 = []
                                #---------------Creo una lista donde en cada posicion, estan todos las columnas de ambas tablas, que cumplen con la condicion---------------#
                                for bloqueOR in otros[1]:
                                        for bloqueAND in bloqueOR:
                                                And = re.split(r'=',bloqueAND)
                                                for x in arch:
                                                        linea = x.strip().split(',')
                                                        for elemento in linea:
                                                                for y in arch2:
                                                                        linea2 = y.strip().split(',')
                                                                        for elemento2 in linea2:
                                                                                if elemento not in lista_col and elemento2 not in lista_col2:
                                                                                        if elemento == elemento2 and lista_col.index(re.split(r'\.',And[0])[1].strip()) == linea.index(elemento) and lista_col2.index(re.split(r'\.',And[1])[1].strip()) == linea2.index(elemento2):
                                                                                                lista_elementos.append(linea)
                                                                                                if len(lista_elementos) == len(columnas):
                                                                                                        lista_filas.append(lista_elementos)
                                                                                                        lista_elementos = []
                                                                                        for x in lista_col2_1:
                                                                                                if lista_col2.index(x) == linea2.index(elemento2):
                                                                                                        lista_elementos2.append(elemento2)
                                                                                                if len(lista_elementos2) == len(lista_col2_1) and len(lista_filas2) < lineas-1:
                                                                                                        lista_filas2.append(lista_elementos2)
                                                                                                        lista_elementos2 = []
                                                                arch2.close()
                                                                arch2 = open(otros[0]+'.csv','r')
                                arch.close()
                                arch = open(tabla+'.csv','r')
                                for linea in range(len(lista_filas)):
                                        lista_filas[linea].append(lista_filas2[linea])
                                lista_elementos_aux = []
                                for x in lista_col:
                                        if x in otros[2]:
                                                for archivos in lista_filas:
                                                        for archivo in archivos:
                                                                if lista_filas.index(archivo) == 0:
                                                                        for elemento in archivo:
                                                                                if lista_col.index(x) == archivo.index(elemento):
                                                                                        lista_elementos_aux.append(elemento)
                                for y in lista_col2_1:
                                        if y in otros[2]:
                                                for archivos in lista_filas:
                                                        for archivo in archivos:
                                                                if archivos.index(archivo) == 1:
                                                                        for elemento in archivo:
                                                                                if lista_col2_1.index(y) == archivo.index(elemento):
                                                                                                lista_elementos_aux.append(elemento)
                                lista_filas_aux = []
                                if 'ASC' in otros[2]:
                                        lista_elementos_aux = sorted(lista_elementos_aux)
                                        for elemento in lista_elementos_aux:
                                                for linea in lista_filas:
                                                        for archivo in linea:
                                                                if elemento in archivo:
                                                                        lista_filas_aux.append(linea)
                                else:
                                        lista_elementos_aux = sorted(lista_elementos_aux,reverse=True)
                                        for elemento in lista_elementos_aux:
                                                for linea in lista_filas:
                                                        for archivo in linea:
                                                                if elemento in archivo:
                                                                        lista_filas_aux.append(linea)
                                for x in lista_filas_aux:
                                        for y in x:
                                                x[x.index(y)] = '  '.join(y)
                                        print('  '.join(x))
                #---------------Casos sin Order By---------------#
                else:
                        #---------------Se imprimen ciertas columnas---------------#
                        if '*' not in columnas:
                                lista_elementos = []
                                lista_filas = []
                                for bloqueOR in otros[1]:
                                        for bloqueAND in bloqueOR:
                                                And = re.split(r'=',bloqueAND)
                                                print(And)
                                                print(re.split(r'\.',And[0])[1].strip())
                                                print(re.split(r'\.',And[1])[1].strip())
                                                for x in arch:
                                                        linea = x.strip().split(',')
                                                        for elemento in linea:
                                                                for y in arch2:
                                                                        linea2 = y.strip().split(',')
                                                                        for elemento2 in linea2:
                                                                                for col in columnas:
                                                                                        if col in lista_col:
                                                                                                if elemento2 == elemento and elemento not in lista_col2 and elemento not in lista_col and linea.index(elemento) != lista_col.index(col) and linea.index(elemento) == lista_col.index(re.split(r'\.',And[0])[1].strip()) and linea2.index(elemento2) == lista_col2.index(re.split(r'\.',And[1])[1].strip()):
                                                                                                        lista_elementos.append(linea[lista_col.index(col)])
                                                                                                if len(lista_elementos) == len(columnas):
                                                                                                        lista_filas.append(lista_elementos)
                                                                                                        lista_elementos=[]
                                                                                        else:
                                                                                                if elemento2 == elemento and elemento not in lista_col and elemento not in lista_col2 and linea2.index(elemento2) != lista_col2.index(col) and linea.index(elemento) == lista_col.index(re.split(r'\.',And[0])[1].strip()) and linea2.index(elemento2) == lista_col2.index(re.split(r'\.',And[1])[1].strip()):
                                                                                                        lista_elementos.append(linea2[lista_col2.index(col)])
                                                                                                if len(lista_elementos) == len(columnas):
                                                                                                        lista_filas.append(lista_elementos)
                                                                                                        lista_elementos=[]
                                                                arch2.close()
                                                                arch2 = open(otros[0]+'.csv','r')
                                for x in lista_filas:
                                        print('  '.join(x))
                        #---------------Se imprimen todas las columnas---------------#
                        else:
                                lista_col2_1 = []
                                lineas = 0
                                for y in lista_col2:
                                        lista_col2_1.append(y)
                                for x in lista_col:
                                        if x in lista_col2:
                                                lista_col2_1.remove(x)
                                for linea in arch2:
                                        lineas += 1
                                arch2.close()
                                arch2 = open(otros[0]+'.csv','r')

                                lista_elementos = []
                                lista_elementos2 = []
                                lista_filas = []
                                lista_filas2 = []
                                for bloqueOR in otros[1]:
                                        for bloqueAND in bloqueOR:
                                                And = re.split(r'=',bloqueAND)
                                                for x in arch:
                                                        linea = x.strip().split(',')
                                                        for elemento in linea:
                                                                for y in arch2:
                                                                        linea2 = y.strip().split(',')
                                                                        for elemento2 in linea2:
                                                                                if elemento not in lista_col and elemento2 not in lista_col2:
                                                                                        if elemento == elemento2 and lista_col.index(re.split(r'\.',And[0])[1]) == linea.index(elemento) and lista_col2.index(re.split(r'\.',And[1])[1]) == linea2.index(elemento2):
                                                                                                lista_elementos.append(linea)
                                                                                                if len(lista_elementos) == len(columnas):
                                                                                                        lista_filas.append(lista_elementos)
                                                                                                        lista_elementos = []
                                                                                        for x in lista_col2_1:
                                                                                                if lista_col2.index(x) == linea2.index(elemento2):
                                                                                                        lista_elementos2.append(elemento2)
                                                                                                if len(lista_elementos2) == len(lista_col2_1) and len(lista_filas2) < lineas-1:
                                                                                                        lista_filas2.append(lista_elementos2)
                                                                                                        lista_elementos2 = []
                                                                arch2.close()
                                                                arch2 = open(otros[0]+'.csv','r')
                                arch.close()
                                arch = open(tabla+'.csv','r')
                                for linea in range(len(lista_filas)):
                                        lista_filas[linea].append(lista_filas2[linea])
                                for x in lista_filas:
                                        for y in x:
                                                x[x.index(y)] = '  '.join(y)
                                        print('  '.join(x))
                arch2.close()        
        arch.close()

"""
ListArchivo
--------
Entradas:
String Nombre de la tabla.
--------
Salida:
Lista: lista que contiene el archivo.
--------
La funcion abre un archivo, para leerlo linea por linea, y cada linea se guarda en una lista
para luego ser retornada por la funcion
""" 

def ListArchivo(archivo):
        arch = open(archivo+'.csv','r')
        lista = []
        for linea in arch:
                lista.append(linea.strip().split(','))
        
        return lista

#INSERT INTO Estudiantes (Nombre,Rol,Telefono) VALUES ('Tu vieja','564831-7',13136969);
#UPDATE Notas SET Nota=54 WHERE Rol='201673557-4';
#SELECT Nombre , Nota FROM Notas;
#SELECT Nombre , Nota FROM Notas ORDER BY Nota ASC;
#SELECT Nombre , Nota FROM Notas ORDER BY Nota DESC;
#SELECT * FROM Notas;
#SELECT * FROM Notas ORDER BY ASC;
#SELECT * FROM Notas ORDER BY DESC;
#SELECT Nombre , Nota FROM Notas WHERE Nombre='Gabriel Carmona';
#SELECT Nombre , Nota FROM Notas WHERE Nombre='Gabriel Carmona' OR Nombre='Clemente Aguilar' ORDER BY Nota ASC; Creo que aqui se va a caer (me di cuenta escribiendo el comando)
#SELECT Nombre , Nota FROM Notas WHERE Nombre='Gabriel Carmona' ORDER BY Nota DESC;
#SELECT * FROM Notas WHERE Nombre='Gabriel Carmona';
#SELECT * FROM Notas WHERE Nombre='Gabriel Carmona' OR Nombre='Clemente Aguilar' ORDER BY Nota ASC; Creo que aqui se va a caer (me di cuenta escribiendo el comando)
#SELECT * FROM Notas WHERE Nombre='Gabriel Carmona' ORDER BY Nota DESC;
#SELECT Edad , Nota FROM Estudiantes INNER JOIN Notas WHERE Estudiantes.Rol = Notas.Rol;
#SELECT Edad , Nota FROM Estudiantes INNER JOIN Notas WHERE Estudiantes.Rol = Notas.Rol ORDER BY Nota ASC;
#SELECT Edad , Nota FROM Estudiantes INNER JOIN Notas WHERE Estudiantes.Rol = Notas.Rol ORDER BY Nota DESC;
#SELECT * FROM Estudiantes INNER JOIN Notas WHERE Estudiantes.Rol = Notas.Rol;
#SELECT * FROM Estudiantes INNER JOIN Notas WHERE Estudiantes.Rol = Notas.Rol ORDER BY Nota ASC;
#SELECT * FROM Estudiantes INNER JOIN Notas WHERE Estudiantes.Rol = Notas.Rol ORDER BY Nota DESC;




