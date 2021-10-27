X  = int(input('Enter value for X-axis :'))
Y = int(input('Enter value for Y-axis :'))

if X > 0 and Y > 0:
    print('X and Y lie at First quadrant')

elif X < 0 and Y > 0:
    print('X and Y lie at Second quadrant')

elif X < 0 and Y < 0:
    print('X and Y lie at Third quadrant')

elif X > 0 and Y < 0:
    print('X and Y lie at Fourth quadrant')
else: 
    print('X and Y lie at Origin')
