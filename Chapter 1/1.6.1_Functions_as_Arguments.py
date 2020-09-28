def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total


def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total


def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / (k * (k + 2)), k + 4
    return total


"""
These three functions clearly share a common underlying pattern. 
They are for the most part identical, differing only in name, the function of k used to compute the term to be added, 
and the function that provides the next value of k. 
We could generate each of the functions by filling in slots in the same template:
def <name>(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + <term>(k), <next>(k)
    return total
"""


def sum_of_series(n, term, next):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), next(k)
    return total


def identity(k):
    return k


def cube(k):
    return pow(k, 3)


def pi_term(k):
    denominator = k * (k + 2)
    return 8 / denominator


def successor(k):
    return k + 1


def pi_next(k):
    return k + 4


print("sum first N = 100, natural digits = ", sum_naturals(100))
print("sum first N = 100, natural digits = ", sum_of_series(100, identity, successor))
print()

print("sum first N = 100, cubes of natural digits = ", sum_cubes(100))
print("sum first N = 100, cubes of natural digits = ", sum_of_series(100, cube, successor))
print()

print("sum first N = 1000000, sum of terms for Pi series = ", pi_sum(1000000))
print("sum first N = 1000000, sum of terms for Pi series = ", sum_of_series(1000000, pi_term, pi_next))