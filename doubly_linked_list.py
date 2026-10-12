"""A doubly linked list with head insertion, search, and node deletion."""


class Node:
    """Store a value and links to the previous and next nodes."""

    def __init__(self, data: object) -> None:
        self.data = data
        self.next: Node | None = None
        self.prev: Node | None = None

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    """Maintain next/prev links for n nodes, using O(n) node/link storage.

    Insert/delete change a fixed number of links, so they take O(1) when
    the node is already known. Search may visit all n nodes, taking O(n)
    with constant-time value comparisons. Stored value objects are excluded
    from the node/link space count.
    """

    def __init__(self) -> None:
        self.head: Node | None = None

    def __str__(self) -> str:
        """Return a display string without printing as a side effect.

        Visiting n links and collecting/joining L characters takes O(n + L)
        formatting work and storage. Converting values to text adds costs
        that depend on the stored objects.
        """
        values: list[str] = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        values.append("None")
        return " -> ".join(values)

    def search(self, target: object) -> Node | None:
        """Return the first matching node, or None when no value matches.

        At most n links are followed, using only one current pointer:
        O(n) time for constant-time comparisons and O(1) extra space.
        """
        current = self.head
        while current is not None:
            if current.data == target:
                return current
            current = current.next
        return None

    def insert(self, node: Node) -> None:
        """Insert a detached node at the head; node must not belong to a list.

        A fixed number of head/next/prev references change, giving O(1)
        time and extra space without scanning the list.
        """
        node.prev = None
        node.next = self.head

        if self.head is not None:
            self.head.prev = node

        self.head = node

    def delete(self, node: Node) -> None:
        """Remove a node that belongs to this list, reconnecting both directions.

        The known node gives direct access to its two neighbors. Updating
        those links and clearing its own links takes O(1) time/extra space.
        Locating the node first, if needed, is a separate O(n) search.
        """
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev

        # A removed node should not keep stale links into its former list.
        node.prev = None
        node.next = None


if __name__ == "__main__":
    linked_list = LinkedList()
    for value in range(5, 0, -1):
        linked_list.insert(Node(value))
    print(linked_list.search(3))

    linked_list.insert(Node(6))
    print(linked_list)

    node = linked_list.search(3)
    if node is not None:
        linked_list.delete(node)
    print(linked_list)
