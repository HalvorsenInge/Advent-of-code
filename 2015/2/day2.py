from icecream import ic

def parseInput(input:str):
    inputArray = [formula.split('x') for formula in input.splitlines()]
    
def calculatePaper(arr:list):
    return [2*int(arr[0])*int(arr[1]), 2*int(arr[1])*int(arr[2]), 2*int(arr[2])*int(arr[0])]

def main():
    f = open("input")
    ic(parseInput(f.read()))

if __name__ == "__main__":
    main()