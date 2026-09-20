import random
import time
import tracemalloc
import sys

# Increase Python's recursion limit.
# This is necessary because Quick Sort can create very deep recursion
# when the last element is chosen as the pivot for sorted or reverse-sorted data.
sys.setrecursionlimit(30000)


# ------------------------------------------------------------
# MERGE SORT
# ------------------------------------------------------------

def merge_sort(arr):
    """
    Sorts a list using the Merge Sort divide-and-conquer algorithm.

    Steps:
    1. Divide the list into two halves.
    2. Recursively sort each half.
    3. Merge the two sorted halves.
    """

    # Base case:
    # A list with 0 or 1 element is already sorted.
    if len(arr) <= 1:
        return arr

    # Find the midpoint of the list.
    mid = len(arr) // 2

    # Recursively sort the left half.
    left = merge_sort(arr[:mid])

    # Recursively sort the right half.
    right = merge_sort(arr[mid:])

    # Merge the two sorted halves.
    return merge(left, right)


def merge(left, right):
    """
    Merges two already-sorted lists into one sorted list.
    """

    result = []

    # i tracks the current position in the left list.
    i = 0

    # j tracks the current position in the right list.
    j = 0

    # Compare elements from both lists and add the smaller one
    # to the result list.
    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from the left list.
    result.extend(left[i:])

    # Add any remaining elements from the right list.
    result.extend(right[j:])

    return result


# ------------------------------------------------------------
# QUICK SORT
# ------------------------------------------------------------

def quick_sort(arr):
    """
    Sorts a list using the Quick Sort divide-and-conquer algorithm.

    This implementation uses the LAST element as the pivot.

    Steps:
    1. Choose a pivot.
    2. Partition values into smaller, equal, and larger groups.
    3. Recursively sort the smaller and larger groups.
    """

    # Base case:
    # A list with 0 or 1 element is already sorted.
    if len(arr) <= 1:
        return arr

    # Choose the last element as the pivot.
    # This is simple, but it can cause worst-case performance
    # for sorted or reverse-sorted input.
    pivot = arr[-1]

    # Store values smaller than the pivot.
    left = []

    # Store values equal to the pivot.
    equal = []

    # Store values greater than the pivot.
    right = []

    # Partition the list around the pivot.
    for value in arr:

        if value < pivot:
            left.append(value)

        elif value == pivot:
            equal.append(value)

        else:
            right.append(value)

    # Recursively sort the left and right partitions,
    # then combine them with the pivot values.
    return quick_sort(left) + equal + quick_sort(right)


# ------------------------------------------------------------
# PERFORMANCE TESTING FUNCTION
# ------------------------------------------------------------

def test_algorithm(name, algorithm, data):
    """
    Measures the execution time and peak memory usage
    of a sorting algorithm.
    """

    # Start tracking memory usage.
    tracemalloc.start()

    # Record the starting time.
    start_time = time.perf_counter()

    # Sort a copy of the data so that the original dataset
    # is not modified.
    result = algorithm(data.copy())

    # Record the ending time.
    end_time = time.perf_counter()

    # Get current and peak memory usage.
    current, peak = tracemalloc.get_traced_memory()

    # Stop tracking memory.
    tracemalloc.stop()

    # Calculate total execution time.
    execution_time = end_time - start_time

    # Convert peak memory usage from bytes to kilobytes.
    memory_kb = peak / 1024

    # Display the performance results.
    print(
        f"{name:<12} "
        f"Time: {execution_time:.6f} seconds | "
        f"Peak Memory: {memory_kb:.2f} KB"
    )

    return result


# ------------------------------------------------------------
# DATASET CREATION AND TESTING
# ------------------------------------------------------------

# Test the algorithms using three different dataset sizes.
sizes = [1000, 5000, 10000]

for size in sizes:

    print("\n" + "=" * 60)
    print(f"DATASET SIZE: {size}")
    print("=" * 60)

    # Create three different types of input data.
    datasets = {

        # Already sorted data.
        "Sorted": list(range(size)),

        # Reverse-sorted data.
        "Reverse": list(range(size, 0, -1)),

        # Random data with unique values.
        "Random": random.sample(range(size * 2), size)
    }

    # Run both sorting algorithms on each dataset type.
    for dataset_name, data in datasets.items():

        print(f"\n{dataset_name} Dataset")

        # Test Merge Sort.
        test_algorithm(
            "Merge Sort",
            merge_sort,
            data
        )

        # Test Quick Sort.
        test_algorithm(
            "Quick Sort",
            quick_sort,
            data
        )