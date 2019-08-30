import re
entrada = 'x'
#c = '(\s[!-~])'
s = r'SELECT\s(\w+(,\s\w+)*|\*)\sFROM\s(\w+)'
i = r'(\s(INNER\sJOIN)\s(\w+))?'
w = r'((\sWHERE\s(\w+\s=\s\w+)((AND|OR)\s(\w+\s=\s\w+))*)?'
o = r'(\s(ORDER\sBY)\s([A-Z]\s(ASC|DESC))))?'
select = re.compile(s+i+w+o)
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

    if select.search(entrada):
        mach = select.search(entrada)
        columnas = mach.group(1).split(', ')
        tabla = mach.group(3)
        #conds = (w.search(entrada)).group(5)
        #print(conds)
        #¿Cambio los tipos de columnas y tabla?

    if insert.search(entrada):
        mach = insert.search(entrada)
        tabla = mach.group(1)
        columnas = mach.group(2).split(',')
        valores = mach.group(4).split(',')
        print(tabla,columnas,valores)
        #¿Cambio los tipos de valores?
        if len(columnas) != len(valores):
            print('Error de sintaxis. Comando no valido.')

    elif update.search(entrada):
        mach = update.search(entrada)
        tabla = mach.group(1)
        cambios = mach.group(2).split(',')
        conds = mach.group(4)

    elif not mach and entrada!='salir':
        print('Error de sintaxis. Comando no valido.')
