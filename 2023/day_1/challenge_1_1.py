file = open("puzzle_input.txt", 'r')
lines = file.readlines()

sum = 0

for line in lines:
    num = ""
    temp = []
    for char in line:
        if char.isdigit():
            temp.append(char)

    if temp.__len__() == 1:
        temp.append(temp[0])
    
    num = temp[0] + temp[-1]
    
    sum += int(num)

print(sum)
        