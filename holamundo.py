import re
count=0
while count<5:
    entrada = input('\n')

    instruccion = re.compile(r'SELECT\s([A-Z]+((,\s\w+)+)?|\*)\sFROM\s[A-Z]+')

    recibido = instruccion.search(entrada)

    print (recibido)

    count+=1

input()
#SELECT\s((\w+(,\s\w+)+?)|*)