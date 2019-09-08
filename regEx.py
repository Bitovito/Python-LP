import re
from funciones import *

entrada = 'xS'
# A continuacion divido la expresion regular en distintos trozos para mayor facilidad de lectura
s = r'SELECT *([^\x20]+ *(?: *, *[^\x20]+ *)*) *FROM ([^\x20]+) *;?'
i = r'(?: *INNER *JOIN *([^\x20]+);?)'
w = r'(?: *WHERE *((?:[^\x20]+ *= *\'[^\27]+\'|[^\x20]+ *= *[^\x20]+)(?: *(?:AND|OR) *(?:[^\x20]+ *= *\'[^\27]+\'|[^\x20]+ *= *[^\x20]+))*);?)'#les quite el ()?     #Le puse un :? al (AND|OR)
o = r'(?: *ORDER *BY *([^\x20]+ *(?:ASC|DESC));?)'
select = re.compile(s+i+r'?'+w+r'?'+o+r'?')
###
ii = r'INSERT *INTO *([^\x20]+) *\(([^\x20]+(,[\x20]+)*)\)'
v = r' *VALUES *\(((?:[^\x20]+|(?:\'[^\x27]+\'))(?: *, *(?:[^\x20]+|(?:\'[^\x27]+\')))*)\);'
insert = re.compile(ii+v)
###
u = r'UPDATE *([^\x20]+) *SET *([^\x20]+ *= *[\x00-\x7F]+(?:, *[^\x20]+ *= *[\x00-\x7F]+)*)'
wh = r' *WHERE *([^\x20]+ *= *[\x00-\x7F]+(?: *(?:AND|OR) *[^\x20]+ *= *[\x00-\x7F]+)*);'
update = re.compile(u+wh)
###
# Ahora hago un ciclo while donde uno puede ingresar su Query mediante el input,
# esto revisa si la query ingresada pertenece a los tipos propuestos, luego depuro
# los datos y los envio a las funciones respectivas.
while entrada != 'salir':
    mach = 0
    entrada = input()
# Depuro los datos de SELECT, los datos opcionales como INNER JOIN 
# los paso a una lista, donde si no es pedido se marca como una x para
# evitar problemas con el paso de parametros.
# Si no hay condicion cuando se pide un INNER JOIN tira error.
    if re.match(select,entrada):
        mach = select.search(entrada)
        columnas = re.match(s,entrada).group(1).replace(' ','').split(',')#Lista de strings
        tabla = re.match(s,entrada).group(2).strip(';')#Un string
        otros = []
        if re.search(i, entrada):
            union = re.search(re.compile(i), entrada).group(1).strip(';')#Un string
            otros.append(union)
        else:
            otros.append('x')
        if re.search(w, entrada):
            conds = re.search(re.compile(w), entrada).group(1).strip(';')#Lista de listas, cada sub-lista es un or y en cada una van los ANDs (Nombre = algo)
            c = condSplit(conds)
            otros.append(c)
        else:
            otros.append('x')
        if re.search(o, entrada):
            orden = re.search(re.compile(o), entrada).group(1).strip(';')#Un string
            otros.append(orden)
        else:
            otros.append('x')
        if otros[0] != 'x' and otros[1] == 'x':
            print('Error de sintaxis. Comando no valido.')
        else:
            Select(columnas,tabla,otros)

# Depuro los datos de INSERT, si la cantidad de valores es
# mayor que las columnas a insertar tira error.
    if insert.search(entrada):
        mach = insert.search(entrada)
        tabla = mach.group(1)
        columnas = mach.group(2).replace('(','').replace(')','').split(',')
        valores = mach.group(4).replace('(','').replace(')','').split(',')
        if len(columnas) != len(valores):
            print('Error de sintaxis. Comando no valido.')
        INSERT(tabla,columnas,valores)
# Depuro los datos en update.
    elif update.search(entrada):
        mach = re.search(update, entrada)
        tabla = re.search(update, entrada).group(1)#Un string
        cambios = re.search(update, entrada).group(2).split(',')#Lista de strings (Nomnre = algo)
        conds = re.search(update, entrada).group(3)#Lista de listas, cada sub-lista es un or y en cada una van los ANDs (Nombre = algo)
        c = condSplit(conds)
        UPDATE(tabla,cambios,c)
# Si la query es invalida y distinta de salir lanza mensaje de error.
    elif not mach and entrada!='salir':
        print('Error de sintaxis. Comando no valido.')
