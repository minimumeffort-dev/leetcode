def running_median(numbers):
    """Print each running median; O(n^2) total worst-case time, O(n) space."""
    sorted_numbers = []

    for anchor in numbers:
        sorted_numbers.append(anchor)
        j = len(sorted_numbers) - 2

        # Insert the new number into the already sorted prefix.
        while j >= 0 and sorted_numbers[j] > anchor:
            sorted_numbers[j + 1] = sorted_numbers[j]
            j -= 1

        sorted_numbers[j + 1] = anchor

        count = len(sorted_numbers)
        middle = count // 2

        if count % 2 == 1:
            median = sorted_numbers[middle]
        else:
            median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

        print(median)


if __name__ == "__main__":
    running_median([2, 1, 5, 7, 2, 0, 5])
