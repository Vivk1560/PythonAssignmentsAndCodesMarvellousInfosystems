def calcArea(n1,n2):
    area = n1*n2
    return area

def main():
    n1 = int(input("Enter the width of the rectangle: "))
    n2 = int(input("Enter the length of the rectangle: "))
    print(f"Area of rectangle is {calcArea(n1,n2)} square units")
    return

if __name__ == "__main__":
    main()