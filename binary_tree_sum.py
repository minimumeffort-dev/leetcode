"""A binary-tree example with a sideways display and a recursive value sum."""


class TreeNode:
    """Store an integer value and optional left and right children."""

    def __init__(
        self,
        value: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """Return a sideways display, with right children above their parents.

        Building indentation/lines and joining c displayed characters costs
        O(c) formatting time and string storage, plus O(h) call frames
        for tree height h.
        A chain can produce O(n^2) indentation characters as depth grows.
        """
        lines: list[str] = []

        def visit(
            node: "TreeNode | None", level: int = 0, prefix: str = "Root: "
        ) -> None:
            if node is None:
                return

            # Reverse inorder places the right branch above the parent in text.
            visit(node.right, level + 1, "/--- ")
            lines.append(f"{'    ' * level}{prefix}{node.value}")
            visit(node.left, level + 1, "\\--- ")

        visit(self)
        return "\n".join(lines)

    def find_sum(self) -> int:
        """Sum all values in O(n) time and O(h) stack space, for tree height h.

        Each of n nodes contributes once, assuming constant-cost additions.
        Only one root-to-leaf path is active, giving h call frames: O(log n)
        for a balanced tree and O(n) for a chain. No value list is collected.
        """

        def subtree_sum(node: "TreeNode | None") -> int:
            if node is None:
                # An absent branch contributes zero to its parent's sum.
                return 0
            return node.value + subtree_sum(node.left) + subtree_sum(node.right)

        return subtree_sum(self)


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(3, TreeNode(1, TreeNode(5), TreeNode(6))), TreeNode(8))
    print(root)
    print(root.find_sum())
