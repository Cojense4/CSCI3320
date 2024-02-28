def quicksort(array):
    def median_of_three(array, left, right):
        mid = (left + right) // 2
        a = array[left]
        b = array[mid]
        c = array[right]

        if a < b:
            if b < c:
                return b
            elif a < c:
                return c
            else:
                return a
        else:
            if c < b:
                return b
            elif c < a:
                return c
            else:
                return a

    def insertion_sort(array):
        for i in range(1, len(array)):
            current_element = array[i]
            j = i - 1
            while j >= 0 and array[j] > current_element:
                array[j + 1] = array[j]
                j -= 1

            array[j + 1] = current_element

    if len(array) <= 4:
        insertion_sort(array)
        return

    # Choose the median of the first, middle, and last elements as the pivot
    pivot = median_of_three(array, 0, len(array) - 1)

    # Partition the array around the pivot
    i = 0
    j = len(array) - 1
    while i < j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    # Recursively sort the two subarrays
    quicksort(array[:i])
    quicksort(array[i:])


nList = [12, 4, 3, 9, 18, 7, 2, 17, 13, 1, 5, 6]
quicksort(nList)
print(nList)
