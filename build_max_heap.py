"""Build a max heap from an existing list, working from the bottom up."""


def heapify(arr: list[int]) -> None:
    """Rearrange arr in place in O(n) time and O(1) extra space."""
    size = len(arr)
    # Leaves are already heaps; each parent's child subtrees are ready before it.
    for parent_index in range(size // 2 - 1, -1, -1):
        index = parent_index
        while index < size:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            largest = index

            if left_child < size and arr[left_child] > arr[largest]:
                largest = left_child
            if right_child < size and arr[right_child] > arr[largest]:
                largest = right_child

            if largest == index:
                break

            arr[index], arr[largest] = arr[largest], arr[index]

            index = largest


if __name__ == "__main__":
    arr = [4, 2, 3, 1, 5]
    heapify(arr)
    print(arr)
