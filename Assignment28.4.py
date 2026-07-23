from os import path

def copyContent(fileName,newName):
    with open(fileName,"r") as srcObj:
        with open(newName,"w") as destObj:
            destObj.write(srcObj.read())


def main():
    fName = input("Enter Existing File Name Whose Contents Are To Be Copied: ")
    nName = input("Enter the new file name in which the contents are to be copied: ")
    if(path.exists(fName)):
        print(f"File Name: {fName}")
        print(f"New File Name: {nName}")     
        copyContent(fName,nName)
    else:
        print("The file name entered is either invalid or the file does not exist....")
    return

if __name__ == "__main__":
   main()
