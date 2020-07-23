def fc(x):
    try:
        eval(x)
        print(eval(x))
    except TypeError as e:
        print("typeerror")
        print(type(e))
        print(e.args)
        print(e)
    except ZeroDivisionError as e:
        print("divzero")
        print(type(e))
        print(e.args)
        print(e)
    except ValueError as e:
        print("ValueError")
        print(type(e))
        print(e.args)
        print(e)
    except NameError as e:
        print ("NsmeErrror")
        print(type(e))
        print(e.args)
        print(e)
                
#TypeError
fc("int+int")
#ZeroDivisionError
fc("5/0")
#NameError
fc("a")
#valueError
fc("int('a')")
fc("float(20/15)")
