def fc(x):
    try:
        eval(x)
        print(eval(x))
    except TypeError:
        print("typeerror")
    except ZeroDivisionError:
        print("divzero")
    except ValueError:
        print("ValueError")
    except NameError:
        print ("NsmeErrror")
                
#TypeError
fc("int+int")
#ZeroDivisionError
fc("5/0")
#NameError
fc("a")
#valueError
fc("int('a')")
fc("float(20/15)")
