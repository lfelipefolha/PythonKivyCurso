import importlib
import mod_a

del(mod_a.a)
mod_a.b = 50
from pprint import pprint 
pprint(mod_a.__dict__)

print(30*'-')
importlib.reload(mod_a)

pprint(mod_a.__dict__)
