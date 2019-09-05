import re

def condSplit(conds):
    lista=[]
    q = conds.split('OR')
    for c in q:
        x = c.split('AND')
        lista.append(x)
    return lista

def selectSelect (columnas, tabla, otros):
    if otros[0] == 'x':#si no hay INNER JOIN
        file = open(tabla+'.csv','r')
        
        
        print('x')

    print('xd')