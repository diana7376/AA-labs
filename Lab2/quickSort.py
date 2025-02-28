import random
def quicksort(arr):

    if len(arr) <= 1: #array with 0 or 1 element is already sorted
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    unsorted_list = [random.randint(1, 1000) for _ in range(20)]
    sorted_list = quicksort(unsorted_list)
    print("Sorted list:", sorted_list)
