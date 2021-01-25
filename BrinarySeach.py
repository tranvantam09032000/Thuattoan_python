def BrinarySeach(arr, left , right , key):
    if left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return BrinarySeach(arr , mid+1 , right , key)
        else:
            return BrinarySeach(arr , left , mid - 1 , key)
    else:
        return "no seach!"

arr = [1,2,3,4,5,6]
result = BrinarySeach(arr , 0 , len(arr) - 1 , 1)
print(result)