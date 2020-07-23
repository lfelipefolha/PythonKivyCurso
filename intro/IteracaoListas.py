'''N funciona
lista = [100, 200, 300, 400, 500]
for i in lista:
    lista[i] += 333
print (lista)

'''
lista = [222,333,444,555,66]
listind = [0,1 ,2,3,4]
for item in listind:
    lista[item] += 333
print(lista)

#outraforma
lista = [222,333,444,555,66]

for item in range(5):
    lista[item] += 333
print(lista)

#outraforma
lista = [222,333,444,555,66]

for item in range(len(lista)):
    lista[item] += 333
print(lista)

 #outraformaENUMERATE
lista = [222,333,444,555,66]

for idx, item in enumerate(lista):
    lista[idx] += 333
print(lista)


