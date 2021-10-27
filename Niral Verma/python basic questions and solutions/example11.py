marks= int(input("Enter Marks Obtained: "))

if marks>=90 :
    print("Your Grade is O")
elif marks>=80 and marks<90:
    print("Your Grade is A")
elif marks>=70 and marks<80:
    print("Your Grade is B")
elif marks>=60 and marks<70:
    print("Your Grade is C")
elif marks>=50 and marks<60:
    print("Your Grade is D")
elif marks>=40 and marks<50:
    print("Your Grade is E")
elif marks<40:
    print("Your Grade is F")
else:
    print("Invalid Input!")
