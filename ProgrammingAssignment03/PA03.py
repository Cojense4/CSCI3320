from random import randint
from time import time_ns


def n_squared(n_array, k_value, cur_time):
    """
    This function checks if there are two numbers in the array whose sum equals to K using a brute force approach.

    It iterates over each pair of numbers in the array and checks if their sum equals to K. If such a pair is found, the function returns True and the two numbers.
    If no such pair is found after checking all pairs, the function returns False and None.

    Parameters:
    n_array (list): The array to be checked.
    k_value (int): The target sum.
    cur_time (int): The current time in nanoseconds.

    Returns:
    list: A list containing a boolean indicating whether two numbers whose sum equals to K were found,
          and a string representation of the two numbers if found and the computation time in nanoseconds.

    Complexity Analysis:
    The worst time complexity of this function is O(n^2) because it involves a nested loop that could potentially run n^2 times in the worst case scenario.
    The space complexity is O(1) as it only uses a constant amount of space to store the temporary variables.
    """

    for i in range(len(n_array)):
        for j in range(i+1, len(n_array)):
            if n_array[i] + n_array[j] == k_value:
                return [True, f'({n_array[i]} + {n_array[j]})', time_ns() - cur_time]
    return [False, None, time_ns() - cur_time]


def nlogn(n_array, k_value, cur_time):
    """
    This function checks if there are two numbers in the array whose sum equals to K using a two-pointer approach.

    The array is first sorted in ascending order. Two pointers, one at the start and one at the end of the array, are used.
    The sum of the numbers at the two pointers is compared with K. If the sum is equal to K, the function returns True and the two numbers.
    If the sum is less than K, the left pointer is moved one step to the right. If the sum is greater than K, the right pointer is moved one step to the left.
    This process continues until the two pointers meet. If no two numbers whose sum equals to K are found, the function returns False and None.

    Parameters:
    n_array (list): The array to be checked.
    k_value (int): The target sum.
    cur_time (int): The current time in nanoseconds.

    Returns:
    list: A list containing a boolean indicating whether two numbers whose sum equals to K were found,
          and a string representation of the two numbers if found and the computation time in nanoseconds.

    Complexity Analysis:
    The worst time complexity of this function is O(n log n) due to the sorting of the array.
    The space complexity is O(1) as it only uses a constant amount of space to store the pointers and temporary variables.
    """

    n_array.sort()  # Sort the array in ascending order
    left = 0
    right = len(n_array) - 1
    while left < right:
        current_sum = n_array[left] + n_array[right]
        if current_sum == k_value:
            return [True, f'({n_array[left]} + {n_array[right]})', time_ns() - cur_time]
        elif current_sum < k_value:
            left += 1
        else:
            right -= 1
    return [False, None, time_ns() - cur_time]


def n(n_array, k_value, cur_time):
    """
    This function checks if there are two numbers in the array whose sum equals to K using a hash table.

    Parameters:
    n_array (list): The array to be checked.
    k_value (int): The target sum.
    cur_time (int): The current time in nanoseconds.

    Returns:
    list: A list containing a boolean indicating whether two numbers whose sum equals to K were found,
          and a string representation of the two numbers if found and the computation time in nanoseconds.

    Complexity Analysis:
    The worst time complexity of this function is O(n) because it involves a loop that runs n times to iterate over the array.
    The space complexity is O(n) because it creates a hash table of size n.

    The function first initializes an empty hash table with a size of 500009.

    It then iterates over the array. For each number, it calculates the complement of the number (i.e., K minus the number) and checks if the complement is in the hash table.
    If the complement is in the hash table, it means that there are two numbers in the array whose sum equals to K, so the function returns True, a string representation of the two numbers, and the computation time.

    If the complement is not in the hash table, the function adds the current number to the hash table and continues to the next number.

    If the function has iterated over all numbers in the array and has not found two numbers whose sum equals to K, it returns False, None, and the computation time.
    """

    # Initialize an empty dictionary
    num_dict = {}

    # Iterate over the array
    for i in range(len(n_array)):
        # Calculate the complement of the current number
        complement = k_value - n_array[i]

        # If the complement is in the dictionary, return True and the two numbers
        if complement in num_dict:
            return [True, f'({n_array[i]} + {complement})', time_ns() - cur_time]

        # Add the current number to the dictionary
        num_dict[n_array[i]] = i

    # If no two numbers whose sum equals to K were found, return False and None
    return [False, None, time_ns() - cur_time]


def main(n, k=None):
    """
    This function generates an array of random integers and asks the user to input a value for K.

    Parameters:
    n (int): The size of the array to be generated.
    k (int, optional): The target sum. If not provided, the user will be asked to input a value.

    Returns:
    tuple: A tuple containing the generated array and the user-inputted K value.
    """

    # Check if the size of the array is less than 50
    if n < 50:
        # Initialize an empty array
        n_array = []
        # Populate the array with random integers between -99 and 99
        for i in range(n):
            n_array.append(randint(-99, 99))
        # Print the generated array
        print(n_array)
    else:
        # Initialize an empty array
        n_array = []
        # Populate the array with random integers between -999999999 and 999999999
        for i in range(n):
            n_array.append(randint(-999999999, 999999999))

    # Ask the user to input a value for K
    if k is None:
        k_value = int(input("Enter the K value: "))
    else:
        k_value = k
    # Return the generated array and the K value
    return n_array, k_value


if __name__ == '__main__':
    """
    This is the main entry point of the program. It prompts the user to input the size of a random array.
    It then generates the array and asks the user to input a value for K.
    It runs three different algorithms to check if there are two numbers in the array whose sum equals to K.
    It prints the results and the computation time for each algorithm.
    The program continues to prompt the user to input the size of a random array until the user inputs 0.
    """

    # Prompt the user to input the size of a random array
    nSize = int(input('Enter size of random array (0 to exit): '))
    while nSize < 10 or nSize > 200000:
        nSize = int(input('Enter size of random array (0 to exit): '))
    # Continue to prompt the user until they input 0
    while nSize:
        # Generate the array and ask the user to input a value for K
        A, K = main(nSize)

        # Print a message indicating that the algorithms are running
        print("Running the algorithms...")

        # Run the three different algorithms
        for i in range(3):
            if i == 0:
                # Run the O(N**2) algorithm
                result = n_squared(A, K, time_ns())
                print(f'\n<O(N**2) Algorithm>')
            elif i == 1:
                # Run the O(NlogN) algorithm
                result = nlogn(A, K, time_ns())
                print(f'\n<O(NlogN) Algorithm>')
            else:
                # Run the O(N) algorithm
                result = n(A, K, time_ns())
                print(f'\n<O(N) Algorithm>')

            # Print the results and the computation time
            if result[0]:
                print('\tYes, there are two numbers whose sum equals to K')
                print(f'\tK = {K}, {result[1]}')
            else:
                print(f'\tNo, there are no two numbers whose sum equals to K')
            print(f'\tTime taken: {result[2]} ns')

        # Prompt the user to input the size of a random array again
        nSize = int(input('Enter size of random array (0 to exit): '))
        while nSize < 10 or nSize > 200000:
            nSize = int(input('Enter size of random array (0 to exit): '))

