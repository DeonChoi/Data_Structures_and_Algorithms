def mergeSort(nlist):
    print("Splitting ", nlist)

    # if len(nlist) <= 1:
    #     return nlist

    if len(nlist) > 1:
        mid = len(nlist) // 2
        left_half, right_half = nlist[:mid], nlist[mid:]

        mergeSort(left_half)
        mergeSort(right_half)
        i=j=k=0       

        #loop that runs when both left_half and right_half array are NOT empty
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                nlist[k] = left_half[i]
                i += 1
            else:
                nlist[k] = right_half[j]
                j += 1
            k += 1

        #loop that runs if right_half array is empty
        while i < len(left_half):
            nlist[k] = left_half[i]
            i += 1
            k += 1

        #loop that runs if left_half array is empty
        while j < len(right_half):
            nlist[k] = right_half[j]
            j += 1
            k += 1

    print("Merging ",nlist)

nlist = [14,46,43,27,57,41,45,21,70]
nlist_2 = [1]
mergeSort(nlist)
#mergeSort(nlist_2)
print(nlist)
#print(nlist_2)