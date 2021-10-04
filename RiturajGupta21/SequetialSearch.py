def search(arr, ele):
    pos = 0
    f = False
    while pos < len(arr) and not f:
        if arr[pos] == ele:
            f = True
            break
        else:
            pos += 1
    return f


print(search([1, 2, 3, 4, 5, 6, 7, 8], 8))
