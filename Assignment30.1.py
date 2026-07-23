import schedule
from time import sleep

def display():
    print("Jai Ganesh.....!")
    return

def main():
    schedule.every(2).seconds.do(display)

    while(True):
        schedule.run_pending()
        sleep(1)

if __name__ == "__main__":
    main()
        