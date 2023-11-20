from icecream import ic

def parseInput(input):
    visited = set()
    santa = (0,0)
    roboSanta = (0,0)
    visited.add(santa)
    b = True
    for char in input:
        if b == True:
            santa = move(char, santa)
            visited.add(santa)
            b = False
        else:
            roboSanta = move(char, roboSanta)
            visited.add(roboSanta)
            b = True
    ic(visited, len(visited))

def move(char, santa):
    x, y = santa
    if char == '^':
        santa = (x, y+1)
    elif char == 'v':
        santa = (x, y-1)
    elif char == '<':
        santa = (x-1, y)
    elif char == '>':
        santa = (x+1, y)        
    return santa


def main():
    f = open("input")
    parseInput(f.read())

if __name__ == "__main__":
    main()
    # parseInput('^>V<')