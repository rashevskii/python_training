def left_boundary(A: list, key: int):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_boundary(A: list, key: int):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right


def binary_search(A: list, key: int):
    left = left_boundary(A, key)
    right = right_boundary(A, key)
    left_index = A.index(left)
    right_index = A.index(right)
    if (right_index - left_index) > 1:
        return True
    else:
        return False


some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(some_list, 8))
