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
    try:
        with open("input") as f:
            ic(parseInput(f.read()))
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")
if __name__ == "__main__":
    main()   