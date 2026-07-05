def checkLen(txt):
    return len(txt)

def main():
    value = input("Enter the word you want length of: ")
    print(f"The length of the entered word {value} is {checkLen(value)}")
    return

if __name__ == "__main__":
    main()
        
