ch = input("Enter Any Character : ")

if(ch >= 'A' and ch <= 'Z'): 
    print("The Given Character ", ch, "is a Capital Alphabet")
elif(ch >= 'a' and ch <= 'z'):
    print("The Given Character ", ch, "is a small case Alphabet")
elif(ch >= '0' and ch <= '9'):
    print("The Given Character ", ch, "is a Digit")
else:
    print("The Given Character ", ch, "is a Special Character")
