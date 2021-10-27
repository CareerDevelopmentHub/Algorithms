a= float(input("Enter 1st number : "))
b= float(input("Enter 2nd number : "))
c= float(input("Enter 3rd number : "))
d= float(input("Enter 4th number : "))
e= float(input("Enter 5th number : "))
f= float(input("Enter 6th number : "))

x = e*d-b*f/a*d-b*c
y=a*f-e*c/a*d-b*c

if (a*d - b*c == 0):
    print("The equation has no solution")

else:
    print ("x=", x, "y=", y)
