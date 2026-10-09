def running_median(elements):
    sorted_numbers = []

    for anchor in elements:
        sorted_numbers.append(anchor)
        j = len(sorted_numbers) - 1 - 1

        while j >= 0 and sorted_numbers[j] > anchor:
            sorted_numbers[j + 1] = sorted_numbers[j]
            j -= 1
        sorted_numbers[j + 1] = anchor

        middle = len(sorted_numbers) // 2

        print(
            sorted_numbers[middle]
            if len(sorted_numbers) % 2 == 1
            else (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
        )


if __name__ == "__main__":
    array = [2, 1, 5, 7, 2, 0, 5]
    running_median(array)
