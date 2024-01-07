"""
Finding the greatest common divisor of two numbers using recursion
"""

def gcd(a, b):
    assert int(a) == a and int(b) == b, "The two numbers must be integers"
    
    # If the two numbers are negative, convert them to positive numbers
    if a < 0: a *= -1
    if b < 0: b *= -1

    if b == 0:
        return a  # According to euclidean algorithm.
    else:
        return gcd(b, a % b)
    
print(gcd(48, -18))