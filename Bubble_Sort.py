# BUBBLE SORT
# https://www.youtube.com/watch?v=xli_FI7CuzA

# O(n^2) search time average
def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [5, 4, 3, 2, 1]
print(bubble_sort(arr))
