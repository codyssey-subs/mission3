#mac_operation.py

def mac_operation(pattern, filter):
    size = len(pattern)
    total = 0.0

    for i in range(size):
        for j in range(size):
            total += pattern[i][j] * filter[i][j]

    return total

#O(N^2)