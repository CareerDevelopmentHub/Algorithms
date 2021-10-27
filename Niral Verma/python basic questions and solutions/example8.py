month= int(input("Enter the month as integer: "))
year= int(input("Enter the year as integer: "))

if (month==1):
    print("January " + year + " had 31 days")
elif(month==2):
    if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
       print("February " , year , " had 29 days")
    else:
       print("February " , year , " had 28 days")
elif(month==3):
    print("March " , year , " had 31 days")
elif(month==4):
    print("April " , year , " had 30 days")
elif(month==5):
    print("May " , year , " had 31 days")
elif(month==6):
    print("June " , year , " had 30 days")
elif(month==7):
    print("July " , year , " had 31 days")
elif(month==8):
    print("August " , year , " had 31 days")
elif(month==9):
    print("September " , year , " had 30 days")
elif(month==10):
    print( "October " , year , " had 31 days")
elif(month==11):
    print("November " , year , " had 30 days")
elif(month==12):
    print( "December " , year , " had 31 days")
else:
    print("Enter a valid number")
 
                


