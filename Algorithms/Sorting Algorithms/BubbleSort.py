def bubbleSort(arr):
    n = len(arr)

    #total number of iterations = length of array
    for i in range(n):
        #total number of inner iterations, comparing one item to its neighbor value
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    

arr = [14,46,43,27,57,41,45,21,70]
bubbleSort(arr)
print(arr)