def hoar_sort(A:list):
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L+M+R:
        A[k] = x
        k += 1


some_list = [5, 80, 2, 12, 5, 32, 9, 1, 0, 4, 8, 12]
hoar_sort(some_list)
print(some_list)
