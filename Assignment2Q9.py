def takingInputAndDisplay():
    print("Can you please enter your name:")
    nam = input()
    print("Now please enter your age:")
    age = int(input())
    print(f"Hello {nam}, you will turn {age + 1} next year.")

def main():
    takingInputAndDisplay()

if(__name__=="__main__"):
    main()