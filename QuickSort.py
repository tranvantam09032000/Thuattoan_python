def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end

    while True:

        while left <= right and arr[right] >= pivot:
            right = right - 1
        while left <= right and arr[left] <= pivot:
            left = left + 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:   
            break

    arr[start], arr[right] = arr[right], arr[start]

    return right


def QuickSort(arr, start, end):
    if start >= end:
        return

    p = partition(arr, start, end)
    QuickSort(arr, start, p-1)
    QuickSort(arr, p+1, end)

arr = [5,4,1,7,2,3,8]
QuickSort(arr,0,len(arr) -1 )
print(arr)