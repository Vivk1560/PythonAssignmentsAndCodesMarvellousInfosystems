def checkVowel(abc):
    return abc.lower() in "aeiou"

def main():
    char = input("Enter the character you wanna check for vowel or consonant: ")
    if(len(char)!=1):
        print("Invalid input, expected only a single character")
    else:
        if(checkVowel(char)==True):
            print("Entered character is a vowel")
        else:
            print("Entered character is a consonant")

if __name__ == "__main__":
    main()