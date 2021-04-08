cache = {}

def fib(n):
    if n in cache:
        return cache[n]
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    val = (fib(n - 1) + fib(n - 2))
    cache[n] = val
    return val

