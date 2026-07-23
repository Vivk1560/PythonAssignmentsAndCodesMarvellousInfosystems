from os import walk,path
from time import sleep
from datetime import datetime
import schedule 
from sys import argv

def directoryScan(dirName):
    tObj = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    logName = "DirectoryCountLog.txt"
    files = 0
    border = "-"*50
    with open(logName,"a") as fObj:
        for folder,subFolder,fileName in walk(dirName):
            files += len(fileName)
        fObj.write(border+"\n")
        fObj.write(f"Directory Path: {dirName} \n")
        fObj.write(f"Total Files: {files} \n")
        fObj.write(f"Date And Time: {tObj} \n")
        fObj.write(border+"\n")
        print(f"Log Created with name: {logName}")
    return

def main():
    if(len(argv)==2):
        if(argv[1]=="--h" or argv[1]=="--H"):
            print("This is a automation script which does a directory scan every 5 minutes and writes result into a log file")
            print("Check --u flag")
            return

        elif(argv[1]=="--u" or argv[1]=="--U"):
            print("This automation scripts scans a directory on providing it's path and writes result of scan in a log file")
            print("You need to provide the input in following format - <program.py> <DirectoryPath> through command line")
            print("This task is repeated every 5 minutes and the scan details are provided in log")
            return
        else:
            if not path.exists(argv[1]):
                print("Error, directory provided does not exist...")
                return
            
            elif not path.isdir(argv[1]):
                print("The name provided is not a directory, provide correct path")
                return
                    
            else:
                schedule.every(5).minutes.do(directoryScan,argv[1])
                while(True):
                    schedule.run_pending()
                    sleep(60)


    elif(len(argv)!=2):
        print("Invalid Number of Arguments")
        print("Use --h for help and --u for usage")
        return        

if __name__ == "__main__":
    main()