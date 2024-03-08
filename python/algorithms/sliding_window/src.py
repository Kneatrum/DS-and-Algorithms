
# Return the highest sum from a window of size 5

data_list = [2,5,33,9,20,63,49,6,13,27,99,71,1,37,22]
window_size = 5

def sliding_window(data, n):
    if len(data) < window_size:
        return 0
    max_total = sum(data[:n])
    total = 0
    for i in range(len(data) - n):
        total -= data[i] # Remove the first element from the window
        total += data[i + n] # Add the next element to the window
        max_total = max(max_total,total) # Assign the maximum total to the max total value 
    return max_total

print(sliding_window(data_list, window_size))

# Find the best time to buy and sell stock for maximum profit in the price list below.

prices = [2,5,33,9,20,63,49,6,13,27,99,71,1,37,22]
 
def two_pointers(data):
    left, right = 0, 1
    max_profit = 0

    while right < len(data):
        if data[right] > data[left]:
            profit = data[right] - data[left]
            max_profit = max(max_profit, profit)
        else:
            left = right
        right += 1
    return max_profit

print(two_pointers(prices))