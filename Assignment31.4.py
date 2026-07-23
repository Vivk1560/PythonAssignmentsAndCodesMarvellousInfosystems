from datetime import datetime
from time import sleep
import schedule 

def createLog():
    tObj = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    fName = f"Marvellous_Log_{tObj}.txt"
    fName = fName.replace(" ","_")
    fName = fName.replace(":","_")
    with open(fName,"w") as fObj:
        fObj.write("Log File Created Successfully \n")
        fObj.write(f"Creation Time: {datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')} \n")
        print(f"Log File Created with name {fName}")
        return

def main():
    schedule.every(10).minutes.do(createLog)
    while(True):
        schedule.run_pending()
        sleep(60)     

if __name__ == "__main__":
    main()