class Bichos:
    qnt_bichos = 0
    def __init__(self):
        self.add_bichos()
    def __del__(self):
        self.del_bichos()
        if (self.qnt_bichos==0):
            print("Tudo morto")

    @classmethod
    def add_bichos(cls):
        cls.qnt_bichos+=1
    @classmethod
    def del_bichos(cls):
        cls.qnt_bichos-=1
    #add_bichos = classmethod(add_bichos)
    #del_bichos = classmethod(del_bichos)

b1 = Bichos()

b2 = Bichos()
print(b2.add_bichos())
del (b1)
print(Bichos.qnt_bichos)
del (b2)
print(Bichos.qnt_bichos)
