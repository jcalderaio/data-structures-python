# SELECTION SORT

# O(n^2) search time average
# https://www.youtube.com/watch?v=g-PGLbMth_g

def selection_sort(arr):
    # iterate over the list (nested loops)
    # first loop (i) points to leftmost number (min_idx)
    # 2nd loop (j) finds the smallest number and, if smaller than min_idx, becomees the new min_idx
    # i and min_idx switch places, and now another int is added to the left (sorted) side
    for i in range(len(arr)):
        # pointer to
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


A = [34, 23, 75, 23, 5, 76, 34, 87, 4, 6, 3, 76, 0, 2, 99]
print(selection_sort(A))
