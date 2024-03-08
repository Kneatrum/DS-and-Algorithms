
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