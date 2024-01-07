
"""
Implementation of the factorial function using recursion
"""


def factorial(n):
    assert int(n) == n, 'Number must be an integer'
    # Base condition. 
    # Prevents infinite recursion
    if n <= 1:
        return 1
    # The recursion
    else:
        return n * factorial(n - 1)
    
# Print the result.
print(factorial(13))