import re
from word2number import w2n
file = open("puzzle_input.txt", 'r')
lines = file.readlines()

SUM = 0


def filterNums(line: str) -> int:  
    help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
    }
    nums = []
    current_word = ""

    for char in line:
        if char.isdigit():
            nums.append(char)
            pass
        current_word += char
        for key in help_dict:
            if current_word.__contains__(key):
                nums.append(help_dict.get(key))
                current_word = char
    
    num = nums[0] + nums[-1]

    return int(num)


for line in lines:
    SUM += filterNums(line)

print(SUM)