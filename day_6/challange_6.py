import re
from collections import OrderedDict
f = open(r'test.txt','r')
#f = open(r'input.txt','r')

one = OrderedDict()

totalnum = 0

while 1:
    char = f.read(1)
    if not char:
        break
    if len(one) == 4:
        break
    if char in one:
        one.popitem(last=False)

    one.update({char:''})
    totalnum += 1
    print(one)
    print(totalnum)

oneList = list(one.keys())

f.close()