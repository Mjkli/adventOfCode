import re
#f = open(r'puzzle_input.txt','r')
f = open(r'test.txt','r')
lines = f.readlines()

class Node:
    name = ''
    parent = ''
    type = ''
    children = []

    def __init__(self,name,type,size):
        self.name = name
        self.type = type
        self.size = size

    def addParent(self,parent):
        self.parent = parent
    
    def addChild(self,child):
        self.children.append(child)

    def getName(self):
        print(self.name)
    
    def getType(self):
        print(self.type)
    
    def getSize(self):
        print(self.size)
    
    def getChildren(self):
        print(self.children)



def tree(line):
    total = 0
    for char in line:
        
        if char == '-':
            break
        if char == ' ':
            total += 1
    
    return (total/2)


def getinfo(line):
    name = ''
    info = ''
    temp = False
    temp2 = False
    for char in line:
        if char == '-':
            temp2 = True
        elif char == '(':
            temp2 = False
            temp = True
        elif char == ')':
            temp = False
        elif temp:
            info += char
        elif temp2:
            name += char
        else:
            continue
    
    name = name.replace(" ", "")
    info = info.replace(" ", "")
    return(name,info)
    
def buildNode(name,info,level):
    if len(info) > 3:
        size = re.findall(r'\d+', info)
        temp = Node(name,"file",size[0])
        fileNodes.append(temp)
    else:
        temp = Node(name,"dir",0)
        dirNodes.append(temp)


dirNodes = []
fileNodes = []


for line in lines:
    name,info = getinfo(line)
    level = tree(line)
    buildNode(name,info,level)


for node in fileNodes:
    if node.name == "None":
        fileNodes.remove(node)
for node in dirNodes:
    if node.name == "None":
        fileNodes.remove(node)

    
