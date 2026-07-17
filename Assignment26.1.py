class Demo:
    value = None

    def __init__(self,no1,no2):
        self.no1 = no1
        self.no2 = no2
    
    def fun(self):
        print(self.no1)
        print(self.no2)
    
    def gun(self):
        print(self.no1)
        print(self.no2)
    
Obj1 = Demo(11,21)
Obj2 = Demo(51,101)
Obj1.fun()
Obj2.fun()
Obj1.gun()
Obj2.gun()