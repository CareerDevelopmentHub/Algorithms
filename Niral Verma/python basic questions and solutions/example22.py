# to compute taylors series 1+x+x^2/2!....

import math
x=float(input('Enter value of x: '))
total_e=1
term=1
i=0
while(math.fabs(term)>0.000001):
    i=i+1
    term=term*x/i
    total_e-total_e + term

print('e(',x,')=',total_e)

print('e(',x,')=',math.exp(x))
