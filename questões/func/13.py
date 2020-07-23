def invert():
    lista2=[]
    lista = '1234abcd'
    print(lista)
    for i in range(7, 0, -1):
        print(lista[i])
        lista2.append(lista[i])
    print(str(lista2))
invert()
