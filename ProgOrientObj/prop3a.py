class Retangulo:
    def __init__(self, largura, altura):
        self._largura = 0
        self._altura = 0
        self.__var = 0
        self._set_altura(altura)
        self._set_largura(largura)

    def _get_altura(self):
        return self._altura
        
    def _set_altura(self, num):
        if (not((isinstance(num, int))and (num > 0))):
            raise ValueError("A altura é invalida{}".format(num))
        self._altura = num
    def _get_largura(self):
        return self._largura
    def _set_largura(self, num):
        if(not((isinstance(num, int))and(num>0))):
            raise ValueError("A largura é invalida{}".format(num))
        self._largura = num
    def _get_area(self):
        return self._altura *self._largura

    altura = property(fget= _get_altura, fset=_set_altura)
    largura = property(fget= _get_largura, fset=_set_largura)
    area = property(fget=_get_area)

r = Retangulo(9098, 6)
r.largura = 10
r.altura = 25
r.area = 2002
print(r._get_area())
