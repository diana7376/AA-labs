import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import time

def fibonacci_fast_doubling(n): # fast doubling method to compute the nth Fibonacci number

    if n == 0:
        return (0, 1)
    else:
        a, b = fibonacci_fast_doubling(n // 2)
        c = a * (2 * b - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

def fibonacci_fast_doubling_sequence(n): # generate the Fibonacci sequence up to the nth term
    sequence = []
    for i in range(n + 1):
        sequence.append(fibonacci_fast_doubling(i)[0])
    return sequence


n_plot = 20
fib_sequence = fibonacci_fast_doubling_sequence(n_plot)

n_values = list(range(10, 510, 50))
times = []
for n_val in n_values:
    start = time.perf_counter()
    fibonacci_fast_doubling(n_val)
    end = time.perf_counter()
    times.append(end - start)

fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# Subplot 1: Fibonacci Sequence computed using Fast Doubling Method
axs[0].plot(range(n_plot + 1), fib_sequence, marker='o', linestyle='-', color='blue')
axs[0].set_title("Fibonacci Sequence (Fast Doubling Method)")
axs[0].set_xlabel("Index (n)")
axs[0].set_ylabel("Fibonacci Number")
axs[0].grid(True)

# Subplot 2: Execution Time vs. n  .. How efficiently the fast doubling method computes them for different n values
# The time complexity of the fast doubling method is O(n)
axs[1].plot(n_values, times, marker='s', linestyle='-', color='red')
axs[1].set_title("Execution Time vs. n (Fast Doubling Method)")
axs[1].set_xlabel("n (Number of Terms)")
axs[1].set_ylabel("Time (seconds)")
axs[1].grid(True)

plt.tight_layout()
plt.show()
# The fast doubling method has linear time complexity, which is significantly faster than the tail-recursive and iterative loop methods.