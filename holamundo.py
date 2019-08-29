import re
count=0
#while count<5:
entrada = input('\n')

#select = re.compile(r'SELECT\s([A-Z]+(,\s\w+)*|\*)\sFROM\s([A-Z]+)(\sINNER\sJOIN\s([A-Z]+))?(\sWHERE\s([A-Z]+\s=\s\w+)((AND|OR)\s([A-Z]+\s=\s\w+))*(\sORDER\sBY\s([A-Z]\s(ASC|DESC)))?')

select = re.compile(r'SELECT\s([A-Za-z]+(,\s[A-Za-z]+)*|\*)\sFROM\s([A-Za-z]+)    (\sINNER\sJOIN\s([A-Za-z]+))?      ( \sWHERE\s ([A-Za-z]\s=\s\w+|[A-Za-z]\s=\s[A-Za-z])  ((AND|OR)([A-Za-z]\s=\s\w+|[A-Za-z]\s=\s[A-Za-z]))*    )?      (\sORDER\sBY\s([A-Za-z]+)\s(ASC|DESC))?      ')

insert = re.compile(r'INSERT\sINTO\s([A-Z]+)\s(\([A-Z]+(,\s[A-Z]+)*\))\sVALUES\s(\(\w+(,\s\w+)*\));')
#                     INSERT  INTO    TABLA     (NOMBRE, APELLIDO, CASA)   VALUES    (JUAN, CHI, OMEGA);
update = re.compile(r'UPDATE\s([A-Za-z]+)\sSET\s([A-Za-z]+\s=\s\w+(,\s[A-Z]+\s=\s\w+)*)\sWHERE\s\w+\s=\s\w+(\s(AND|OR)\s\w+\s=\s\w+)*;')

mach = update.search(entrada)
x = mach
print (x,'\n')
#
#INSERT = (r'INSERT\sINTO\s[A-Z]+\s\([A-Z]((,\s[A-Z]+)*\)')
#         (r'VALUES\s\(\w+((,\s[A-Z])*\);')
#UPDATE = (r'UPDATE\s[A-Z]+')
#         (r'SET\s[A-Z]+\s=\s\w+((,\s[A-Z]+\s=\s\w+)*')
#         (r'WHERE\s[A-Z]+\s=\s\w+\s((AND\s[A-Z]+\s=\s\w+|OR\s[A-Z]\s=\s\w+)*;')
#\sSET\s([A-Za-z]+\s=\s\w+(,[A-Z]+\s=\s\w+)*)\sWHERE\s([A-Z]+\s=\s\w+((\sAND\s[A-Z]+\s=\s\w+)|(\sOR\s[A-Z]\s=\s\w+))*);
