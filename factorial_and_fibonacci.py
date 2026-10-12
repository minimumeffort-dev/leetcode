"""Direct recursion examples for factorial and Fibonacci numbers."""


def fact(n: int) -> int:
    """Return n! for n >= 0; O(n) recursive steps and O(n) call frames.

    Each call decreases n by one and waits for the next result, so there
    are n multiplications and up to n + 1 active calls. These are operation
    and frame counts: Python's growing factorial integers add arithmetic
    and numeric-storage costs beyond the constant-size-integer model.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    # 0! = 1 supplies the value from which the recursive calls build back up.
    if n == 0:
        return 1
    return n * fact(n - 1)


def fib(n: int) -> int:
    """Return F(n) with F(0) = 0; exponential time and O(n) call frames.

    Each non-base call makes two calls and repeats earlier subproblems.
    A binary call tree of depth n gives an O(2^n) upper bound on calls.
    Only one root-to-leaf path is active at once, so the stack has O(n)
    frames. Large-integer arithmetic/storage adds costs as values grow.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    # This intentionally repeats subproblems to demonstrate direct recursion.
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(fact(3))
    print(fib(3))
