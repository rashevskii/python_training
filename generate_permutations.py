def find(number, A):
    """
    поиск number в A и возврат True, если такой есть
    :param number:int
    :param A:list
    :return:boolean
    """
    for x in A:
        return True if number == x else False


def generate_permutations(N:int, M:int=-1, prefix=None):
    """
    Генерация всех перестановок N чисел в M позициях, с префиксом prefix
    :param N:int
    :param M:int
    :param prefix:list
    :return:None
    """
    M = N if M == -1 else M
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()


generate_permutations(3)