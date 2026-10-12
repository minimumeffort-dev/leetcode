"""Stable merge sort using inclusive index ranges."""


def merge(low: int, mid: int, high: int, elements: list[int]) -> list[int]:
    """Merge sorted ranges low..mid and mid+1..high back into elements."""
    merged: list[int] = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        # Choosing the left half on ties keeps equal values in their input order.
        if elements[left] <= elements[right]:
            merged.append(elements[left])
            left += 1
        else:
            merged.append(elements[right])
            right += 1

    while left <= mid:
        merged.append(elements[left])
        left += 1
    while right <= high:
        merged.append(elements[right])
        right += 1

    # Write back into the original list so the parent merge sees sorted halves.
    for index, value in enumerate(merged, start=low):
        elements[index] = value

    return elements


def merge_sort(low: int, high: int, elements: list[int]) -> list[int]:
    """Sort low..high in place; O(n log n) time and O(n) extra space."""
    if low < high:
        mid = (low + high) // 2
        merge_sort(low, mid, elements)
        merge_sort(mid + 1, high, elements)
        merge(low, mid, high, elements)

    return elements


if __name__ == "__main__":
    array = [12, 11, 13, 5, 6]
    print(merge_sort(0, len(array) - 1, array))
