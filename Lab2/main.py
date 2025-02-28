import time
import random
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


from quickSort import quicksort
from mergeSort import merge_sort
from heapSort import heap_sort
from insertionSort import insertion_sort


def run_test_cases():
    # Task 2: Test cases from your earlier analysis (properties of input data)
    test_cases = [
        ("Nearly sorted with two random numbers at the end", [1, 2, 3, 4, 5, 42, 7]),
        ("Half sorted (first half ascending, second half descending)", [1, 2, 3, 4, 5, 9, 8, 7]),
        ("Descending list", [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
        ("List with duplicates and negatives", [3, -1, 2, -1, 3, 2, 0, 0, 5]),
        ("All identical elements", [7, 7, 7, 7, 7, 7]),
        ("Already sorted list", [1, 2, 3, 4, 5, 6, 7, 8]),
        ("Mixed large and small numbers", [99999, -100000, 250, 1, -999, 50000, 3, 42]),
        ("List with repeated numbers", [2, 2, 2, 3, 3, 1, 1, 1]),
    ]

    # Map algorithm names to a tuple: (function, in_place)
    algorithms = {
        "QuickSort": (quicksort, False),
        "MergeSort": (merge_sort, False),
        "HeapSort": (heap_sort, True),
        "InsertionSort": (insertion_sort, True)
    }

    print("==== Basic Test Cases ====")
    for description, data in test_cases:
        print(f"Test case: {description}")
        print("Original:", data)
        for algo_name, (algo_func, in_place) in algorithms.items():
            data_copy = data.copy()  # preserve original test case
            if in_place:
                algo_func(data_copy)
                sorted_result = data_copy
            else:
                sorted_result = algo_func(data_copy)
            print(f"  {algo_name}: {sorted_result}")
        print()


def empirical_analysis():
    # Task 3 & 4: Choose metric (execution time) and perform empirical analysis
    input_sizes = [100, 500, 1000, 5000, 10000]
    # For each algorithm, we store a list of average times corresponding to each input size.
    times = {
        "QuickSort": [],
        "MergeSort": [],
        "HeapSort": [],
        "InsertionSort": []
    }

    algorithms = {
        "QuickSort": (quicksort, False),
        "MergeSort": (merge_sort, False),
        "HeapSort": (heap_sort, True),
        "InsertionSort": (insertion_sort, True)
    }

    runs_per_size = 5  # run each algorithm several times for averaging

    for size in input_sizes:
        print(f"Running empirical tests for input size: {size}")
        # Generate a random list of given size
        base_list = [random.randint(1, size) for _ in range(size)]

        # For each algorithm, average the run time over several runs.
        for algo_name, (algo_func, in_place) in algorithms.items():
            total_time = 0.0
            for _ in range(runs_per_size):
                test_list = base_list.copy()
                start_time = time.perf_counter()
                if in_place:
                    algo_func(test_list)
                else:
                    _ = algo_func(test_list)
                end_time = time.perf_counter()
                total_time += (end_time - start_time)
            avg_time = total_time / runs_per_size
            times[algo_name].append(avg_time)
            print(f"  {algo_name}: avg time = {avg_time:.6f} sec")
        print()

    # Task 5: Make a graphical presentation of the data
    plt.figure(figsize=(10, 6))
    for algo_name, time_list in times.items():
        plt.plot(input_sizes, time_list, marker='o', label=algo_name)
    plt.xlabel("Input Size (number of elements)")
    plt.ylabel("Average Execution Time (seconds)")
    plt.title("Empirical Analysis of Sorting Algorithms")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return times


def conclusions(times):
    # Task 6: Conclusion on the work done.
    print("==== Conclusions ====")
    print("Based on the empirical analysis, we can observe:")
    for algo_name, time_list in times.items():
        print(f" - {algo_name} execution times over different input sizes: {time_list}")

    print("\nObservations:")
    print("1. Algorithms like QuickSort and MergeSort generally perform well with larger datasets,")
    print("   as their average-case time complexities are O(n log n).")
    print("2. InsertionSort, with its O(n^2) worst-case time complexity, becomes significantly slower")
    print("   as the input size increases.")
    print("3. HeapSort shows consistent performance with O(n log n) complexity, but constant factors may vary.")
    print("\nFinal Conclusion: The choice of sorting algorithm depends on the specific properties of the input data")
    print("and the performance metric of interest (e.g., execution time). For larger inputs, algorithms with")
    print("O(n log n) complexity (like QuickSort, MergeSort, and HeapSort) are preferable over InsertionSort.")


def main():
    run_test_cases()  # Task 1 & 2: Basic testing with defined input cases
    times = empirical_analysis()  # Tasks 3 & 4: Measure execution times
    conclusions(times)  # Task 6: Print conclusions


if __name__ == "__main__":
    main()
