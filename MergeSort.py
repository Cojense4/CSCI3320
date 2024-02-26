def merge_sort(array):
    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if right[j] > left[i]:
                result.append(left[i])
                print(f"\n{right[j]} > {left[i]}")
                i += 1
            else:
                result.append(right[j])
                print(f"\n{right[j]} < {left[i]}")
                j += 1
            print(result)

        # Add the remaining elements from the left and right arrays
        result += left[i:]
        if i < len(left):
            print(f"\nAdded left:{left[i:]}")
        result += right[j:]
        if j < len(right):
            print(f"\nAdded right:{right[j:]}")

        print(result)
        return result

    if len(array) <= 1:
        return array

    # Divide the array into two halves
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    # Merge the two sorted halves
    return merge(left, right)


nList = [5, 65, 29, 100, 41, 45, 9, 38, 12, 24]
ans = merge_sort(nList)
print(f"\n\n\n{ans}")
