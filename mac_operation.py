#mac_operation.py

def mac_operation(pattern, filter):
    size = len(pattern)
    total = 0.0

    for i in range(size):
        for j in range(size):
            total += pattern[i][j] * filter[i][j]

    return total

#O(N^2)

def measure_average_time(pattern, filter, repeat=10):
    total_time = 0.0

    for i in range(repeat):
        start = time.perf_counter()
        mac_operation(pattern, filter)
        end = time.perf_counter()
        total_time += end - start
    return (total_time / repeat) * 1000 # ms 단위