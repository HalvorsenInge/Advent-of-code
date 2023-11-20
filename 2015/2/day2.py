from icecream import ic

def parseInput(input:str):
    paper_array = [formula.split('x') for formula in input.splitlines()]
    paper = 0
    ribbon = 0
    for formula in paper_array:
        paper += calculatePaper(formula)
        ribbon += calculateRibbon(formula)
    ic(paper)
    ic(ribbon)
    
def calculatePaper(arr):
    return_array = sorted([2*int(arr[0])*int(arr[1]),
                    2*int(arr[1])*int(arr[2]),
                    2*int(arr[2])*int(arr[0])])
    return return_array[0]/2+return_array[0]+return_array[1]+return_array[2]

def calculateRibbon(arr):
    return_array = sorted(list(map(int, arr)))
    return return_array[0]*2+return_array[1]*2+return_array[0]*return_array[1]*return_array[2]

def main():
    f = open("input")
    parseInput(f.read())

if __name__ == "__main__":
    main()