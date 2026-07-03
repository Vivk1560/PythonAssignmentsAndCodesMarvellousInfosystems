def sumOfNaturalNumbers(n1):
    sum = 0
    for i in range(1,n1+1):
        sum += i
    return sum

def main():
    no1 = int(input("Enter the number till which you want the sum: "))
    print("The Sum Of Numbers Till The Number Entered Is:",sumOfNaturalNumbers(no1))
    return

if __name__ == "__main__":
    main()
