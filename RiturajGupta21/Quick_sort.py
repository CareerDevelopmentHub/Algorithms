def partition(start,end,ar):
    pivot_ind=start
    pivot=ar[pivot_ind]
    while start<end:
        while start<len(ar) and ar[start]<=pivot:
            start+=1
        while ar[end]>pivot:
            end-=1
        if start<end:
            ar[start],ar[end]=ar[end],ar[start]
    ar[end],ar[pivot_ind]=ar[pivot_ind],ar[end]
    return end
def quick(start,end,ar):
    if start<end:
        p=partition(start,end,ar)
        quick(start,p-1,ar)
        quick(p+1,end,ar)
ar = [ 10, 7, 8, 9, 1, 5 ]
n=len(ar)
quick(0, n - 1, ar)
print ("Sorted array is:") 
for i in range(n): 
	print ("%d" %ar[i],end=" ")
