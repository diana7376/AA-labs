import random
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    unsorted_list = [random.randint(1, 1000) for _ in range(20)]
    insertion_sort(unsorted_list)
    print("Sorted list:", unsorted_list)
