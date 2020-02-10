def insertion_sort(arr):
    for sort_len in range(1, len(arr)):
        cur_item = arr[sort_len] #next unsorted item
        insert_idx = sort_len # current index of item

        #iterate until we reach correct insert spot
        while insert_idx > 0 and cur_item < arr[insert_idx - 1]:
            arr[insert_idx] = arr[insert_idx - 1] #shift
            insert_idx += -1

        #insert item at correct spot
        arr[insert_idx] = cur_item
    return arr

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)