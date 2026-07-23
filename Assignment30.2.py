from datetime import datetime
import schedule 
from time import sleep

def display():
    print("Current Date And Time:",datetime.now())
    return

def main():
    schedule.every(1).minute.do(display)

    while(True):
        schedule.run_pending()
        sleep(20)

if __name__ == "__main__":
    main()
