def fib_economy(number: int):
    fib = [0, 1] + [0] * (number-1)
    for i in range(2, number+1):
        fib[i] = fib[i - 1] + fib[i - 2]
    print(fib)
    return fib[number]


print(fib_economy(60))
