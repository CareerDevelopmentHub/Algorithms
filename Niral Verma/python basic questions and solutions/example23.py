#to display the Fibonacci sequence up to n-th term

n = int(input("Enter number of terms: "))

n1, n2 = 0, 1
count = 0

if n <= 0:
   print("Enter a positive integer")

elif n == 1:
   print("Fibonacci sequence upto",n,": ", n1)

else:
   print("Fibonacci sequence: ")
   while count < n:     
       print(n1)
       nth = n1 + n2
  
       n1 = n2
       n2 = nth
       count += 1
