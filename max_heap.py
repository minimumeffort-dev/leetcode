"""A max heap backed by a zero-indexed list."""


class MaxHeap:
    """Keep each parent >= its children in a complete binary tree.

    With n entries the tree height is O(log n), and sifting follows one
    parent/child path with constant work per level. Insert/delete therefore
    take O(log n) amortized time, including Python's amortized O(1) list
    append/pop operations. The backing list holds n values, using O(n) space.
    """

    def __init__(self) -> None:
        self.data: list[int] = []
        self.size = 0

    def heapify_up(self, index: int) -> None:
        """Move a newly inserted node up while its parent is smaller.

        The parent index halves at each step, allowing at most O(log n)
        swaps. Only the current and parent indices add O(1) extra space.
        """
        while index > 0:
            # Subtract one before halving because the root occupies index zero.
            parent = (index - 1) // 2

            if self.data[index] <= self.data[parent]:
                break

            self.data[index], self.data[parent] = (
                self.data[parent],
                self.data[index],
            )
            index = parent

    def heapify_down(self) -> None:
        """Move the root down until every parent is at least its children.

        Compare at most two children per level along one path of height
        O(log n). Time is O(log n), and the handful of indices uses O(1) space.
        """
        index = 0
        while index < self.size:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            largest = index

            if left_child < self.size and self.data[left_child] > self.data[largest]:
                largest = left_child

            if right_child < self.size and self.data[right_child] > self.data[largest]:
                largest = right_child

            # Both child subtrees are heaps; swapping with the larger child is safe.
            if largest == index:
                break

            self.data[index], self.data[largest] = (
                self.data[largest],
                self.data[index],
            )
            index = largest

    def insert(self, value: int) -> None:
        """Append a value at the next leaf position, then restore heap order."""
        self.data.append(value)
        self.size += 1
        self.heapify_up(self.size - 1)

    def delete(self) -> int:
        """Remove and return the maximum; raise IndexError if the heap is empty."""
        if self.size == 0:
            raise IndexError("Cannot delete from an empty heap")

        # Replace the root with the last leaf to preserve the complete tree shape.
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
