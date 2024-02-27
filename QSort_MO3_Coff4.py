def quicksort(array):
    def median_of_three(array):
        first = array[0]
        middle = array[len(array) // 2]
        last = array[-1]

        if first < middle < last:
            return middle
        elif last < middle < first:
            return middle
        elif first < last < middle:
            return last
        elif middle < last < first:
            return last
        elif middle < first < last:
            return first
        else:
            return first

    def partition(array, pivot):
        less = []
        equal = []
        greater = []

        for element in array:
            if element < pivot:
                less.append(element)
            elif element == pivot:
                equal.append(element)
            else:
                greater.append(element)

        return less, equal, greater

    def insertion_sort(array):
        for i in range(1, len(array)):
            current_element = array[i]
            j = i - 1
            while j >= 0 and array[j] > current_element:
                array[j + 1] = array[j]
                j -= 1

            array[j + 1] = current_element

        return array

    if len(array) <= 4:
        return insertion_sort(array)

    # Choose the median of the first, middle, and last elements as the pivot
    pivot = median_of_three(array)
    # Partition the array around the pivot
    less, equal, greater = partition(array, pivot)

    # Recursively sort the less and greater subarrays
    return quicksort(less) + equal + quicksort(greater)


nList = [12, 4, 3, 9, 18, 7, 2, 17, 13, 1, 5, 6]
ans = quicksort(nList)
print(ans)
