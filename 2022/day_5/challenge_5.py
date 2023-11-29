import re
f = open(r'puzzle_input.txt','r')
#f = open(r'test.txt','r')
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
    for i in range(0,nums[0]):
        stacks[nums[2] - 1].insert(0,stacks[nums[1] - 1].pop(0))
    print(stacks)

def sort2(nums):
    temp = []
    for i in range(0,nums[0]):
        temp += stacks[nums[1] - 1].pop(0)
    stacks[nums[2] - 1] = temp + stacks[nums[2] - 1]
    print(stacks)
    


moves = []

for i,line in enumerate(lines):
    if '[' in line:
        stackbuild(line)
    elif line[0] == 'm':
        cleanstacks()
        strnums = re.findall(r'\d+',line)
        nums = list(map(int, strnums))
        moves.append(nums)
    else:
        continue


print (stacks)
for move in moves:
    #sort(move)
    sort2(move)



answer1 = ""
for stack in stacks:
    answer1 += stack[0]

print(answer1)