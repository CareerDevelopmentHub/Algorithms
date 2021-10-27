#to compute x^n/n!

x , n = map(int,input('Enter numbers x and n: ').split())

factorial=1

for i in range(1,n + 1):
       factorial = factorial*i
       
print('Result is ',(x**n)/factorial)
