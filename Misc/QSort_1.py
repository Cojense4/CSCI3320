def QS(NList):
    def MO3(Ls):
        F = Ls[0]
        M = Ls[len(Ls) // 2]
        L = Ls[-1]

        if F < M < L:
            return M
        elif L < M < F:
            return M
        elif F < L < M:
            return L
        elif M < L < F:
            return L
        elif M < F < L:
            return F
        else:
            return F

    def IS(Ls=NList):
        if len(Ls) <= 1:
            return Ls
        for i in range(1, len(Ls)):
            nextVal = Ls[i]
            j = i - 1
            while j >= 0 and nextVal < Ls[j]:
                Ls[j+1] = Ls[j]
                j -= 1
            Ls[j+1] = nextVal
        return Ls

    if len(NList) <= 4:
        return IS(NList)

    pivot = MO3(Ls=NList)

    L, R = 0, len(NList)-1
    while NList[L] < pivot:
        L += 1
    while NList[R] < pivot:
        R -= 1
    NList[L], NList[R] = NList[R], NList[L]
    return QS(NList)


nList = [12, 4, 3, 9, 18, 7, 2, 17, 13, 1, 5, 6]
print(nList)
ans = QS(nList)
print(ans)
