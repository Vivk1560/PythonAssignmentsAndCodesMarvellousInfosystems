from os import path

def displayLines(fileName):
    with open(fileName,"r") as fObj:
        for line in fObj:
            print(line, end = "")


def main():
    fName = input("Enter File Name: ")
    if(path.exists(fName)):
        print(f"File Name: {fName}")
        print("Lines of the file are now being displayed one by one: ")     
        displayLines(fName)
    else:
        print("The file name entered is either invalid or the file does not exist....")
    return

if __name__ == "__main__":
   main()
