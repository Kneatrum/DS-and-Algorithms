

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

nums = [33, 4, 2, 5, 8, 11, 15]

our_target =  9

def get_two_sum(numbers, target):
    hash_map = {}
    for i, number in enumerate(numbers):
        difference = target - number
        if difference in hash_map:
            return [hash_map[difference], i]
        else:
            hash_map[number] = i

print(get_two_sum(nums, our_target))