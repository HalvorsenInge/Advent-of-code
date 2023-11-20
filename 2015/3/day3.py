from icecream import ic

def parseInput(input):
    visited = set()
    (x, y) = (0,0)
    visited.add((x,y))
    for char in input:
        if char == '^':
            (x, y) = (x, y+1)
        elif char == 'v':
            (x, y) = (x, y-1)
        elif char == '<':
            (x, y) = (x-1, y)
        elif char == '>':
            (x, y) = (x+1, y)        
        visited.add((x, y))
    ic(visited, len(visited))


def main():
    f = open("input")
    parseInput(f.read())

if __name__ == "__main__":
    main()
    # parseInput('^>V<')