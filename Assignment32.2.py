from datetime import datetime
from os import path
from sys import argv
import schedule
from time import sleep

def monitorSize(filePath):
    border = "-"*50
    with open("FileSizeLog.txt","a") as fObj:
        try:

            if not path.exists(filePath):
                print("Invalid Path, Scan Not Possible")
                fObj.write(border+"\n")
                fObj.write(f"File Path: {filePath} Does Not Exist, Hence Scan Not Possible \n")
                fObj.write(f"Date And Time: {datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')} \n")
                fObj.write(border+"\n")
                return
            
            else:
                fObj.write(border+"\n")
                fObj.write(f"File Path: {filePath} \n")
                fObj.write(f"File Size: {path.getsize(filePath)} bytes \n")
                fObj.write(f"Date And Time: {datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')} \n")
                fObj.write(border+"\n")
                print(f"File with path {filePath} is scanned and scan details are stored in FileSizeLog.txt")
                return
            
        except Exception as eObj:
            print("Exception Occurred!, file scan not possible.")
            print("Details of the exception stored in FileSizeLog.txt")
            fObj.write(border+"\n")
            fObj.write(f"Exception Occurred, Details: {eObj} \n")
            fObj.write(f"File Path: {filePath} \n")
            fObj.write(f"Date And Time: {datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')} \n")
            fObj.write(border+"\n")
            return



def main():
    if(len(argv)==2):

        if(argv[1]=="--h" or argv[1]=="--H"):
            print("This is a automation script which monitors size of a specified file every 30 seconds")
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
                schedule.every(30).seconds.do(monitorSize,argv[1])
                while(True):
                    schedule.run_pending()
                    sleep(10)

    elif(len(argv)!=2):
        print("Invalid Number of arguments")
        print("Use --h flag for help and --u flag for usage")
        return

if __name__ == "__main__":
    main()

