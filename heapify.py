def heapify(arr):
    size = len(arr)
    # leaves already satisfy the heap property
    for i in range(size // 2 - 1, -1, -1):
        index = i
        while index < size:
            child_left = 2 * index + 1
            child_right = 2 * index + 2
            largest = index

            if child_left < size and arr[child_left] > arr[largest]:
                largest = child_left
            if child_right < size and arr[child_right] > arr[largest]:
                largest = child_right

            if largest == index:
                break

            arr[index], arr[largest] = arr[largest], arr[index]

            index = largest


if __name__ == "__main__":
    arr = [4, 2, 3, 1, 5]
    heapify(arr)
    print(arr)
