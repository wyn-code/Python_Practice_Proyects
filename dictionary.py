dic = {'c1': 55, 'c2':[10,20,40], 'c3':{'s1':100, 's2':200}}

## Imprimo lo que haya en el index 1 dentro de una lista
print(dic['c2'][1])

## Imprimo lo que haya en el index dentro del diccionario
print(dic['c3']['s2'])

dic1 = {'q1': ['a','b','c'], 'q2': ['d','e','f']}
print(dic1['q2'][1].upper())

dic3 = {1:'a', 2:'b'}
print(dic3)

dic3[3] = 'c'
print(dic3)

## Sobreescribir
dic3[2] = 'B'
print(dic3)

print(dic3.keys())
print(dic3.values())
print(dic3.items())