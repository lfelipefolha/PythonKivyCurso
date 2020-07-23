def testenonlocal ():
    x= 10
    def teste():
        nonlocal x
        x+=1
        print (x)
    teste()

testenonlocal()

xx=20

def testeglobal():
    global xx
    xx *=30
    return xx

print(testeglobal())
