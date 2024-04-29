# Programming Assignment 03

This project contains Python scripts for testing the performance of three different algorithms that check if there are two numbers in an array whose sum equals to a given value (K). The three algorithms have different time complexities: O(N^2), O(NlogN), and O(N).

## Files

- `PA03.py`: This is the main script that contains the three algorithms and a main function to generate a random array and a K value.
- `PA03_test.py`: This script uses the functions from `PA03.py` to run a series of tests on the three algorithms and writes the results to a CSV file.

## How to Run

1. Run `PA03_test.py` script. It will prompt you to enter the input size for the array.
2. The script will then run the three algorithms on the generated array and record the computation time of each algorithm.
3. The results of each test, including the computation times, are written to a CSV file named 'results_{input_size}.csv'.
4. This process is repeated 10 times. After all tests, it computes the average computation time for each algorithm and writes it to the CSV file.

## Requirements

- Python 3.6 or higher

## Note

Please make sure to have the `PA03.py` and `PA03_test.py` in the same directory before running the tests.