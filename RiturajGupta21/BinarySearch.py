def search(arr, ele):
    first = 0
    last = len(arr)-1
    f = False
    while (first <= last and not f):
        mid = (first+last)//2
        if arr[mid] == ele:
            f = True
        else:
            if ele < arr[mid]:
                last = mid-1
            else:
                first = mid+1
    return f


print(search([1, 2, 3, 4, 5, 6, 7, 8], 8))
