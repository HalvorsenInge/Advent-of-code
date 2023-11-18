from icecream import ic

def parseInput(input:str):
    floor = 0
    for characther in input:
        if characther == '(':
            ic("incremnent floor")
            floor += 1
        elif characther == ')':
            ic("decrement floor")
            floor -= 1
        else:
            print("Invalid char")
    return floor

def main():
    f = open("1.1/input")
    ic(parseInput(f.read()))

if __name__ == "__main__":
    main()   