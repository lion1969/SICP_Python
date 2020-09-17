def fib(n):
    """Compute Nth Fibonacci number, for n >= 2."""

    pred, curr = 0, 1  # Finonacci numbers
    k = 2              # position for curr in the sequence

    while k < n:
        print("b4 asign.    pred = ", pred, "; curr = ", curr)
        pred, curr = curr, pred + curr # Re-bind pred and curr
        print("after asign. pred = ", pred, "; curr = ", curr)
        k = k + 1
        print("[||]")
    return curr

print(fib(11))