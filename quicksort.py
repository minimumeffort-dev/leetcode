from random import randrange


def partition(low: int, high: int, elements: list[int]):
    pivot_index = randrange(low, high + 1)
    elements[low], elements[pivot_index] = elements[pivot_index], elements[low]

    pivot = elements[low]
    i = low
    j = high

    while i < j:
        while i < high and elements[i] <= pivot:
            i += 1

        while j > low and elements[j] > pivot:
            j -= 1

        if i < j:
            elements[i], elements[j] = elements[j], elements[i]

    elements[low], elements[j] = elements[j], elements[low]

    return j


def quicksort(low: int, high: int, elements: list[int]):
    if low < high:
        j = partition(low, high, elements)
        quicksort(low, j - 1, elements)
        quicksort(j + 1, high, elements)


if __name__ == "__main__":
    elements = [10, 7, 8, 9, 1, 5]
    quicksort(0, len(elements) - 1, elements)
    print(elements)
