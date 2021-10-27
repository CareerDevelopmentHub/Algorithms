k=(-1)

n=int(input("Enter a number"))

sum=0

for i in range(1,n+1,2):

 k=k*(-1)

 print(k*i,end=" ")

 sum+=(k*i)

print()

print("sum =",sum)
