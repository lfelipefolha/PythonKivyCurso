class Ret:
    def __init__(me):
        me.a = 0
        me.b = 0
    def area(me):
        return (me.a * me.b)
    def compr(me):
        return ((me.a *2) + (2* me.b))

r1 = Ret()
r1.a =10
r1.b =20

r2 = Ret()
r2.a =10
r2.b =230
print(r1.area(), id(r2.area))
print(r1.compr())
