import re
from funciones import *

entrada = 'xS'
###
s = r'SELECT *([^\x20]+ *(?: *, *[^\x20]+ *)*) *FROM ([^\x20]+ *);?'
i = r'(?: *INNER *JOIN *([^\x20]+))'
w = r'(?: *WHERE *((?:[^\x20]+ *= *[^\x20]+|[^\x20]+ *= *\'[^\27]+\')(?: *(?:AND|OR) *(?:[^\x20]+ *= *[^\x20]+|[^\x20]+ *= *\'[^\27]+\'))*);?)'#les quite el ()?     #Le puse un :? al (AND|OR)
o = r'(?: *ORDER *BY *([^\x20]+ *(?:ASC|DESC));?)'
select = re.compile(s+i+r'?'+w+r'?'+o+r'?')
###
ii = r'INSERT *INTO *([^\x20]+) *\(([^\x20]+(,[\x20]+)*)\)'
v = r' *VALUES *\(((?:[^\x20]+|(?:\'[^\x27]+\'))(?: *, *(?:[^\x20]+|(?:\'[^\x27]+\')))*)\);'
insert = re.compile(ii+v)
###
u = r'UPDATE *([^\x20]+) *SET *([^\x20]+ *= *[\x00-\x7F]+(?:, *[^\x20]+ *= *[\x00-\x7F]+)*)'
wh = r' *WHERE *([^\x20]+ *= *[\x00-\x7F]+(?: *(?:AND|OR) *[^\x20]+ *= *[\x00-\x7F]+))*;'
update = re.compile(u+wh)
###
while entrada != 'salir':
    mach = 0
    entrada = input()

    if re.match(select,entrada):###### OJO QUE ESTA WEA FIJO TIRA ERROR, Y ACTUALMENTE NADA ES OPCIONAL
        mach = select.search(entrada)
        columnas = re.match(s,entrada).group(1).replace(' ','').split(',')#Lista de strings
        print('Columnas: ',columnas)
        tabla = re.match(s,entrada).group(2)#Un string
        print('Tabla: ',tabla)
        otros = []
        if re.search(i, entrada):
            union = re.search(re.compile(i), entrada).group(1)#Un string
            print('Union: ',union)
            otros.append(union)
        else:
            otros.append('x')
        if re.search(w, entrada):
            conds = re.search(re.compile(w), entrada).group(1)#Lista de listas, cada sub-lista es un or y en cada una van los ANDs (Nombre = algo)
            c = condSplit(conds)
            print('Condiciones: ',c)
            otros.append(c)
        else:
            otros.append('x')
        if re.search(o, entrada):
            orden = re.search(re.compile(o), entrada).group(1) #Un string
            print('Orden: ',orden)
            otros.append(orden)
        else:
            otros.append('x')
        print(otros)


    if insert.search(entrada):
        mach = insert.search(entrada)
        tabla = mach.group(1)
        print(tabla)
        columnas = mach.group(2).replace('(','').replace(')','').split(',')
        print(columnas)
        valores = mach.group(4).replace('(','').replace(')','').split(',')
        print(valores)
        #¿Cambio los tipos de valores?
        if len(columnas) != len(valores):
            print('Error de sintaxis. Comando no valido.')

    elif update.search(entrada):
        mach = re.search(update, entrada)
        tabla = re.search(update, entrada).group(1)#Un string
        print('Tabla: ',tabla)
        cambios = re.search(update, entrada).group(2).split(',')#Lista de strings (Nomnre = algo)
        print('Cambios: ',cambios)
        conds = re.search(update, entrada).group(3)#Lista de listas, cada sub-lista es un or y en cada una van los ANDs (Nombre = algo)
        c = condSplit(conds)
        print('Condiciones: ',c)

    elif not mach and entrada!='salir':
        print('Error de sintaxis. Comando no valido.')
