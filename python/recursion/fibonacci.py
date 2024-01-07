
"""
Creating a fibonacci function using recursion.
"""

def fibonacci(n):
    assert n >= 0 and int(n) == n, "n must be a positive integer"
    # Base condition.
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n - 2)
    

print(fibonacci(8))