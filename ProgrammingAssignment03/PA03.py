from random import randint
from time import time_ns


def nSquared(nArray, kValue, curTime):
    for i in range(len(nArray)):
        for j in range(i+1, len(nArray)):
            if nArray[i] + nArray[j] == kValue:
                return [True, f'({nArray[i]} + {nArray[j]})'], time_ns() - curTime
    return False, time_ns() - curTime


def nlogn(nArray, kValue, curTime):
    nArray.sort()  # Sort the array in ascending order
    left = 0
    right = len(nArray) - 1
    while left < right:
        currentSum = nArray[left] + nArray[right]
        if currentSum == kValue:
            return [True, f'({nArray[left]} + {nArray[right]})'], time_ns() - curTime
        elif currentSum < kValue:
            left += 1
        else:
            right -= 1
    return False, time_ns() - curTime


def n(nArray, kValue, curTime):
    num_dict = {}
    for i in range(len(nArray)):
        complement = kValue - nArray[i]
        if complement in num_dict:
            return [True, f'({nArray[i]} + {complement})'], time_ns() - curTime
        num_dict[nArray[i]] = i
    return False, time_ns() - curTime

def main(n):
    if n < 50:
        nArray = []
        for i in range(n):
            nArray.append(randint(-99, 99))
        print(nArray)
    else:
        nArray = []
        for i in range(n):
            nArray.append(randint(-99, 99))
    kValue = int(input("Enter the K value: "))
    return nArray, kValue


if __name__ == '__main__':
    nSize = int(input('Enter size of random array (0 to exit): '))
    while nSize:
        A, K = main(nSize)
        print("Running the algorithms...")
        for i in range(3):
            if i == 0:
                result, compTime = nSquared(A, K, time_ns())
                print(f'\n<O(N**2) Algorithm>')
            elif i == 1:
                result, compTime = nlogn(A, K, time_ns())
                print(f'\n<O(NlogN) Algorithm>')
            else:
                result, compTime = n(A, K, time_ns())
                print(f'\n<O(N) Algorithm>')
            if result[0]:
                print('\tYes, there are two numbers whose sum equals to K')
                print(f'\tK={K}, {result[1]}')
            else:
                print(f'\tNo, there are no two numbers whose sum equals to K')
            print(f'\tTime taken: {compTime} ns')