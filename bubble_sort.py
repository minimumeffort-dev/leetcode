"""Bubble sort with an early stop when a pass makes no swaps."""


def bubble_sort(elements: list[int]) -> list[int]:
    """Sort stably in place; O(n^2) worst-case time and O(1) extra space."""
    swapped = True

    # A pass without swaps proves that every neighboring pair is in order.
    while swapped:
        swapped = False
        for index in range(len(elements) - 1):
            if elements[index] > elements[index + 1]:
                swapped = True
                elements[index], elements[index + 1] = (
                    elements[index + 1],
                    elements[index],
                )

    return elements


if __name__ == "__main__":
    elements = [10, 9, 10, 7, 6, 5, 4, 3, 2, 1]
    print(bubble_sort(elements))
