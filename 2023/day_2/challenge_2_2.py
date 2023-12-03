import re

file = open("puzzle_input.txt", 'r')
lines = file.readlines()


SUM = int('0')


def get_power(given: list[str]) -> int:

    largest = {
        'red' : 0,
        'blue' : 0,
        'green': 0
    }

    power = 1
    
    
    given = re.split(r';|,', given)

    for color in given:
        num = re.findall(r'\d+', color)
        num = int(num[0])
        word = re.sub(r'[0-9]','',color).strip()
        
        if num > largest.get(word):
            largest[word] = num


    for key in largest:
        power *= largest.get(key)

    return power



for game in lines:
    x = game.split(":")
    SUM += get_power(x[1])

print(SUM)
