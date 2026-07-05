def displayWithoutSpace():
    for i in range(10,0,-1):
        print(i,end="  ")#print() has 2 parameters and default value of the second parameter "end" is /n but here we changed it to "  " which adds 2 spaces after each print and does not go to the next line as usual
    return

def main():
    displayWithoutSpace()
    return

if __name__ == "__main__":
    main()
