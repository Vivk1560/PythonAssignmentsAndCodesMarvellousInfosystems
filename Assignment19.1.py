squaring = lambda no : no*no

def main():
    value = int(input("Enter the number you want power of 2 of: "))
    print(f"Power of 2 of the given number {value} is {squaring(value)}")
    return

if __name__ == "__main__":
    main()