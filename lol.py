import re
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
    return ('Se ha insertado 1 fila')

def condSplit(conds):
    lista=[]
    q = conds.split('OR')
    for c in q:
        x = c.split('AND')
        lista.append(x)
    return lista
entrada = 'xS'
#c = '(\s[!-~])'
s = r'SELECT\s(\w+(?:,\s\w+)*|\*)\sFROM\s(\w+)'
i = r'(?:\sINNER\sJOIN\s(\w+))'
w = r'(?:\sWHERE\s((?:\w+\s=\s\w+)(?:\s(?:AND|OR)\s\w+\s=\s\w+)*))'#les quite el ()?     #Le puse un :? al (AND|OR)
o = r'(?:\sORDER\sBY\s(\w+\s(?:ASC|DESC)))'
select = re.compile(s+i+r'?'+w+r'?'+o+r'?')
###
ii = r'INSERT\sINTO\s(\w+)\s\((\w+(,\w+)*)\)'
v = r'\sVALUES\s\((\w+(,\w+)*)\);'
insert = re.compile(ii+v)
###
u = r'UPDATE\s(\w+)\sSET\s(\w+\s=\s\w+(,\w+\s=\s\w+)*)'
wh = r'\sWHERE\s(\w+\s=\s\w+(\s(AND|OR)\s\w+\s=\s\w+))*;'
update = re.compile(u+wh)
###
while entrada != 'salir':
    mach = 0
    entrada = input()

    if select.search(entrada):###### OJO QUE ESTA WEA FIJO TIRA ERROR, Y ACTUALMENTE NADA ES OPCIONAL
        mach = select.search(entrada)
        columnas = re.search(re.compile(s), entrada).group(1).split(', ')
        print(columnas)
        tabla = re.search(re.compile(s), entrada).group(2)
        print(tabla)
        if re.search(i, entrada):
            union = re.search(re.compile(i), entrada).group(1)
            print(union)
        if re.search(w, entrada):
            conds = re.search(re.compile(w), entrada).group(1)
            c = condSplit(conds)
            print(c)
        if re.search(o, entrada):
            orden = re.search(re.compile(o), entrada).group(1)
            print(orden)

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
        tabla = re.search(re.compile(u), entrada).group(1)
        print(tabla)
        cambios = re.search(re.compile(u), entrada).group(2)
        print(cambios)
        conds = re.search(re.compile(wh), entrada).group(1)
        c = condSplit(conds)
        print(c)

    elif not mach and entrada!='salir':
        print('Error de sintaxis. Comando no valido.')
