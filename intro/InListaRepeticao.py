cores = ["azul","verde","vermelho","amarelo"]
while True:
    cor = input("Digite uma cor ou 0 para sair")
    if cor == '0':
        print("pode crer")
        break
    elif cor in cores:
        print("Contido")
    else:
        print("nao contido")
    
