
"""
How to convert an number from decimal to binary using recursion.

Step 1. Recursive case. 

1. Divide the number by 2.
2. Get the integer quotient from the next iteration.
3. Get the remainder for the binary digit.
4. Repeat until the quotient is 0.


    ___________________________________________________
    | Division by   |     Quotient   |       Remainder |
    |__________________________________________________|
    | 13/2          |       6        |         1       |
    |__________________________________________________|  101 * 10 + 0 = 1010
    | 6/2           |       3        |         0       |
    |__________________________________________________|  10 * 10 + 1 = 101
    | 3/2           |       1        |         1       |
    |__________________________________________________|  1 * 10 + 0 = 10
    | 1/2           |       0        |         1       |
    |_______________|________________|_________________|  


 Step 2: Base condition
  If N is 0



"""

def decToBinary(n):
    assert int(n) == n, "The number must be an integer"
    if n == 0: 
        return 0
    else: 
        return n%2 + 10 * decToBinary(int(n/2))


print(decToBinary(3))