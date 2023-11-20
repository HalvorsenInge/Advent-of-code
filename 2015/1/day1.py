import os
from icecream import ic

def list_files_in_current_directory():
    current_directory = os.getcwd()
    files = os.listdir(current_directory)
    return files


def parseInput(input:str):
    floor = 0
    increment = 0
    for characther in input:
        if floor == -1:
            break
        increment += 1
        if characther == '(':
            ic("incremnent floor")
            floor += 1
        elif characther == ')':
            ic("decrement floor")
            floor -= 1
        else:
            print("Invalid char")
    return floor, increment


def main():
    filePath = "input"
    ic(os.path.exists(filePath))
    try:
        with open(filePath) as f:
            ic(parseInput(f.read()))
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")


if __name__ == "__main__":
    files_in_current_directory = list_files_in_current_directory()
    print("Files in the current directory:")
    for file in files_in_current_directory:
        print(file)
    main()   