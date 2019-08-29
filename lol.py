import re
entrada = 'x'

select = re.compile(r'SELECT\s([A-Z]+(,\s\w+)*|\*)\sFROM\s([A-Z]+)(\s(INNER\sJOIN)\s([A-Z]+))?((\sWHERE\s([A-Z]+\s=\s\w+)((AND|OR)\s([A-Z]+\s=\s\w+))*)?(\s(ORDER\sBY)\s([A-Z]\s(ASC|DESC))))?')
insert = re.compile(r'INSERT\sINTO\s([A-Z]+)\s\(([A-Z]+(,[A-Z]+)*)\)\sVALUES\s\((\w+(,\w+)*)\);')
update = re.compile(r'UPDATE\s([A-Z]+)\sSET\s([A-Z]+\s=\s\w+(,[A-Z]+\s=\s\w+)*)\sWHERE\s([A-Z]+\s=\s\w+(\s(AND|OR)\s[A-Z]+\s=\s\w+))*;')
#
while entrada != 'salir':

    entrada = input()
    """
    if select.search(entrada):
        mach = select.search(entrada)
        columnas = mach.group(1).split(', ')
        tabla = mach.group(2)
        print (mach)
        #¿Cambio los tipos de columnas y tabla?
"""
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
        cond = mach.group(4)

    elif entrada != 'salir':
        print('Error de sintaxis. Comando no valido.')
