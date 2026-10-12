"""Random-pivot quicksort with two-way partitioning."""

from random import randrange


def partition(low: int, high: int, elements: list[int]) -> int:
    """Partition low..high into values <= pivot and > pivot; return its index."""
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
    """Sort low..high in place; average O(n log n), worst O(n^2) time.

    Recursion uses O(log n) stack space on average and O(n) in the worst case.
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
