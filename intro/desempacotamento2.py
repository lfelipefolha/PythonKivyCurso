lista = [11, 10, 12]
def func(a,b,c):
    print(a, b, c)


func(**dict(zip(('b','a','c'), lista)))
