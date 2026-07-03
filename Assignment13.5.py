def displayClass(marks):

    if marks >=75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 50:
        return "Second Class"
    else :
        return "Fail"

def main():
    m = int(input("Enter the marks: "))
    print(f"The marks of the respective student are {m} and the result is: {displayClass(m)}")
    return

if __name__ == "__main__":
    main()