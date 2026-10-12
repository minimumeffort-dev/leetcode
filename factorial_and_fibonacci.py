"""Direct recursion examples for factorial and Fibonacci numbers."""


def fact(n: int) -> int:
    """Return n! for n >= 0; O(n) recursive calls and stack space."""
    if n < 0:
        raise ValueError("n must be non-negative")
    # 0! = 1 supplies the value from which the recursive calls build back up.
    if n == 0:
        return 1
    return n * fact(n - 1)


def fib(n: int) -> int:
    """Return F(n) with F(0) = 0; exponential time and O(n) stack space."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    # This intentionally repeats subproblems to demonstrate direct recursion.
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(fact(3))
    print(fib(3))
