def sort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        pos = i
        while pos > 0 and arr[pos-1] > curr:
            arr[pos] = arr[pos-1]
            pos -= 1
        arr[pos] = curr
    return arr


print(sort([1, 3, 2, 4, 6, 5]))
