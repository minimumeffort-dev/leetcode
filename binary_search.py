def binary_search(arr: list[int], target: int) -> int:
    """Return a matching index for target, or -1 if target is absent.

    arr must be sorted in ascending order. If duplicates are present,
    any matching index may be returned.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    print(binary_search(arr, target))
