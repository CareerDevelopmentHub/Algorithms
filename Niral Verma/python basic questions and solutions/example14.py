num = int(input("Enter the integer number: "))  
revnum = 0  
  
while (num> 0):  
      
    remainder = num % 10  
    revnum = (revnum * 10) + remainder  
    num = num // 10  

print("The reverse number is : ", revnum)  
