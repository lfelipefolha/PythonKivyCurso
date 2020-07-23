class Ret:
    def __init__ (self, largura, altura):
        self.l = largura
        self.a = altura
    def area(self):
        return self.l*self.a
    def per(self):
        return((2*self.l)+(2*self.a))

r = Ret(50,60)
r2 = Ret(50,500)
print(r.area(), r.per())
