f = open("challange_text",'r')
lines = f.readlines()

elves = []

temp = 0
elf = []
for line in lines:
    if line.strip() == "":
        elves.append(elf)
        elf = []
    else:
        elf.append(int(line))

def largest(elves):
    elf = 0
    temp = 0
    for elve in elves:
        if sum(elve) > temp:
            elf = elve
            temp = sum(elve)

    return elf

def top3(elves):
    sumelves = []
    top3 = []
    for elf in elves:
        sumelves.append(sum(elf))

    sumelves = sorted(sumelves, reverse=True)

    top3.append(sumelves.pop(0))
    top3.append(sumelves.pop(0))
    top3.append(sumelves.pop(0))
    return(top3)


print(sum(largest(elves)))
print(sum(top3(elves)))
