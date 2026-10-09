class TreeNode:
    def __init__(
        self, value: int = 0, left: "TreeNode" = None, right: "TreeNode" = None
    ) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        lines = []

        def visit(node, level=0, prefix="Root: "):
            if node is None:
                return

            visit(node.right, level + 1, "/--- ")
            lines.append(f"{'    ' * level}{prefix}{node.value}")
            visit(node.left, level + 1, "\\--- ")

        visit(self)
        return "\n".join(lines)

    def find_sum(self) -> int:
        def sum(root) -> int:
            if root is None:
                return 0
            return root.value + sum(root.left) + sum(root.right)

        return sum(self)


if __name__ == "__main__":
    head = TreeNode(1, TreeNode(3, TreeNode(1, TreeNode(5), TreeNode(6))), TreeNode(8))
    print(head)
    print(head.find_sum())
