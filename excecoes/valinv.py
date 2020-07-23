def inpt(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("invalido")
def divz(msg2):
    while True:
        try:
            return(float(input(msg2)))
        except ZeroDivisionError:
            print ("nao pode")
        except ValueError:
            print("invalido")
       
n1 = inpt(("N1"))
n2 = divz(("N2"))
while (n2==0):
    n2 = divz(("N2"))
print(n1/n2)

