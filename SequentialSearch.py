def SequentialSearch(arr, item):
    i = 0
    while i < len(arr):
        if arr[i] == item:
            return True
        i += 1
    return False

arr = [1,2,3,4,5,6,7,9]
if SequentialSearch(arr,10) == True:
    print("tìm thấy!")
else:
    print("không tìm thấy!")