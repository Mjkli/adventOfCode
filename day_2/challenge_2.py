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
                case "X": # +1
                    # loss
                    return(loss + sissors)
                case "Y": # +2
                    # draw
                    return(draw + rock)
                case "Z": # +3
                    # win
                    return(win + paper)

        case "B":
            match us:
                case "X": # +1
                    # loss
                    return(loss + rock)
                case "Y": # +2
                    # draw
                    return(draw + paper)
                case "Z": # +3
                    # win
                    return(win + sissors)
        case "C":
            match us:
                case "X": # +1
                    # loss
                    return(loss + paper)
                case "Y": # +2
                    # draw
                    return(draw + sissors)
                case "Z": # +3
                    # win
                    return(win + rock)




total = 0

for line in lines:
    #total += tictoe(line[0],line[2])
    total += part_2(line[0],line[2])


print(total)