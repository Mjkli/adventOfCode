f = open("puzzle_input.txt",'r')
#f = open("test_input.txt",'r')
lines = f.readlines()

rock = 1
paper = 2
sissors = 3

loss = 0
draw = 3
win = 6


def tictoe(opp,us):
    match opp:
        case "A":
            match us:
                case "X": # +1
                    # draw
                    return(draw + rock)
                case "Y": # +2
                    # win
                    return(win + paper)
                case "Z": # +3
                    # loss
                    return(loss + sissors)

        case "B":
            match us:
                case "X":
                    # loss
                    return(loss + rock)
                case "Y":
                    # draw
                    return(draw + paper)
                case "Z":
                    # win
                    return(win + sissors)
        case "C":
            match us:
                case "X":
                    # win
                    return(win + rock)
                case "Y":
                    # loss
                    return(loss + paper)
                case "Z":
                    # draw
                    return(draw + sissors)

def part_2(opp,us):
    match opp:
        case "A":
            match us:
                case "X":
                    # loss
                    return(loss + sissors)
                case "Y":
                    # draw
                    return(draw + rock)
                case "Z":
                    # win
                    return(win + paper)

        case "B":
            match us:
                case "X":
                    # loss
                    return(loss + rock)
                case "Y":
                    # draw
                    return(draw + paper)
                case "Z":
                    # win
                    return(win + sissors)
        case "C":
            match us:
                case "X":
                    # loss
                    return(loss + paper)
                case "Y":
                    # draw
                    return(draw + sissors)
                case "Z":
                    # win
                    return(win + rock)


total_1 = 0
total_2 = 0

for line in lines:
    total_1 += tictoe(line[0],line[2])
    total_2 += part_2(line[0],line[2])


print(total_1)
print(total_2)