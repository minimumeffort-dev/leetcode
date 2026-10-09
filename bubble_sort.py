def bubble_sort(elements: list[int]) -> list[int]:
    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(elements) - 1):
            if elements[i] > elements[i + 1]:
                swapped = True
                elements[i], elements[i + 1] = elements[i + 1], elements[i]

    return elements


if __name__ == "__main__":
    elements = [10, 9, 10, 7, 6, 5, 4, 3, 2, 1]
    print(bubble_sort(elements))
