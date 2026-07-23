from os import path
from datetime import datetime
import schedule 
from time import sleep

def display():
    
    with open("Marvellous.txt","a") as fObj:
        fObj.write(f"Task Executed at: {datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}\n")
        print("Task Executed and done in Marvellous.txt")
    return

def main():
    schedule.every(5).minutes.do(display)

    while(True):
        schedule.run_pending()
        sleep(60)

if __name__ == "__main__":
    main()

