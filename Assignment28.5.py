from os import path

def checkWordInAFile(fileName,chkWord):
    with open(fileName,"r") as fObj:
        for line in fObj:
            for word in line.split():
                if(chkWord.lower()==word.lower()):
                    return True
    return False

def main():
    fName = input("Enter The File Name: ")
    wordName = input("Enter the word you want to check for in the file: ")
    if(path.exists(fName)):
        print(f"File Name: {fName}")
        print(f"Word To Be Found: {wordName}")     
        if(checkWordInAFile(fName,wordName)):
            print(f"The word {wordName} exists in the file {fName}")
        else:
            print(f"The word {wordName} does not exist in the file {fName}") 
    else:
        print("The file name entered is either invalid or the file does not exist....")
    return

if __name__ == "__main__":
   main()
    