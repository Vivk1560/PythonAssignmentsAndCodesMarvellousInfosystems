def factAdd(no):
    sum = 0
    for i in range(1,no):
        if(no%i==0):
            sum+=i
    return sum

def main():
    v = int(input("Enter the number for you want to check sum of its factors: "))
    print(f"The sum of the factors of the given number {v} is {factAdd(v)}")
    return

if __name__ == "__main__":
    main()
    