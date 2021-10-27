import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
   
d = (b**2) - (4*a*c)
print('Discriminant is ',d)

sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a) 
if d > 0:
        print('Two Solutions: ', sol1,sol2)
elif d == 0:
        print('One Solution :', sol1)
else:
        print('No Real Solutions')
