from os import walk,path
from time import sleep
from datetime import datetime
import schedule 
from sys import argv

def directoryScan(dirName):
    subDirectories = 0
    files = 0
    for folder,subFolder,fileName in walk(dirName):
        subDirectories += len(subFolder)
        files += len(fileName)

    print(f"Directory Scanned: {dirName}")
    print(f"Total Files: {files}")
    print(f"Total SubDirectories: {subDirectories}")
    print(f"Scan Time: {datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}")
    return

def main():
    if(len(argv)==2):
        if(argv[1]=="--h" or argv[1]=="--H"):
            print("This is a automation script which does a directory scan every minute")
            print("Check --u flag")
            return

        elif(argv[1]=="--u" or argv[1]=="--U"):
            print("This automation scripts scans a directory on providing it's path")
            print("You need to provide the input in following format - <program.py> <DirectoryPath> through command line")
            print("This task is repeated every 1 minute and the scan details are provided on console")
            return
        else:
            if not path.exists(argv[1]):
                print("Error, directory provided does not exist...")
                return
            
            elif not path.isdir(argv[1]):
                print("The name provided is not a directory, provide correct path")
                return
                    
            else:
                schedule.every(1).minute.do(directoryScan,argv[1])
                while(True):
                    schedule.run_pending()
                    sleep(10)


    elif(len(argv)!=2):
        print("Invalid Number of Arguments")
        print("Use --h for help and --u for usage")
        return        

if __name__ == "__main__":
    main()