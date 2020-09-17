def fib(n):
    """Compute Nth Fibonacci number, for n >= 2."""

    pred, curr = 0, 1  # Finonacci numbers
    k = 2              # position for curr in the sequence

    while k < n:
        pred, curr = curr, pred + curr # Re-bind pred and curr
        k = k + 1
    return curr

