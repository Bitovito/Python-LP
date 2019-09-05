import re

def condSplit(conds):
    lista=[]
    q = conds.split('OR')
    for c in q:
        x = c.split('AND')
        lista.append(x)
    return lista

def selectSelect (columnas, tabla, otros):
    file = open(tabla+'.csv','r')
    if otros[0] == 'x':                             #si no hay INNER JOIN
        if otros[1] != 'x':                         #si no hay INNER JOIN y hay WHERE
            if otros[2] != 'x':                     #si no hay INNER JOIN y hay WHERE y hay ORDER BY
                print('xd')
            else:                                   #si no hay INNER JOIN y hay WHERE y no hay ORDER BY
                print('xd')
        else:
            if otros[2] != 'x':                     #si no hay INNER JOIN y no hay WHERE y hay ORDER BY
                print('xd')
            else:                                   #si no hay INNER JOIN y no hay WHERE y no hay ORDER  SIMPLE
                print('xd')
    else:
        arch2 = otros[0]
        otherFile = open(arch2+'csv','r')   
        print('xd')
        if otros[2] != 'x':                     #si hay INNER JOIN y hay ORDER BY
            print('xd')
        else:                                   #si hay INNER JOIN y no hay ORDER BY
            print('xd')

    print('xd')
    
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
        lista.append(linea.strip().split(','))
    arch.close()
    lista_col = lista_arch[0]
    cumple = 0
    lista_cumple = []
    arch = open('Alumnos.csv','r')
    for linea in lista_arch:
        for bloqueOR in cond:
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
    print('Se ha(n) actualizado'+str(len(lista_cumple)+'fila(s)')
    return
