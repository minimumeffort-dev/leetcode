"""Binary-tree nodes with a sideways display and three recursive traversals."""


class Node:
    """Represent a tree by its root; each traversal returns a fresh value list.

    In the traversal notes, n is the node count and h is the tree height.
    Each returned list uses O(n) space in addition to the recursion stack.
    """

    def __init__(
        self, value: int, left: "Node | None" = None, right: "Node | None" = None
    ) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """Return a sideways display, with right children above their parents."""
        lines: list[str] = []

        def visit(node: "Node | None", level: int = 0, prefix: str = "*") -> None:
            if node is None:
                return

            # Visit the right branch first to place it above the parent in text.
            visit(node.right, level + 1, "/--- ")
            lines.append(f"{'    ' * level}{prefix}{node.value}")
            visit(node.left, level + 1, "\\--- ")

        visit(self)
        return "\n".join(lines)

    def preorder(self) -> list[int]:
        """Return root/left/right order; O(n) time and O(h) recursion space."""
        values: list[int] = []

        # The helper shares this list during one call; later calls get a new list.
        def visit(node: "Node | None") -> None:
            if node is None:
                return

            values.append(node.value)
            visit(node.left)
            visit(node.right)

        visit(self)
        return values

    def inorder(self) -> list[int]:
        """Return left/root/right order; O(n) time and O(h) recursion space."""
        values: list[int] = []

        def visit(node: "Node | None") -> None:
            if node is None:
                return

            visit(node.left)
            values.append(node.value)
            visit(node.right)

        visit(self)
        return values

    def postorder(self) -> list[int]:
        """Return left/right/root order; O(n) time and O(h) recursion space."""
        values: list[int] = []

        def visit(node: "Node | None") -> None:
            if node is None:
                return

            visit(node.left)
            visit(node.right)
            values.append(node.value)

        visit(self)
        return values


if __name__ == "__main__":
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    print(tree)

    print(tree.preorder())
    print(tree.inorder())
    print(tree.postorder())
