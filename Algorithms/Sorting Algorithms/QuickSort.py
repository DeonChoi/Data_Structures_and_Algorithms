def quicksort(arr):
    #base case
    if len(arr) <= 1:
        return arr

    #setting pivot as the middle value
    pivot = len(arr) // 2

    # l = [i for i in arr if i < arr[pivot]]
    # print('left ', l)
    # m = [i for i in arr if i == arr[pivot]]
    # print('m ', m)
    # r = [i for i in arr if i > arr[pivot]]
    # print('right ', r)

    #iterates through array, and appends it to a new "less than" array if current value of iteration is less than pivot value
    l = []
    for i in arr:
        if i < arr[pivot]:
            l.append(i)

    #iterates through array, and appends/assigns current value of iteration as new pivot if current value of iteration is equal to current pivot value
    m = []
    for i in arr:
        if i == arr[pivot]:
            m.append(i)

    #iterates through array, and appends it to a new "greater than" array if current value of iteration is greater than pivot value
    r = []
    for i in arr:
        if i > arr[pivot]:
            r.append(i)

    return quicksort(l) + m + quicksort(r)


array_to_be_sorted = [3,45,1,2,34]
print("Original Array: ",array_to_be_sorted)
print("Sorted Array: ",quicksort(array_to_be_sorted))