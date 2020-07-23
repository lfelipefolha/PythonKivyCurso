def testenonlocal (x,y):

    def teste():
        nonlocal x
        nonlocal y
        
        print (x+y)
    teste()

testenonlocal(10,30)

xx=20

def testeglobal():
    global xx
    xx *=30
    return xx

print(testeglobal())
