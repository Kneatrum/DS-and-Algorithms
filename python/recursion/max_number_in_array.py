
"""
Using recursion to find the biggest number inside an array.
"""

my_array = [4,5,23,6,76,34,2,55,9,28]

def findMaxNumberInArray(example_array, array_size):
    if array_size == 1:
        return example_array[0]
    else:
        return max(example_array[array_size - 1], findMaxNumberInArray(example_array, array_size - 1))
    


print(findMaxNumberInArray(my_array, len(my_array)))