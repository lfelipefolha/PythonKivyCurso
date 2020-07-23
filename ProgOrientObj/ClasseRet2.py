class Retangulo:
    def area(self):
        return self.a*self.l

def membro_retangulo(r):
    r.a = 0
    r.l = 0

r1 = Retangulo()
membro_retangulo(r1)
r1.l=10
r1.a=5

print(r1.area())
