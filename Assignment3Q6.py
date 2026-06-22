'''#question -> write a program to display data type memory address and size 
in bytes of a variable entered by the user '''
from sys import getsizeof
import ast

def assignment(value):
    print("Type of Entered Value Is:",type(value))
    print("Memory Address Of Given Value Is:",id(value))
    print("Size Of Value In Bytes Is:",getsizeof(value))

def main():
    val = ast.literal_eval(input("Enter the desired value:"))
    assignment(val)

if __name__ == "__main__":
    main()

'''here we are using ast.literal_eval as we can't typecast input's return 
statement because user can type either a string or list or tuple or integer 
or anything but the drawback is user will have to input string between 
double quotes if the user wants to input a string and similiarly for 
lists and tuples input should be inside appropriate brackets'''

