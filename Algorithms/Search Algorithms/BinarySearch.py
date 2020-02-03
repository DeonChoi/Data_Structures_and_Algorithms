"""
You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list.
"""



def binary_search(input_array, value):
    first = 0
    last = len(input_array)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if input_array[mid] == value:
            index = mid
        else:
            if value < input_array[mid]:
                last = mid - 1
            elif value > input_array[mid]:
                first = mid + 1
    return index

test_list = [1,3,9,11,15,19,29]
test_val1 = 26
test_val2 = 15
#returns -1
print(binary_search(test_list, 29))
#returns 4
#print(binary_search(test_list, test_val2))

#recursive
def binary_search_r(arr,value):
    if len(arr) == 0 or (len(arr) == 1 and arr[0] != value):
        return False

    mid = arr[len(arr) // 2]

    if value == mid: 
        return True
    elif value < mid:  
        return binary_search_r(arr[:len(arr) // 2], value)
    elif value > mid:  
        return binary_search_r(arr[len(arr) // 2+1:], value)


arr = [1,3,9,11,15,19,29]
print(binary_search_r(arr, 19))