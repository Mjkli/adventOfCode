import re
from collections import OrderedDict
#f = open(r'test.txt','r')
f = open(r'input.txt','r')

one = []

totalnum = 0

while 1:
    char = f.read(1)
    if not char:
        break
    
    if len(one) == 14:
        break
    
    if char in one:
        for iter in range(0,len(one)):
            if char in one:
                one.pop(0)

    one.append(char)
    totalnum += 1
    print(one)
    print(totalnum)



print(list)

f.close()