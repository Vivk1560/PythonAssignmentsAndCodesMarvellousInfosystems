from datetime import datetime
from os import path
import schedule 
from shutil import copy2
from sys import argv
from time import sleep

def copyContent(srcFile,destFolder):
    logFile = "backup_log.txt" 
    with open(logFile,"a") as fObj:
        sO = path.basename(srcFile)
        so1,so2 = path.splitext(sO)
        tObj = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        destFileName = so1+"_"+tObj+so2
        destFileName = destFileName.replace(" ","_")
        destFileName = destFileName.replace(":","_")
        destFolder = path.join(destFolder,destFileName)
        try:
            copy2(srcFile,destFolder)
            fObj.write(f"File with name {srcFile} is successfully copied to {destFileName} at time {tObj} \n")
            print(f"Copy Success!, log file created with name as {destFileName}, at location {destFolder}, at time {datetime.now()}")
        except Exception as eobj:
            fObj.write(f"Exception Occurred!, copying of data not possible: {eobj} at time {tObj} \n")
            print(f"Exception Occurred!, record stored in log file with name as {destFileName}, at location {destFolder}, at time{datetime.now()}")
    return

def main():
    if(len(argv)==2):
        if(argv[1]=="--h" or argv[1]=="--H"):
            print("This is a automation script which does a file backup every hour to the desired directory upon providing src file path and destination directory path")
            print("Check --u flag")
            return

        elif(argv[1]=="--u" or argv[1]=="--U"):
            print("This automation scripts copies a file on providing it's path to a directory")
            print("You need to provide the input in following format - <program.py> <srcFilePath> <DestinationDirectoryPath> through command line")
            print("This task is repeated every 1 hour and the copied file is stored into directory with source file's baseName_timeStamp")
            return

    elif(len(argv)!=3):
        print("Invalid Number of Arguments")
        print("Use --h for help and --u for usage")
        return

    else:
        if not path.exists(argv[1]):
            print("Error, source file provided does not exist at the provided path or you may have provided incorrect path")
            return

        elif not path.isdir(argv[2]):
            print("The destination provided is not a directory, provide correct path")
            return
        
        else:
            schedule.every(1).minute.do(copyContent,argv[1],argv[2])
            while(True):
                schedule.run_pending()
                sleep(10)

if __name__ == "__main__":
    main()



    



    
