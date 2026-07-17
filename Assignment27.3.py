class Numbers:

    def __init__(self,Value):
        self.Value = Value
    
    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range (2,self.Value):
            if(self.Value%i==0):
                return False
        
        return True
    
    def ChkPerfect(self):
        sum = 0
        for i in range(1,self.Value):
            if(self.Value%i==0):
                sum += i
        
        return sum == self.Value
    

    def Factors(self):
        print("Printing All The Factors: ")
        for i in range(1,self.Value+1):
            if(self.Value%i==0):
                print(i, end=" ")
    
    def SumFactors(self):
        sum = 0
        for i in range(1,self.Value+1):
            if(self.Value%i==0):
                sum+=i
        return sum

nObj1 = Numbers(6)

print("Value:", nObj1.Value)
print("Is Prime:", nObj1.ChkPrime())
print("Is Perfect:", nObj1.ChkPerfect())
nObj1.Factors()
print("\nSum of Factors:", nObj1.SumFactors())


nObj2 = Numbers(17)

print("Value:", nObj2.Value)
print("Is Prime:", nObj2.ChkPrime())
print("Is Perfect:", nObj2.ChkPerfect())
nObj2.Factors()
print("\nSum of Factors:", nObj2.SumFactors())


nObj3 = Numbers(28)

print("Value:", nObj3.Value)
print("Is Prime:", nObj3.ChkPrime())
print("Is Perfect:", nObj3.ChkPerfect())
nObj3.Factors()
print("\nSum of Factors:", nObj3.SumFactors())

nObj4 = Numbers(12)

print("Value:", nObj4.Value)
print("Is Prime:", nObj4.ChkPrime())
print("Is Perfect:", nObj4.ChkPerfect())
nObj4.Factors()
print("\nSum of Factors:", nObj4.SumFactors())
