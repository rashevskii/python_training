def check_sorted(A: list, ascending: bool = True):
    flag = True
    s = 2 * int(ascending) - 1
    for x in range(0, len(A) - 1):
        if s * A[x] > s * A[x+1]:
            flag = False
            break
    return flag


print(check_sorted([1, 2, 3, 4, 5]))
