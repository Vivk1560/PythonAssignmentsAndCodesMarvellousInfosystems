from os import walk, path, remove
import schedule 
from datetime import datetime
from sys import argv
from time import sleep

def deleteEmptyFiles(srcDict):
    tObj = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    logObj = f"Marvellous {tObj}.log"
    logObj = logObj.replace(" ","_")
    logObj = logObj.replace(":","_")
    border = "-"*55
    
    try:
        with open(logObj,"w") as lObj:

            removedFiles = 0
            failed = 0
            totalFiles = 0
            emptyFiles = 0

            if not path.exists(srcDict):
                print(f"Source Directory {srcDict} does not exist at provided path")
                lObj.write(border+"\n")
                lObj.write(f"Source Directory {srcDict} does not exist at provided path \n")
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

            else:
                lObj.write(border+"\n")
                lObj.write(f"Directory Path: {srcDict} \n")

                try:
                    lObj.write(border+"\n")
                    for folder,subfolders, file in walk(srcDict):
                        totalFiles += len(file)
                        for fName in file:
                            src = path.join(folder,fName)
                            if (path.getsize(src)==0):
                                emptyFiles += 1
                                try:
                                    remove(src)
                                    removedFiles += 1
                                    lObj.write(f"File name {src} deleted from {srcDict} at date and time {tObj} \n")

                                except Exception as e1Obj:
                                    failed += 1
                                    lObj.write(f"The File {src} of {srcDict} cannot be removed from directory {srcDict} because of a exception \n")
                                    lObj.write(f"Date And Time {tObj} \n")
                                    lObj.write(f"Exception Details: {e1Obj} \n")
                                
                    lObj.write(border+"\n")
                    lObj.write(f"Total Files Found: {totalFiles} \n")
                    lObj.write(f"Empty Files: {emptyFiles} \n")
                    lObj.write(f"Successfully Removed: {removedFiles} \n")
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
                    print(f"Log File Is Created With Name: {logObj} at time {tObj} containing all the details of the delete operation, check log file for the same")

                return
            
    except OSError as oObj:
        print("Log File Was Not Able To Be Created Because Of A Error")
        print("Error Is: ",oObj)
        return


def main():
    if(len(argv)==2):
        if (argv[1] == "--h" or argv[1] == "--H"):
            print("This is an automation script that scans a directory recursively every hour.")
            print("It detects all empty files (files with size 0 bytes) and deletes them automatically.")
            print("Details of all deleted files, errors, and summary statistics are stored in a log file.")
            print("Use the --u flag to see the correct usage of this script.")
            return

        elif (argv[1] == "--u" or argv[1] == "--U"):
            print("Provide the source directory path through the command line.")
            print("Usage:")
            print("python Program.py <SourceDirectory>")
            print("Example:")
            print("python Program.py C:\\Users\\Vivaan\\Documents\\SampleFolder")
            return

        else:
                
            if not (path.isdir(argv[1])):
                print(f"The source path provided is not a directory")
                return
        
            else:
                schedule.every(1).hour.do(deleteEmptyFiles,argv[1])
                while(True):
                    schedule.run_pending()
                    sleep(60)

    elif (len(argv)!=2):
        print("Invalid Number Of Arguments, check --h flag for help and --u flag for usage")
        return

if __name__ == "__main__":
    main()

                            
                        
        