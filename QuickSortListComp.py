def quicksort(array):
    if len(array) < 2:
        return array

    pivot = array[0]    # Pivot
    less = [x for x in array[1:] if x <= pivot]
    greater = [x for x in array[1:] if x > pivot]

    # recursively sort the sub-arrays
    return quicksort(less) + [pivot] + quicksort(greater)


nList = [5, 65, 29, 100, 41, 45, 9, 38, 12, 24]
ans = quicksort(nList)
print(f"\n\n\n{ans}")