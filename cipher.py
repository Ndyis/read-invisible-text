file = open("cipher.txt","r").read()
str = ""
for ch in file:
    if ord(ch)==32:
        str+="0"
    else:
        str+="1"
print(str)
    
        