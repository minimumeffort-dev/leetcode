"""Recursive binary search over an ascending list."""


def binary_search_recursive(arr: list[int], low: int, high: int, target: int) -> int:
    """Return a matching index within inclusive bounds, or -1 if absent.

    arr must be sorted in ascending order, with valid bounds unless the
    range is empty. To search the whole list, use low=0 and high=len(arr)-1.
    If duplicates are present, any matching index may be returned.

    Each call discards about half the remaining n elements, giving O(log n)
    time for a nonempty range. Calls wait for deeper calls to return, so the
    stack also uses O(log n) space. Passing indices avoids copying sublists.
    An empty range takes O(1) time and space.
    """
    # Check before indexing: crossed bounds mean there is nothing left to search.
    if low > high:
        return -1

    middle = (low + high) // 2
    if arr[middle] == target:
        return middle

    # Exclude middle so the range shrinks even when only one element remains.
    if target < arr[middle]:
        return binary_search_recursive(arr, low, middle - 1, target)
    return binary_search_recursive(arr, middle + 1, high, target)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    print(binary_search_recursive(arr, 0, len(arr) - 1, target))
