import schedule  
from time import sleep
from datetime import datetime

def createFile():

    tObj = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    sFile = f"File {tObj}.txt"
    sFile = sFile.replace(" ","_")
    sFile = sFile.replace(":","_")
    border = "-"*50

    with open(sFile,"w") as fObj:
        fObj.write(border+"\n")
        fObj.write(f"File Name: {sFile} \n")
        fObj.write(f"Creation date: {datetime.now().strftime('%d-%m-%Y')} \n")
        fObj.write(f"Creation time: {datetime.now().strftime('%I:%M:%S %p')} \n")
        fObj.write(border+"\n")
        print("File Created Successfully with name:",sFile)
        return

def main():
    schedule.every().minute.do(createFile)

    while(True):
        schedule.run_pending()
        sleep(10)

if __name__ == "__main__":
    main()
