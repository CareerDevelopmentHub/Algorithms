import math as m

x=float(input('Enter the x coordinate:'))
y=float(input('Enter the y coordinate:'))
r=10
radius=float(m.sqrt((x**2)+(y**2)))

if(radius==r):
   print('Both circles are equal')
elif(radius>r):
    print('Point is not in the circle')
else:
    print('Point is in the circle')
   




