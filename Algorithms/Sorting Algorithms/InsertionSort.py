
#create random arrays for testing Insertion Sort method
def create_array(size = 10, max = 50):
    from random import randint
    return [randint(0, max) for _ in range(size)]


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

new_arr = create_array()
print(new_arr)
new_arr = insertion_sort(new_arr)
print(new_arr)