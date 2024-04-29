from PA03 import *
import csv


def test():
    """
    This function runs a series of tests on three algorithms: O(N**2), O(NlogN), and O(N).
    It prompts the user to enter the input size, then generates an array and a target sum using the main function.
    It runs each algorithm on the generated array and target sum, and records the computation time of each algorithm.
    The results of each test, including the computation times, are written to a CSV file named 'results_{input_size}.csv'.
    This process is repeated 10 times.
    After all tests, it computes the average computation time for each algorithm and writes it to the CSV file.

    Parameters:
    None

    Returns:
    None
    """

    # Prompt the user to enter the input size
    input_size = int(input("Enter the input size: "))

    # Initialize variables to store the total computation times for each algorithm
    total_time_n_squared = 0
    total_time_nlogn = 0
    total_time_n = 0

    # Define the number of tests to run
    num_tests = 10

    # Open a CSV file to write the results
    with open(f'results_{input_size}.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row to the CSV file
        writer.writerow([f'Input size ({input_size})', 'O(N**2) algorithm', 'O(NlogN) algorithm', 'O(N) algorithm'])

    # Run the tests 10 times
    for i in range(num_tests):
        # Generate an array and a target sum
        array, k = main(input_size, 2000000000)

        # Run each algorithm and record the computation time
        comp_results = [n_squared(array, k, time_ns()), nlogn(array, k, time_ns()), n(array, k, time_ns())]

        # Add the computation times to the corresponding total
        total_time_n_squared += comp_results[0][2]
        total_time_nlogn += comp_results[1][2]
        total_time_n += comp_results[2][2]

        # Open the CSV file to append the results
        with open(f'results_{input_size}.csv', 'a', newline='') as file:
            writer = csv.writer(file)

            # Write the results of the current test to the CSV file
            writer.writerow([f'Test {i+1}', comp_results[0][2], comp_results[1][2], comp_results[2][2]])

    # Calculate the average computation time for each algorithm
    avg_time_n_squared = int(total_time_n_squared / num_tests)
    avg_time_nlogn = int(total_time_nlogn / num_tests)
    avg_time_n = int(total_time_n / num_tests)

    # Open the CSV file to append the averages
    with open(f'results_{input_size}.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        # Write the averages to the CSV file
        writer.writerow(['Average', avg_time_n_squared, avg_time_nlogn, avg_time_n])


if __name__ == "__main__":
    test()

