"""Running medians using insertion sort, with the median cases written out."""

from collections.abc import Iterable


def running_median(numbers: Iterable[int | float]) -> None:
    """Print each running median; O(n^2) total worst-case time, O(n) space."""
    sorted_numbers: list[int | float] = []

    for value in numbers:
        sorted_numbers.append(value)
        previous_index = len(sorted_numbers) - 2

        # Insert the new number into the already sorted prefix.
        while previous_index >= 0 and sorted_numbers[previous_index] > value:
            sorted_numbers[previous_index + 1] = sorted_numbers[previous_index]
            previous_index -= 1

        sorted_numbers[previous_index + 1] = value

        count = len(sorted_numbers)
        middle = count // 2

        if count % 2 == 1:
            median = sorted_numbers[middle]
        else:
            # middle is the right of the two central positions.
            median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

        print(median)


if __name__ == "__main__":
    running_median([2, 1, 5, 7, 2, 0, 5])
