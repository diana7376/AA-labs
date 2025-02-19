import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import time
import sys


sys.setrecursionlimit(10000) # increase the recursion limit to avoid RecursionError

def fibonacci_tail_recursive(n, a=0, b=1): # tail recursive function to compute the nth Fibonacci number

    if n == 0:
        return a
    elif n == 1:
        return b
    return fibonacci_tail_recursive(n-1, b, a+b)

def fibonacci_tail_recursive_sequence(n): # generate the Fibonacci sequence up to the nth term

    seq = []
    for i in range(n+1):
        seq.append(fibonacci_tail_recursive(i))
    return seq


n_plot = 20
fib_sequence = fibonacci_tail_recursive_sequence(n_plot)

n_values = list(range(10, 510, 50))  # measure the execution time to illustrate the time complexity
times = []

for n_val in n_values:
    start = time.perf_counter()
    fibonacci_tail_recursive(n_val)
    end = time.perf_counter()
    times.append(end - start)

fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# Subplot 1: Fibonacci Sequence (how Fibonacci numbers themselves grow)
# The Fibonacci sequence grows exponentially
axs[0].plot(range(n_plot + 1), fib_sequence, marker='o', linestyle='-', color='blue')
axs[0].set_title("Fibonacci Sequence (Tail-Recursive Method)")
axs[0].set_xlabel("Index (n)")
axs[0].set_ylabel("Fibonacci Number")
axs[0].grid(True)

# Subplot 2: Execution Time vs. n (illustrating exponential time complexity) .. How efficiently the tail-recursive method computes them for different n values
# The time complexity of the tail-recursive method is O(2^n)
axs[1].plot(n_values, times, marker='s', linestyle='-', color='red')
axs[1].set_title("Execution Time vs. n (Tail-Recursive Method)")
axs[1].set_xlabel("n (Number of Terms)")
axs[1].set_ylabel("Time (seconds)")
axs[1].grid(True)

plt.tight_layout()
plt.show()

# The tail-recursive method has exponential time complexity, similar to the iterative loop method.