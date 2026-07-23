from sys import argv
from os import path

def compareContents(f1,f2):
    with open(f1,"r") as f1Obj:
        with open(f2,"r") as f2Obj:
            return (f1Obj.read()==f2Obj.read())

def main():
    if len(argv) == 2:

        if argv[1] == "--h" or argv[1] == "--H":
            print("This is a file handling program which compares the contents of two files.")
            print("Use --u flag to check usage")
            return

        elif argv[1] == "--u" or argv[1] == "--U":
            print("Usage : <program.py> <File1Name> <File2Name>")
            return

    if len(argv) != 3:
        print("Invalid Number Of Arguments...!")
        print("Use --h flag for help or --u flag to check usage")
        return

    if not path.exists(argv[1]):
        print(f"The file '{argv[1]}' does not exist in the current directory. Provide an absolute path.")
        return

    if not path.exists(argv[2]):
        print(f"The file '{argv[2]}' does not exist in the current directory. Provide an absolute path.")
        return

    if compareContents(argv[1], argv[2]):
        print("Success")
    else:
        print("Failure")


if __name__ == "__main__":
    main()

