def generateTable(n1):
    table = list()
    for i in range(1,11):
        t = i*n1
        table.append(t)
    return table

def main():
    no1 = int(input("Enter the number you want table for: "))
    ans = generateTable(no1)
    print("Table for given number is as follows - ")
    for i in ans:
        print(i)
    return

if __name__ == "__main__":
    main()
