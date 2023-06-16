def insertion_sort(arr):
    n = len(arr)
    for j in range (1, n):
        i = j - 1
        key = arr[j]
        while arr[i] > key and (i >= 0):
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    return arr

arr = [5,3,1,4,2]
print(insertion_sort(arr))