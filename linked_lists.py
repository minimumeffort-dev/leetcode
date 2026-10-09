class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        return ""

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return current
            current = current.next
        return None

    def insert(self, node):
        node.next = self.head

        if self.head:
            self.head.prev = node

        self.head = node
        node.prev = None

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev


if __name__ == "__main__":
    ll = LinkedList()
    for value in range(5, 0, -1):
        ll.insert(Node(value))
    print(ll.search(3))

    ll.insert(Node(6))
    print(ll)

    ll.delete(ll.search(3))
    print(ll)
