
# Example function A.
def functionA():
	for i in range(n): 				# n**1
		for j in range(0, n**2): 	# n**1
			if j % 1 == 0:			# 
				for k in range(n**2):
					sum += 1

# Factorial function
# T(n) = T(n-1) + C; C is an arbitrary constant
# Example of a telescoping function, see notebook
def functionB():
	if n <= 1: return 1
	return n*functionB(n-1)

# Factorial similar function
# T(n) = T(n - 1) + C
def functionC(x, y):
	if x == 0:
		return y
	else:
		return functionC(x-1, x + y)	


# Binary search function
# Divides array in half recursively, returns middle
def binary_search(arr, start, end, key): 
	if start > end:
		return None
	mid = start + (end - start)//2 
	if arr[mid] < key:
		return binary_search(arr, mid+1, end, key) 
	elif arr[mid] > key:
		return binary_search(arr, start, mid-1, key) 
	else:
		return mid


# Another recursion function
# Recursion Relation T(n) = T(n - 1) + O(n)
# Big O notation: T(n) = C * (n(n+1)/2) = O(n**2)
# Note: O(n) == C*n; C is any constant
def functionD(n):
	i = 0
	if n > 1:
		functionD(n - 1)
	for i in range(n):
		print(" * ", end='')	


# Recursion Relation: T(n) = 
def functionE(a, n):
	if n == 1:
		return a[0]
	else:
		x = functionE(a, n - 1)
	if x > a[n - 1]:
		return x
	else:
		return a[n - 1]			
				