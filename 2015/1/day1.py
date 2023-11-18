def parseInput(input:str):
    floor = 0
    for characther in input:
        if characther == '(':
            ++floor
        elif characther == ')':
            --floor
        else:
            print("Invalid char")
    return floor

if "__name__" == "__main__":
    #day1()
    pass