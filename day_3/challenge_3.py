f = open("puzzle_input.txt",'r')
#f = open("test_input.txt",'r')
lines = f.readlines()

# return priority number
def priority(ch):
    if ch.islower():
        return ord(ch) - 96
    else:
        return ord(ch) - 38


def compare(a, b):
    A = set(a)
    B = set(b)
    result = sorted(A.intersection(B))
    return priority(result[0])

def compare3(a,b,c):
    A = set(a)
    B = set(b)
    C = set(c)
    temp = sorted(A.intersection(B))
    result = sorted(set(temp).intersection(C))
    return priority(result[0])



total_1 = 0
total_2 = 0

group = []

for num, line in enumerate(lines):
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    total_1 += compare(firstpart, secondpart)
    if num % 3 == 0:
        #print(num)
        if group:
            total_2 += compare3(group[0],group[1],group[2])
        group = []

    group.append(line.strip())

total_2 += compare3(group[0],group[1],group[2])

print(total_1)
print(total_2)
