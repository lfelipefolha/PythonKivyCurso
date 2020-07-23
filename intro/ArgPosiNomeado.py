def dados_pessoais(nome, sobrenome, idade, sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo {}"
          .format(nome, sobrenome, idade,sexo))
dados_pessoais("Joao", "Paulo", 36, True) #posicional
dados_pessoais(sobrenome="Leite", nome = "Joao", sexo = True, idade =34) #nomeado
