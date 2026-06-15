x =15 #int -> numeric
y = "Vivaan" #str -> text
z = 55.5 #float -> numeric
m = 44 + 5j #complex -> numeric
n = True #bool -> bool
k = range(1,5,2) #range -> sequence
j = {"A":10,"B":20} #dict -> mapping
l = {10,20,30} #set -> set
s = [10,20,30] #list -> sequence
p = (10,20,30) #tupple -> sequence
q = None #none -> none

def displayValue():
    print("Value Of x which is int is:",x)
    print("Value of y which is String is:",y)
    print("Value of z which is float is:",z)
    print("Value of m which is complex is:",m)
    print("Value of n which is bool is:",n)
    print("Value of k which is range is:",k)
    print("Value of j which is dict is:",j)
    print("Value of l which is set is:",l)
    print("Value of s which is list is:",s)
    print("Value of p which is tupple is:",p)
    print("Value of q which is none is:",q)

def displayType():
    print("Type Of x which is int is:",type(x))
    print("Type of y which is String is:",type(y))
    print("Type of z which is float is:",type(z))
    print("Type of m which is complex is:",type(m))
    print("Type of n which is bool is:",type(n))
    print("Type of k which is range is:",type(k))
    print("Type of j which is dict is:",type(j))
    print("Type of l which is set is:",type(l))
    print("Type of s which is list is:",type(s))
    print("Type of p which is tupple is:",type(p))
    print("Type of q which is none is:",type(q))

def displayID():
    print("MemoryAddress Of x which is int is:",id(x))
    print("MemoryAddress of y which is String is:",id(y))
    print("MemoryAddress of z which is float is:",id(z))
    print("MemoryAddress of m which is complex is:",id(m))
    print("MemoryAddress of n which is bool is:",id(n))
    print("MemoryAddress of k which is range is:",id(k))
    print("MemoryAddress of j which is dict is:",id(j))
    print("MemoryAddress of l which is set is:",id(l))
    print("MemoryAddress of s which is list is:",id(s))
    print("MemoryAddress of p which is tupple is:",id(p))
    print("MemoryAddress of q which is none is:",id(q))

def main():
    displayValue() #to display value pointed by variable
    displayType() #to display data type of variable
    displayID() #to display memory address of the variable

if(__name__ == "__main__"):
    main()