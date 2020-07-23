#iterando string EX1
'''
s = 'iterando string'
c=0
for i in s:
    c+=1
    print(c-1, i)'''

#EX2
'''
s = 'iterando string'
indice=0
while indice < len(s):
    print(indice, s[indice])
    indice+=1
'''

#EX3
s = 'iterando string'
for key, val in enumerate(s):
    print(key, val)

print(dict(enumerate(s)))
