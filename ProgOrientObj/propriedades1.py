class A:
    def __init__(self):
        self._var = 0
    @property
    def var(self ):
        print("O valor foi lido")
        return self._var
    @var.setter 
    def var(self, x):
        print("Valor sendo escrito")
        self._var = x

   # var  = property(fget=_get_var, fset=_set_var)
a = A()
a.var = 10
t = a.var