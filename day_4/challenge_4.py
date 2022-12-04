import re

f = open("puzzle_input.txt",'r')
#f = open("./test_input.txt",'r')
lines = f.readlines()



def enclose(num1,num2,num3,num4):
    if (num3 >= num1 and num4 <= num2) or (num3 <= num1 and num4 >= num2):
            return 1
    return 0

def overlap(num1,num2,num3,num4):
    print(str(num1)+","+str(num2)+","+str(num3)+","+str(num4))
    if(num3 <= num2 and num4 >= num1) or (num3 <= num1 and num4 >= num1):
        print("overlap!")
        return 1
    return 0


total_1 = 0
total_2 = 0

for line in lines:
    nums = re.findall(r'\d+',line)
    total_1 += enclose(int(nums[0]),int(nums[1]),int(nums[2]),int(nums[3]))
    total_2 += overlap(int(nums[0]),int(nums[1]),int(nums[2]),int(nums[3]))

print(total_1)
print(total_2)
