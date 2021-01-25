def ShellSort(arr):
        interval = len(arr)//2
        while interval > 0:
                for i in range(interval, len(arr)):
                    if arr[i] > arr[i - interval]:
                        temp = arr[i]
                        arr[i] = arr[i - interval]
                        arr[i - interval] = temp
                interval //= 2
   
        for i in range(1 , len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] < key:
                arr[j+1] = arr[j]
                j -= 1 
            arr[j+1] = key

arr = [5,4,1,7,2,3,8]
ShellSort(arr)
print(arr)