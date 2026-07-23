from os import path

def countLines(fileName):
    count = 0
    with open(fileName,"r") as fObj:
        for line in fObj:
            count += 1
    return count

def main():
    fName = input("Enter File Name: ")
    if(path.exists(fName)):
        print(f"Total number of lines in {fName} : {countLines(fName)}")
    else:
        print("The file name entered is either invalid or the file does not exist....")
    return

if __name__ == "__main__":
    main()