import re

file = open("puzzle_input.txt", 'r')
lines = file.readlines()


def possible_game(game: str) -> bool:
    # given input
    shown = {
        'red'   : 12,
        'blue'  : 14,
        'green' : 13
    }

    given = re.split(r';|,', game)
    
    for color in given:
        num = re.findall(r'\d+', color)
        num = int(num[0])
        word = re.sub(r'[0-9]','',color).strip()


        #print(str(num) + " " + word)

        if num > shown.get(word):
            return False
    
    return True

count = 0

for game in lines:
    x = game.split(":")
    if possible_game(x[1]):
        gameNum = re.findall(r'\d+', x[0])
        count += int(gameNum[0])

print(count)