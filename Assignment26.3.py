class Arithmetic:

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def accept(self):
        self.value1 = int(input("Enter the value of first number: "))
        self.value2 = int(input("Enter the value of second number: "))
    
    def addition(self):
        ans = self.value1+self.value2
        return ans

    def subtraction(self):
        ans = self.value1-self.value2
        return ans
    
    def multiplication(self):
        ans = self.value1*self.value2
        return ans
    
    def division(self):
        try:
            return self.value1 / self.value2
        except ZeroDivisionError:
            print("Division by zero is not possible.")
            return None

obj1 = Arithmetic()

obj1.accept()

print("Addition:", obj1.addition())
print("Subtraction:", obj1.subtraction())
print("Multiplication:", obj1.multiplication())
print("Division:", obj1.division())

obj2 = Arithmetic()

obj2.accept()

print("Addition:", obj2.addition())
print("Subtraction:", obj2.subtraction())
print("Multiplication:", obj2.multiplication())
print("Division:", obj2.division())


        
        
