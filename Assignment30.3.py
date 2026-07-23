from datetime import datetime
import schedule 
from time import sleep

def display():
    print("Coding Kar....")
    return

def main():
    schedule.every(30).minutes.do(display)

    while(True):
        schedule.run_pending()
        sleep(300)

if __name__ == "__main__":
    main()
