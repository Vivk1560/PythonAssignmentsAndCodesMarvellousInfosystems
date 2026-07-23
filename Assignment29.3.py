from os import path
from sys import argv

def copyContents(fileName):
    with open(fileName,"r") as srcObj:
        with open("Demo.txt","w") as destObj:
            destObj.write(srcObj.read())

def main():
    if(len(argv)!=2):
        print("Invalid Number Of Arguments...!")
        print("Use --h flag for help or --u flag to check usage")
        return

    else:
        if(argv[1]=="--h" or argv[1]=="--H"):
            print("This is a file handling program which copies contents of your file to a new file named Demo.txt")
            print("Use --u flag to check usage")
            return

        elif(argv[1]=="--u" or argv[1]=="--U"):
            print("Provide file name through command line arguments as <program.py> <fileName>")
            return

        else:
            if path.exists(argv[1]):
                copyContents(argv[1])
                print(f"Contents of '{argv[1]}' copied successfully to 'Demo.txt'.")
                return 

            else:
                print(f"The name of the file provided {argv[1]} does not exist in current directory provide absolute path for the same")
                return

if __name__ == "__main__":
    main()

