def sort(arr):
    for i in range(len(arr)-1, 0, -1):
        pos = 0
        for j in range(1, i+1):
            if arr[j] > arr[pos]:
                pos = j
        temp = arr[i]
        arr[i] = arr[pos]
        arr[pos] = temp
    return arr


print(sort([1, 3, 2, 4, 6, 5]))
