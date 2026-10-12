class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        lines = []

        def visit(node, level=0, prefix="*"):
            if node is None:
                return

            visit(node.right, level + 1, "/--- ")
            lines.append(f"{'    ' * level}{prefix}{node.value}")
            visit(node.left, level + 1, "\\--- ")

        visit(self)
        return "\n".join(lines)

    def preorder(self, root, nodes=None):
        if nodes is None:
            nodes = []

        if root is None:
            return nodes

        nodes.append(root.value)
        self.preorder(root.left, nodes)
        self.preorder(root.right, nodes)

        return nodes

    def inorder(self, root, nodes=None):
        if nodes is None:
            nodes = []

        if root is None:
            return nodes

        self.inorder(root.left, nodes)
        nodes.append(root.value)
        self.inorder(root.right, nodes)

        return nodes


if __name__ == "__main__":
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    print(tree)

    dlr = tree.preorder(tree)
    print(dlr)
    ldr = tree.inorder(tree)
    print(ldr)
