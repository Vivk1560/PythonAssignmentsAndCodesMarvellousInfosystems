from sys import argv
from os import path

def checkFrequency(fileName,freqString):
    fCount = 0
    with open(fileName,"r") as fObj:
        for line in fObj:
            for word in line.split():
                if(freqString==word):
                    fCount += 1
    return fCount                

def main():
    if len(argv) == 2:

        if argv[1] == "--h" or argv[1] == "--H":
            print("This is a file handling program which counts the frequency of a string in a file.")
            print("Use --u flag to check usage")
            return

        elif argv[1] == "--u" or argv[1] == "--U":
            print("Usage : <program.py> <FileName> <String>")
            return

    if len(argv) != 3:
        print("Invalid Number Of Arguments...!")
        print("Use --h flag for help or --u flag to check usage")
        return

    if path.exists(argv[1]):
        print(f"The count of the string '{argv[2]}' in file {argv[1]} is {checkFrequency(argv[1], argv[2])}")
    else:
        print(f"The file '{argv[1]}' does not exist in the current directory. Provide an absolute path.")


if __name__ == "__main__":
    main()
