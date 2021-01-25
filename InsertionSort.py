def InsertionSort(arr):
    for i in range(1 , len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1 
        arr[j+1] = key


arr = [8,4,6,7,3,9,1]
InsertionSort(arr)
print(arr)