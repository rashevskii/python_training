def gen_bin(M:int, prefix=""):
    if M == 0:
        print(prefix)
        return
    for digit in "0", "1":
        gen_bin(M-1, prefix+digit)


def generate_numbers(N:int, M:int, prefix=None):
    """
    Генерирует все числа (с лидирующими незначащами нулями) в N-ричной системе счисления (N <= 10) длины M
    :param N:система счисления
    :param M:длина
    :param prefix:
    :return:array
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()


# gen_bin(5)
# generate_numbers(4, 3)
