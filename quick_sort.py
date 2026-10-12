"""Random-pivot quicksort with two-way partitioning."""

from random import randrange


def partition(low: int, high: int, elements: list[int]) -> int:
    """Partition low..high into values <= pivot and > pivot; return its index.

    For k values, each pointer crosses the range at most once, giving O(k)
    comparisons/swaps overall. The pivot and indices use O(1) extra space.
    """
    pivot_index = randrange(low, high + 1)
    # The scan expects the pivot at low, regardless of where it was chosen.
    elements[low], elements[pivot_index] = elements[pivot_index], elements[low]

    pivot = elements[low]
    left = low
    right = high

    while left < right:
        # Bound each scan even when every value belongs on the same side.
        while left < high and elements[left] <= pivot:
            left += 1

        while right > low and elements[right] > pivot:
            right -= 1

        if left < right:
            elements[left], elements[right] = elements[right], elements[left]

    elements[low], elements[right] = elements[right], elements[low]

    return right


def quicksort(low: int, high: int, elements: list[int]) -> None:
    """Sort low..high in place; O(n log n) balanced work, O(n^2) worst case.

    Each partition scans its range once. Balanced partitions give O(log n)
    levels with O(n) total work per level. With distinct values, random
    pivots give O(n log n) expected time.
    One-sided partitions scan n, n - 1, ... values, giving O(n^2) worst-case
    time; equal values cause that pattern in this two-way version.
    Expected depth is O(log n) for distinct values and O(n) in the worst case.
    Each call stores only a few indices, so stack space follows that depth.
    """
    if low < high:
        pivot_index = partition(low, high, elements)
        # The pivot is already in its final position, so exclude it from recursion.
        quicksort(low, pivot_index - 1, elements)
        quicksort(pivot_index + 1, high, elements)


if __name__ == "__main__":
    elements = [10, 7, 8, 9, 1, 5]
    quicksort(0, len(elements) - 1, elements)
    print(elements)
