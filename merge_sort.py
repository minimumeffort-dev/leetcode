def merge(low: int, mid: int, high: int, elements: list[int]) -> list[int]:
    """Merge sorted ranges low..mid and mid+1..high back into elements."""
    c = []
    i = low
    j = mid + 1

    while i <= mid and j <= high:
        if elements[i] <= elements[j]:
            c.append(elements[i])
            i += 1
        else:
            c.append(elements[j])
            j += 1

    while i <= mid:
        c.append(elements[i])
        i += 1
    while j <= high:
        c.append(elements[j])
        j += 1

    for index, value in enumerate(c, start=low):
        elements[index] = value

    return elements


def merge_sort(low: int, high: int, elements: list[int]) -> list[int]:
    """Sort the inclusive range low..high and return the original list."""
    if low < high:
        mid = (low + high) // 2
        merge_sort(low, mid, elements)
        merge_sort(mid + 1, high, elements)
        merge(low, mid, high, elements)

    return elements


if __name__ == "__main__":
    array = [12, 11, 13, 5, 6]
    print(merge_sort(0, len(array) - 1, array))
