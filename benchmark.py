import random
import time
import tracemalloc
import sys
sys.setrecursionlimit(30000)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    equal = []
    right = []

    for value in arr:
        if value < pivot:
            left.append(value)
        elif value == pivot:
            equal.append(value)
        else:
            right.append(value)

    return quick_sort(left) + equal + quick_sort(right)


def test_algorithm(name, algorithm, data):
    tracemalloc.start()

    start_time = time.perf_counter()

    result = algorithm(data.copy())

    end_time = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    execution_time = end_time - start_time
    memory_kb = peak / 1024

    print(
        f"{name:<12} "
        f"Time: {execution_time:.6f} seconds | "
        f"Peak Memory: {memory_kb:.2f} KB"
    )

    return result


sizes = [1000, 5000, 10000]

for size in sizes:

    print("\n" + "=" * 60)
    print(f"DATASET SIZE: {size}")
    print("=" * 60)

    datasets = {
        "Sorted": list(range(size)),
        "Reverse": list(range(size, 0, -1)),
        "Random": random.sample(range(size * 2), size)
    }

    for dataset_name, data in datasets.items():

        print(f"\n{dataset_name} Dataset")

        test_algorithm(
            "Merge Sort",
            merge_sort,
            data
        )

        test_algorithm(
            "Quick Sort",
            quick_sort,
            data
        )