import math
def calcAreaofCircle(r1):
    p = math.pi
    area = p*r1*r1
    return area

def main():
    radius = int(input("Enter the radius of circle you want area of: "))
    print(f"Area of the circle is {calcAreaofCircle(radius)}")
    return

if __name__ == "__main__":
    main()
