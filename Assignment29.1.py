from os import path

def checkFileInDirectory(fileName):
    return path.exists(fileName)

def main():
    fName = input("Enter file name : ")

    if checkFileInDirectory(fName):
        print(f"{fName} exists in the current directory.")
    else:
        print(f"{fName} does not exist in the current directory.")

if __name__ == "__main__":
    main()


