class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
    
    def accept(self):
        self.Radius = int(input("Enter the radius of circle: "))
    
    def calculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def calculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def display(self):
        print(f"Radius          : {self.Radius}")
        print(f"Area            : {self.Area}")
        print(f"Circumference   : {self.Circumference}")

cir1 = Circle()
cir1.accept()
cir1.calculateArea()
cir1.calculateCircumference()
cir1.display()

cir2 = Circle()
cir2.accept()
cir2.calculateArea()
cir2.calculateCircumference()
cir2.display()


cir3 = Circle()
cir3.accept()
cir3.calculateArea()
cir3.calculateCircumference()
cir3.display()


cir4 = Circle()
cir4.accept()
cir4.calculateArea()
cir4.calculateCircumference()
cir4.display()

