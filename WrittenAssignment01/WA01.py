# O(n**2)
def fun1(n):
    i = 1               # C
    sumA = 0            # C
    while i < n * n:    # While loop = O(N^2)
        sumA += 1       # C
        i += 3          # C


# O(log(n))
def fun2(n):
    i = 1               # C
    sumB = 0            # C
    while i < n * n:    # While loop = O(log (N))
        sumB += 1       # C
        i *= 3          # C


# O(n**7)
def fun3(n):
    process = 0
    sumC = 0                        # C
    for i in range(n):              # N
        process += 1
        for j in range(i*2, n**3):  # For loop = O(n**3/2i)
            process += 1
            for k in range(j):      # For loop = O(n**3/2i)
                process += 1
                sumC += 1           # C
    return sumC, process


# O(n**4)
def fun4(n):
    process = 0
    sumD = 0                        # C
    for i in range(n):              # N
        process += 1
        for j in range(i*2, n**3):  # N**3/2i
            process += 1
            if j < i:               # Never happens: N
                process += 1
                for k in range(j):  # Never happens: N**3
                    process += 1
                    sumD += 1       # C
    return sumD, process


# O(N)
def fun5():
    k = 0                   # C
    n = 5                   # C
    if n > 10:              # C
        k = n
    else:                       # C
        for i in range(n):
            for j in range(n):
                k += 1


# T(N) = T(N-1) + O(N) + C
# O(N)
def fun6(n):
    i = 0
    if n > 1:
        fun6(n - 1)
    for i in range(n):
        print(" * ", end="")


def fun8(n, start=0, end=0, aux=0):
    processes = 0
    if n == 1:
        processes += 1
        print("Move disk 1 from", start, "to", end, " - DONE")
        return
    fun8(n=n-1, start=start, aux=aux, end=end)
    print("Move disk", n, "from", start, "to", end)
    fun8(n=n-1, start=start, aux=aux, end=end)


def fun8_2(n, r=0):
    if n == 1:
        print(" - DONE")
        return
    fun8_2(n-1, r)
    print(n)
    fun8_2(n-1)


def fib_sum(N):
    N -= 2
    sumE = 0
    if N < 0:
        raise ValueError("N must be a non=negative integer, yours was ", N)
    elif N == 0 or N == 1:
        sumE += 1
        return sumE
    else:
        sumE += fib_sum(N - 1, sumE)
        sumE += fib_sum(N - 2, sumE)


print("1 = ", fun8_2(1))
print("2 = ", fun8_2(2))
print("3 = ", fun8_2(3))
print("4 = ", fun8_2(4))
print("5 = ", fun8_2(5))
print("6 = ", fun8_2(6))
print("7 = ", fun8_2(7))
print("8 = ", fun8_2(8))
print("9 = ", fun8_2(9))

