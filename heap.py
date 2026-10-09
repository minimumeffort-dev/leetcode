class MaxHeap:
    def __init__(self) -> None:
        self.data: list[int] = []
        self.size = 0

    def heapify_up(self, index: int) -> None:
        while index > 0:
            parent = (index - 1) // 2

            if self.data[index] <= self.data[parent]:
                break

            self.data[index], self.data[parent] = (
                self.data[parent],
                self.data[index],
            )
            index = parent

    def heapify_down(self) -> None:
        """Move the root down until every parent is at least its children."""
        index = 0
        while index < self.size:
            child_left = 2 * index + 1
            child_right = 2 * index + 2
            largest = index

            if child_left < self.size and self.data[child_left] > self.data[largest]:
                largest = child_left

            if child_right < self.size and self.data[child_right] > self.data[largest]:
                largest = child_right

            # this means we haven't found a larger child, so we can stop
            if largest == index:
                break

            self.data[index], self.data[largest] = (
                self.data[largest],
                self.data[index],
            )
            index = largest

    def insert(self, value: int) -> None:
        self.data.append(value)
        self.size += 1
        self.heapify_up(self.size - 1)

    def delete(self) -> int:
        """Remove and return the maximum; raise IndexError if the heap is empty."""
        if self.size == 0:
            raise IndexError("Cannot delete from an empty heap")

        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        maximum = self.data.pop()
        self.size -= 1
        self.heapify_down()
        return maximum


if __name__ == "__main__":
    heap = MaxHeap()
    heap.insert(1)
    heap.insert(2)
    heap.insert(3)
    print(heap.data)

    heap.insert(4)
    print(heap.data)

    heap.delete()
    print(heap.data)
