import re

def condSplit(conds):
    lista=[]
    q = conds.split('OR')
    for c in q:
        x = c.split('AND')
        lista.append(x)
    return lista
    
def INSERT(tabla,columna,valores):
    arch = open(tabla+".csv",'r')
    lista_col = []
    i = 1
    col_aux = []
    val_aux = []
    for linea in arch:
        if i == 1:
            lista_col = linea.strip().split(',')
            i+=1
    arch.close()
    for x in lista_col:
        for y in columna:             
            if y == x:
                col_aux.append(y)
                val_aux.append(valores[columna.index(y)])
        if (x not in columna):
            val_aux.append(' ')
    arch = open(tabla+".csv",'a')
    a = ','.join(val_aux)
    arch.write(a)
    arch.write('\n')
    
    arch.close()
    print('Se ha insertado 1 fila')
    return

def UPDATE(tabla,cambios,conds):
    arch = open(tabla+".csv",'r')
    lista_arch = []
    for linea in arch:
        lista_arch.append(linea.strip().split(','))
    arch.close()
    lista_col = lista_arch[0]
    cumple = 0
    lista_cumple = []
    arch = open('Alumnos.csv','r')
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
    arch.close()
    arch = open('Alumnos.csv','w')
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
    print('Se ha(n) actualizado'+str(len(lista_cumple)+'fila(s)'))
    return









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
        print(lista_col)
        print (columnas)
        print(otros)
        if otros[0] == 'x':                             #si no hay INNER JOIN
                if otros[1] != 'x':                         #si no hay INNER JOIN y hay WHERE
                        if otros[2] != 'x':                     #si no hay INNER JOIN y hay WHERE y hay ORDER BY
                                if '*' not in columnas:
                                        lista_elementos = []
                                        lista_filas = []
                                        lista_elementos_aux = []
                                        lista_filas_aux = []
                                        FILA = []
                                        cumple = 0
                                        lista_cumple = []
                                        FILA_N = 0
                                        for linea in arch:
                                                FILA = linea.strip().split(',')
                                                for bloqueOR in otros[1]:
                                                        for elemento in FILA:
                                                                for bloqueAND in bloqueOR:
                                                                        And = re.split(r'=',bloqueAND)
                                                                        print('elemento = '+str(elemento))
                                                                        print('valor condicion = '+str(And[1].strip()))
                                                                        if And[1].strip() == elemento and And[0].strip() == lista_col[FILA.index(elemento)]:
                                                                                cumple+=1
                                                        if cumple == len(bloqueOR):
                                                                lista_cumple.append(FILA_N)
                                                        cumple = 0
                                                FILA_N += 1
                                        FILA_N = 0
                                        arch.close()
                                        arch = open(tabla+'.csv','r')
                                        print(lista_cumple)
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
                                        for col in columnas: #ordeno el grupo elementos por el elemento que me pidan
                                                if col in otros[2]:
                                                        lugar = columnas.index(col)
                                                        for elementos in lista_filas:
                                                                for elemento in elementos:
                                                                        if elementos.index(elemento) == lugar:
                                                                                lista_elementos_aux.append(elemento)
                                                        if 'ASC' in otros[2]:
                                                                lista_elementos_aux.sort().reverse()
                                                                for elemento in lista_elementos_aux:
                                                                        for elementos in lista_filas:
                                                                                if elemento in elementos:
                                                                                        lista_filas_aux.append('  '.join(elementos))
                                                        else:
                                                                lista_elementos_aux.sort()
                                                                for elemento in lista_elementos_aux:
                                                                        for elementos in lista_filas:
                                                                                if elemento in elementos:
                                                                                        lista_filas_aux.append('  '.join(elementos))
                                        print(lista_filas_aux)
                                        print(lista_elementos_aux)
                                        for x in lista_filas_aux:
                                                print(x)
                                else:
                                        lista_elementos = []
                                        lista_filas = []
                                        lista_elementos_aux = []
                                        lista_filas_aux = []
                                        FILA = []
                                        cumple = 0
                                        lista_cumple = []
                                        FILA_N = 0
                                        for linea in arch:
                                                FILA = linea.strip().split(',')
                                                for bloqueOR in otros[1]:
                                                        for elemento in FILA:
                                                                for bloqueAND in bloqueOR:
                                                                        And = re.split(r'=',bloqueAND)
                                                                        print('elemento = '+str(elemento))
                                                                        print('valor condicion = '+str(And[1].strip()))
                                                                        if And[1].strip() == elemento and And[0].strip() == lista_col[FILA.index(elemento)]:
                                                                                cumple+=1
                                                        if cumple == len(bloqueOR):
                                                                lista_cumple.append(FILA_N)
                                                        cumple = 0
                                                FILA_N += 1
                                        FILA_N = 0
                                        arch.close()
                                        arch = open(tabla+'.csv','r')
                                        for linea in arch:
                                                FILA = linea.strip().split(',')
                                                for x in lista_cumple:
                                                        if x == FILA_N:
                                                                lista_filas.append(FILA)
                                                FILA_N += 1
                                        lista_elementos_aux = []
                                        lista_filas_aux = []
                                        Ordenador = re.split(r' ',otros[2])[0]
                                        lugar = lista_col.index(Ordenador)
                                        for elementos in lista_filas:
                                                for elemento in elementos:
                                                        if elementos.index(elemento) == lugar:
                                                                lista_elementos_aux.append(elemento)
                                        if 'ASC' in otros[2]:
                                                lista_elementos_aux.sort().reverse()
                                                for elemento in lista_elementos_aux:
                                                        for elementos in lista_filas:
                                                                if elemento in elementos:
                                                                        lista_filas_aux.append('  '.join(elementos))
                                        else:
                                                lista_elementos_aux.sort()
                                                for elemento in lista_elementos_aux:
                                                        for elementos in lista_filas:
                                                                if elemento in elementos:
                                                                        lista_filas_aux.append('  '.join(elementos))
                                        for x in lista_filas_aux:
                                                print (x)
                                        
                        else:                                   #si no hay INNER JOIN y hay WHERE y no hay ORDER BY LISTOO
                                if '*' not in columnas:
                                        lista_elementos = []
                                        lista_filas = []
                                        FILA = []
                                        cumple = 0
                                        lista_cumple = []
                                        FILA_N = 0
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
                                        print(lista_filas)
                                        for x in lista_filas:
                                                print(x)
                                else:
                                        lista_elementos = []
                                        lista_filas = []
                                        FILA = []
                                        cumple = 0
                                        lista_cumple = []
                                        FILA_N = 0
                                        for linea in arch:
                                                FILA = linea.strip().split(',')
                                                for bloqueOR in otros[1]:
                                                        for elemento in FILA:
                                                                for bloqueAND in bloqueOR:
                                                                        And = re.split(r'=',bloqueAND)
                                                                        print('AND = '+str(And))
                                                                        print('elemento = '+str(elemento))
                                                                        #print ('valor de la condicion = '+str(And[1].strip))
                                                                        if And[1].strip() == elemento and And[0].strip() == lista_col[FILA.index(elemento)]:
                                                                                cumple+=1
                                                        if cumple == len(bloqueOR):
                                                                lista_cumple.append(FILA_N)
                                                        cumple = 0
                                                FILA_N += 1
                                        FILA_N = 0
                                        print(lista_cumple)
                                        for linea in arch:
                                                FILA = linea.strip().split(',')
                                                for x in lista_cumple:
                                                        if x == FILA_N:
                                                                lista_filas.append(FILA)
                                                FILA_N += 1
                                        for x in lista_filas:
                                                print('  '.join(x))
                                                
                else:
                        if otros[2] != 'x':                     #si no hay INNER JOIN y no hay WHERE y hay ORDER BY LISTO Y PROBADO
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
                                                                lista_elementos_aux.sort().reverse()
                                                                for elemento in lista_elementos_aux:
                                                                        for elementos in lista_filas:
                                                                                if elemento in elementos:
                                                                                        lista_filas_aux.append('  '.join(elementos))
                                                        else:
                                                                lista_elementos_aux.sort()
                                                                for elemento in lista_elementos_aux:
                                                                        for elementos in lista_filas:
                                                                                if elemento in elementos:
                                                                                        lista_filas_aux.append('  '.join(elementos))
                                        for x in lista_filas_aux:
                                                print(x)
                                        
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
                                                lista_elementos_aux.sort().reverse()
                                                for elemento in lista_elementos_aux:
                                                        for elementos in lista_filas:
                                                                if elemento in elementos:
                                                                        lista_filas_aux.append('  '.join(elementos))
                                        else:
                                                lista_elementos_aux.sort()
                                                for elemento in lista_elementos_aux:
                                                        for elementos in lista_filas:
                                                                if elemento in elementos:
                                                                        lista_filas_aux.append('  '.join(elementos))
                                        for x in lista_filas_aux:
                                                print (x)
                                        
                                        

                        else:                                   #si no hay INNER JOIN y no hay WHERE y no hay ORDER  SIMPLE LISTOOOOOO y PROBADO
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
        else:
                arch2 = otros[0]
                otherFile = open(arch2+'csv','r')   
                print('xd')
                if otros[2] != 'x':                     #si hay INNER JOIN y hay ORDER BY
                        print('xd')
                else:                                   #si hay INNER JOIN y no hay ORDER BY
                        print('xd')

                print('xd')

def ListArchivo(archivo):
        arch = open(archivo+'.csv','r')
        lista = []
        for linea in arch:
                lista.append(linea.strip().split(','))
        
        return lista
