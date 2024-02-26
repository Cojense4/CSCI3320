def quicksort(array):
    if len(array) < 2:
        # base case, the array is already sorted
        return array

    # choose a pivot element
    pivot = array[0]

    # partition the array around the pivot
    less = [x for x in array[1:] if x <= pivot]
    greater = [x for x in array[1:] if x > pivot]

    # recursively sort the sub-arrays
    return quicksort(less) + [pivot] + quicksort(greater)


nList = [5, 65, 29, 100, 41, 45, 9, 38, 12, 24]
ans = quicksort(nList)
print(f"\n\n\n{ans}")