funcB(n):
if (n > 0):
	funcB(n - 1)
	print(n, end="")
	funcB(n - 1)

