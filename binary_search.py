"""Binary search over an ascending list."""


def binary_search(arr: list[int], target: int) -> int:
    """Return a matching index for target, or -1 if target is absent.

    arr must be sorted in ascending order. If duplicates are present,
    any matching index may be returned.
    Each comparison discards about half the remaining range, so after
    O(log n) comparisons at most one position remains. Only left/right/middle
    indices are stored, giving O(1) extra space without copying sublists.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        # Discard the half that cannot contain the target, including middle.
        if arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    print(binary_search(arr, target))
