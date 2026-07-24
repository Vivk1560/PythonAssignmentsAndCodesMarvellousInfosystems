from os import path
from sys import argv
from time import sleep
import schedule 


def readDisplay(filePath):

    if not path.exists(filePath):
        print("File Does Not Exist At Specified Path!")
        print("Please Provide Correct Path")
        return

    elif (path.getsize(filePath)==0):
        print("File provided is empty!")
        print("No Contents to display")
        return

    else:

        try:
            with open(filePath,"r") as fObj:
                print("File Contents Are As Follows:")
                print(fObj.read())
                return
            
        except PermissionError as pObj:
            print("Permission Denied!")
            print("Permission Error:",pObj)
            return
        
        except Exception as eObj:
            print("Exception Occurred!")
            print("Exception:",eObj)
            return

def main():
    if(len(argv)==2):

        if(argv[1]=="--h" or argv[1]=="--H"):
            print("This is a automation script which displays content of a specified file every 1 minute")
            print("Use --u flag for usage")
            return
        
        elif(argv[1]=="--u" or argv[1]=="--U"):
            print("This automation script accepts filename using commandline")
            print("Enter input as <Program.py> <filePath>")
            return
        
        else:

            if not path.exists(argv[1]):
                print("Specified File Path Does Not Exist, enter correct file path")
                return
            
            else:
                schedule.every(1).minute.do(readDisplay,argv[1])
                while(True):
                    schedule.run_pending()
                    sleep(10)

    elif(len(argv)!=2):
        print("Invalid Number of arguments")
        print("Use --h flag for help and --u flag for usage")
        return

if __name__ == "__main__":
    main()

