    
def BubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] < arr[j+1] :
                # print("loop: "+str(i))
                # print(str(arr[j]) + " " + str(arr[j+1]))
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                # print(arr)
arr = [6,9,7,3,10,1]
BubbleSort(arr)
print(arr)
