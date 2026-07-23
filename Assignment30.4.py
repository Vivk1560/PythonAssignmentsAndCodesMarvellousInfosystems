from datetime import datetime
import schedule 
from time import sleep

def display():
    print("Namaskar")
    return

def main():
    schedule.every().day.at("9:00").do(display)

    while(True):
        schedule.run_pending()
        sleep(10)

if __name__ == "__main__":
    main()
