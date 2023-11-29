import re
f = open(r'C:\Users\Anthony\Desktop\adventofcode2022\day_5\puzzle_input.txt','r')
#f = open(r'C:\Users\Anthony\Desktop\adventofcode2022\day_5\test.txt','r')
lines = f.readlines()

stacks = []


def stackbuild(line):
    chars = []
    for i, char in enumerate(line):
        if i % 4 == 0:
            if char == '\n':
                continue
            chars.append(line[i + 1])

    for i, char in enumerate(chars):
        if len(stacks) <= i:
            stack = [char]
            stacks.append(stack)
        else:
            if char == ' ':
                continue
            else:
                stacks[i].append(char)

def cleanstacks():
    for stack in stacks:
        if stack[0] == ' ':
            stack.remove(' ')


def sort(nums):
    print(nums)




for i,line in enumerate(lines):
    if line[0] == '[':
        stackbuild(line)
    if line[0] == ' ':
        cleanstacks()
    else:
        strnums = re.findall(r'\d+',line)
        nums = list(map(int, strnums))
        sort(nums)