def chkNum(no):

    if(no%2==0):
        print(f"Number Entered - {no} is a Even Number")
    else:
        print(f"Number Entered - {no} is a Odd Number")
    return

def main():
    chkNum(2)
    chkNum(3)
    return

if __name__ == "__main__":
    main()