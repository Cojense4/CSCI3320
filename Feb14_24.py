import random as rand
import time as t


def insertion_sort(nList):
	for i in range(len(nList)):
		key = nList[i]
		j = i - 1
		while j >= 0 and key < nList[j]:
			nList[j + 1] = nList[j]
			j -= 1
		nList[j + 1] = key
	return nList


def quick_sort(nList):
	if len(nList) <= 1:
		return nList
	else:
		pivot = nList[0]
		less = [x for x in nList[1:] if x <= pivot]
		greater = [x for x in nList[1:] if x > pivot]
		return quick_sort(less) + [pivot] + quick_sort(greater)


def bubble_sort(nList):
	n = len(nList)
	# Traverse through all array elements
	for i in range(n):
		# Last i elements are already in place, so we don't need to check them
		for j in range(0, n - i - 1):
			# Swap if the element found is greater than the next element
			if nList[j] > nList[j + 1]:
				nList[j], nList[j + 1] = nList[j + 1], nList[j]
	return nList


def shell_sort(nList):
	n = len(nList)
	if n % 2 != 0 and n > 2:
		gap = (n // 2) - 1
	else:
		gap = n // 2

	while gap > 0:
		for i in range(gap, n):
			temp = nList[i]
			j = i
			while j >= gap and nList[j - gap] > temp:
				nList[j] = nList[j - gap]
				j -= gap
			nList[j] = temp
		gap //= 2
	return nList


def main():
	num = int(input("Enter number of elements (N): "))
	L1 = [rand.randint(-9999, 9999) for i in range(num)]
	start = t.time_ns()
	L1_Insertion = insertion_sort(L1)
	tTime = (t.time_ns() - start) / 1000000000
	print(f'{L1_Insertion}\nInsertion sort took {tTime} seconds')
	start = t.time_ns()
	L1_Quick = quick_sort(L1)
	tTime = (t.time_ns() - start) / 1000000000
	print(f'{L1_Quick}\nQuick sort took {tTime} second')
	start = t.time_ns()
	L1_Bubble = bubble_sort(L1)
	tTime = (t.time_ns() - start) / 1000000000
	print(f'{L1_Bubble}\nBubble sort took {tTime} seconds')
	start = t.time_ns()
	L1_Shell = shell_sort(L1)
	tTime = (t.time_ns() - start) / 1000000000
	print(f'{L1_Shell}\nShell sort took {tTime} seconds')


if __name__ == "__main__":
	main()
