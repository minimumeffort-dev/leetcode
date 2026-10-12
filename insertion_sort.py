"""Insertion sort by growing a sorted prefix."""


def insertion_sort(elements: list[int]) -> list[int]:
    """Sort stably in place; O(n^2) worst-case time and O(1) extra space.

    Inserting position i may shift all i earlier values. In the worst case,
    1 + 2 + ... + (n - 1) shifts give O(n^2) work. Sorted input needs only
    one failed comparison per insertion, giving O(n) best-case time.
    The saved value and indices use O(1) space; the input list is reused.
    """
    for index in range(1, len(elements)):
        value = elements[index]
        previous_index = index - 1

        # Shift larger values to make a gap; equal values keep their order.
        while previous_index >= 0 and elements[previous_index] > value:
            elements[previous_index + 1] = elements[previous_index]
            previous_index -= 1

        elements[previous_index + 1] = value

    return elements


if __name__ == "__main__":
    array = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    print(insertion_sort(array))
