from os import path

def displayContents(fileName):
    with open(fileName,"r") as fObj:
        print(fObj.read())

def main():
    fName = input("Enter file name : ")

    if path.exists(fName):
        displayContents(fName)
    else:
        print("File does not exist.")

if __name__ == "__main__":
    main()