def pessoa(nome, sobrenome, idade):
    print(nome, sobrenome , idade)
lista = ["Luiz", "Felipe", 21]
d = {"nome":"Joao", "idade":21, "sobrenome":"Folha"}

pessoa(**d)
print(20*"--")
pessoa(*lista)
