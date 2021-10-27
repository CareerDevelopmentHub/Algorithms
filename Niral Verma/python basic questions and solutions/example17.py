i=0
for x in range(100,1001):
    if x%5==0 and x%6==0:
        print(x,end=' ')
        i+=1
    if(i==10):
            i=0
            print()
