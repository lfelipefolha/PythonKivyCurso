def lista_de_argumentos (*args):
    print(args)
print (10*"-")
def lista_de_argumentos_associativos(**kwargs):
    print (kwargs)
def argumentos (*args, **kwargs):
    print (args, 20*"--", kwargs)

lista_de_argumentos (1, 2, 3, "bartender")
print (10*"-")
lista_de_argumentos_associativos(um = 1, dois =2, tres =3)
argumentos (1, 2,3,5, aaaa=222)

