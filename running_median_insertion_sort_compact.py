"""Running medians using insertion sort and a compact median expression."""

from collections.abc import Iterable


def running_median(elements: Iterable[int | float]) -> None:
    """Print each running median; O(n^2) total worst-case time, O(n) space.

    Inserting the kth value may shift k - 1 earlier values. Over n inputs,
    0 + 1 + ... + (n - 1) shifts give O(n^2) worst-case work. Reading one
    or two middle positions costs O(1) per median. The sorted prefix grows
    to n stored values, using O(n) space.
    """
    sorted_numbers: list[int | float] = []

    for value in elements:
        sorted_numbers.append(value)
        previous_index = len(sorted_numbers) - 2

        # Insert the new value into the sorted prefix before reading its middle.
        while previous_index >= 0 and sorted_numbers[previous_index] > value:
            sorted_numbers[previous_index + 1] = sorted_numbers[previous_index]
            previous_index -= 1
        sorted_numbers[previous_index + 1] = value

        middle = len(sorted_numbers) // 2

        # An even prefix has two middle values instead of one.
        print(
            sorted_numbers[middle]
            if len(sorted_numbers) % 2 == 1
            else (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
        )


if __name__ == "__main__":
    array = [2, 1, 5, 7, 2, 0, 5]
    running_median(array)
