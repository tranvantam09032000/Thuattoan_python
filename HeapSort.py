def heapify(arr, n, i): 
    largest = i  
    l = 2 * i + 1    
    r = 2 * i + 2    
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  
  
        heapify(arr, n, largest) 
  
def heapSort(arr): 

    for i in range(len(arr) // 2 - 1, -1 , -1): 
        heapify(arr, len(arr) - 1, i) 
  
    for i in range(len(arr)-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0) 

arr = [6,9,7,3,10,1]
heapSort(arr)
print(arr)
