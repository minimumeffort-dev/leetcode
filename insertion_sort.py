def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1

        while j >= 0 and elements[j] > anchor:
            elements[j + 1] = elements[j]
            j -= 1

        elements[j + 1] = anchor

    return elements


if __name__ == "__main__":
    array = [12, 11, 13, 5, 6]
    array = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    print(insertion_sort(array))
