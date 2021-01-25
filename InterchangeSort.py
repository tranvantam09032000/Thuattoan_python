def InterchangeSort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp


arr = [5,4,1,7,2,3,8]
InterchangeSort(arr)
print(arr)