import random
def heapify(arr, n, i):

    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child index
    right = 2 * i + 2  # right child index

    # If left child exists and is greater than root.
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than the current largest.
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not the root, swap and continue heapifying.
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Perform HeapSort on the array.

    Parameters:
    arr (list): The list of elements to sort.
    """
    n = len(arr)

    # Build a max heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from the heap.
    for i in range(n - 1, 0, -1):
        # Move current root (largest) to the end.
        arr[0], arr[i] = arr[i], arr[0]
        # Call heapify on the reduced heap.
        heapify(arr, i, 0)

if __name__ == "__main__":
    unsorted_list = [random.randint(1, 1000) for _ in range(20)]
    heap_sort(unsorted_list)
    print("Sorted array is:", unsorted_list)
