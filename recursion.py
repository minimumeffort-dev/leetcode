def fact(n: int) -> int:
    if n == 0:
        return 1
    return n * fact(n - 1)


def fib(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(fact(3))
    print(fib(3))
