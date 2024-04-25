from random import randint
import time


def quadratic_algorithm(n_array_A, k_twinSum_value):
    pass


def main():
    n = int(input("Enter size of random array: "))
    if n < 50:
        n_array_A = []
        for i in range(n):
            n_array_A.append(randint(-99, 99))
        print(n_array_A)
    else:
        n_array_A = []
        for i in range(n):
            n_array_A.append(randint(-99, 99))
    k_TwinSum_value = int(input("Enter the K value: "))
    return n_array_A, k_TwinSum_value


if __name__ == '__main__':
    A, K = main()
    print("Running the alorithms ...")
    quadratic_algorithm(A, K)
    print(A, "\n", K)
