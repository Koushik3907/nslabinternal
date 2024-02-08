#1.a
def encrypt(text,s):
    result=""
    for i in range(len(text)):
        char=text[i]
        if result == "":
            result=result+""
        if(char.isupper()):
            result=result+chr((ord(char)+s-65)%26+65)
        else:
            result=result+chr((ord(char)+s-97)%26+97)
    return result
    
text = input("Enter the text")
s = int(input("Enter the shifts"))
text=text.lower()
print(encrypt(text,s))

        