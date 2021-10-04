def sort(arr):
    if len(arr) > 1:
        mid = len(arr)/2
        left = arr[:int(mid)]
        right = arr[int(mid):]
        sort(left)
        sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[i]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


print(sort([1, 3, 2, 4, 6, 5]))
