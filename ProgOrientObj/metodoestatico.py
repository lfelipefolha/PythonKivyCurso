class Mestaticos:
    @staticmethod
    def func1():
        print("func1()")
    @staticmethod
    def func2(x, y):
        print("Função '{}' invocada.\nParams = ({} , {})".format("func2", x,y))
    @staticmethod
    def func3(a, b, c):
        info = """
        Nome da funcao: {nome}
        Qtd de args:{quantidade}
        Args = {args}
        """
        info =  info.format(
            nome = Mestaticos.func3.__name__,
            quantidade = Mestaticos.func3.__code__.co_argcount,
            args = Mestaticos.func3.__code__.co_varnames
        )
        print(info)
m1 = Mestaticos()
m1.func1()
m1.func2(100, 200)
m1.func3(100, 200, 300)