def func():
    soma=0
    lista = [1, 2, 3, 4, 5]
    for i in range(len(lista)):
        soma += lista[i]
    print(soma)

func()
    
def func2():
    soma=0
    lista2 = [1, 2, 3, 4, 5]
    for i, idx in enumerate(lista2):
        soma += lista2[idx-1]
    print(soma)
    print (dict(enumerate(lista2)))

func2()
    
