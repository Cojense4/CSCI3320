from random import randint
import time


def n_squared_algorithm(n_array_A, k_twinSum_value, cur_time):
    pass


def n_log_n_algorithm(n_array_A, k_twinSum_value, cur_time):
    pass


def n_algorithm(n_array_A, k_twinSum_value, cur_time):
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
    cur_time = time.time()
    A, K = main()
    print("Running the alorithms ...")
    cur_time = time.time()
    n_squared_result, n_squared_time = n_squared_algorithm(A, K, cur_time)
    cur_time = time.time()
    n_log_n_result, n_log_n_time = n_log_n_algorithm(A, K, cur_time)
    cur_time = time.time()
    n_result, n_time = n_algorithm(A, K, cur_time)
    print(A, "\n", K)
