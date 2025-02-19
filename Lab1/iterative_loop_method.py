import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import time


def fibonacci_iterative(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]

    a, b = 0, 1
    fib_sequence = [a, b]

    for _ in range(2, n + 1):
        a, b = b, a + b
        fib_sequence.append(b)

    return fib_sequence


# generate the first 20 Fibonacci numbers using the iterative loop method
n_plot = 20
fib_sequence = fibonacci_iterative(n_plot)

# measure the execution time for n = 10, 60, 110, ..., 510
n_values = list(range(10, 510, 50))
times = []

for n_val in n_values:
    start = time.perf_counter()
    fibonacci_iterative(n_val)
    end = time.perf_counter() # perf_counter() returns the current time in fractional seconds
    times.append(end - start)

fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# Subplot 1: Fibonacci sequence (how Fibonacci numbers themselves grow)
# The Fibonacci sequence grows exponentially
axs[0].plot(range(n_plot + 1), fib_sequence, marker='o', linestyle='-', color='blue')
axs[0].set_title("Fibonacci Sequence (Iterative Loop Method)")
axs[0].set_xlabel("Index (n)")
axs[0].set_ylabel("Fibonacci Number")
axs[0].grid(True)

# Subplot 2: Execution Time vs. n (illustrating linear time complexity) .. How efficiently the iterative method computes them for different n values
# The time complexity of the iterative loop method is O(n)
axs[1].plot(n_values, times, marker='s', linestyle='-', color='red')
axs[1].set_title("Execution Time vs. n (Iterative Loop Method)")
axs[1].set_xlabel("n (Number of Terms)")
axs[1].set_ylabel("Time (seconds)")
axs[1].grid(True)

plt.tight_layout()
plt.show()
