from os import walk, path, makedirs
import schedule 
from datetime import datetime
from shutil import copy2
from sys import argv
from time import sleep

def copyFilesToDirectory(srcDict,destDict):
    tObj = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    logObj = f"Marvellous {tObj}.log"
    logObj = logObj.replace(" ","_")
    logObj = logObj.replace(":","_")
    border = "-"*55
    
    try:
        with open(logObj,"w") as lObj:

            txtFiles = 0
            copied = 0
            failed = 0
            totalFiles = 0

            if not path.exists(srcDict):
                print(f"Source Directory {srcDict} does not exist at provided path")
                lObj.write(border+"\n")
                lObj.write(f"Source Directory {srcDict} does not exist at provided path \n")
                lObj.write(f"Date And Time: {tObj} \n")
                lObj.write(border+"\n")
                return

            elif not path.exists(destDict):
                print(f"Destination Directory {destDict} does not exist at provided path")
                lObj.write(border+"\n")
                lObj.write(f"Destination Directory {destDict} does not exist at provided path \n")
                lObj.write(f"Date And Time: {tObj} \n")
                lObj.write(border+"\n")
                return

            elif not path.isdir(srcDict):
                print(f"Source Path Provided {srcDict} is not a directory")
                lObj.write(border+"\n")
                lObj.write(f"Source Path Provided {srcDict} is not a directory \n")
                lObj.write(f"Date And Time: {tObj} \n")
                lObj.write(border+"\n")
                return

            elif not path.isdir(destDict):
                print(f"Destination Path Provided {destDict} is not a directory")
                lObj.write(border+"\n")
                lObj.write(f"Destination Path Provided {destDict} is not a directory \n")
                lObj.write(f"Date And Time: {tObj} \n")
                lObj.write(border+"\n")
                return

            else:
                lObj.write(f"Source Directory: {srcDict} \n")
                lObj.write(f"Destination Directory: {destDict} \n")
                try:
                    lObj.write(border+"\n")
                    for folder,subfolders, file in walk(srcDict):
                        totalFiles += len(file)
                        for fName in file:
                            if path.splitext(fName)[1].lower() == ".txt":
                                txtFiles += 1
                                src = path.join(folder,fName)
                                relative = path.relpath(folder,srcDict)
                                destFold = path.join(destDict,relative)
                                makedirs(destFold, exist_ok=True)
                                dest = path.join(destFold,fName)
                                try:
                                    copy2(src,dest)
                                    copied += 1
                                    lObj.write(f"File name {src} copied to {dest} at date and time {tObj} \n")

                                except Exception as e1Obj:
                                    failed += 1
                                    lObj.write(f"The File {src} of {srcDict} cannot be copied to directory {destDict} because of a exception \n")
                                    lObj.write(f"Date And Time {tObj} \n")
                                    lObj.write(f"Exception Details: {e1Obj} \n")
                                
                    lObj.write(border+"\n")
                    lObj.write(f"Total Files Found: {totalFiles} \n")
                    lObj.write(f"Total Text Files: {txtFiles}\n")
                    lObj.write(f"Successfully Copied: {copied} \n")
                    lObj.write(f"Failed: {failed} \n")
                    lObj.write(border+"\n")

                except PermissionError as pObj:
                    lObj.write("Permission Denied \n")
                    lObj.write(f"Date And Time: {tObj} \n")
                    lObj.write(f"Exception Details: {pObj} \n")

                except Exception as eObj:
                    lObj.write("Exception Occurred! \n")
                    lObj.write(f"Date And Time: {tObj} \n")
                    lObj.write(f"Exception Details: {eObj} \n")

                finally:
                    print(f"Log File Is Created With Name: {logObj} at time {tObj} containing all the details of the copy operation, check log file for the same")

                return
            
    except OSError as oObj:
        print("Log File Was Not Able To Be Created Because Of A Error")
        print("Error Is: ",oObj)
        return


def main():
    if(len(argv)==2):
        if (argv[1] == "--h" or argv[1] == "--H"):
            print("This is a automation script which copies all the files from a directory to a different directory every 10 minutes")
            print("Copying of files is done by taking both paths of source and destination directories")
            print("Details of the process are stored into a log file which is newly created every 10 minutes")
            print("Check --u flag for usage")
            return

        elif (argv[1] == "--u" or argv[1] == "--U"):
            print("Provide source and destination directory's paths through command line")
            print("It should be <Program.py> <SourceDirectory> <DestinationDirectory>")
            return

    elif (len(argv)!=3):
        print("Invalid Number Of Arguments, check --h flag for help and --u flag for usage")
        return

    else:
        if not (path.isdir(argv[1])):
            print(f"The source path provided is not a directory")
            return

        elif not (path.isdir(argv[2])):
            print(f"The destination path provided is not a directory")
            return

        else:
            schedule.every(10).minutes.do(copyFilesToDirectory,argv[1],argv[2])
            while(True):
                schedule.run_pending()
                sleep(60)

if __name__ == "__main__":
    main()

                            
                        
        