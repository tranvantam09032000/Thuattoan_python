def SelectionSort(arr):
    for i in range(len(arr)):
        max = i
        for j in range(i+1 , len(arr)):
            if arr[max] < arr[j]:
                max = j
        temp = arr[max]
        arr[max] = arr[i]
        arr[i] = temp
                

arr = [5,4,7,3,8,1,2]
SelectionSort(arr)
print(arr)