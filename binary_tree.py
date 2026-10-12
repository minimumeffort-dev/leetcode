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

    def preorder(self):
        nodes = []

        def visit(node):
            if node is None:
                return

            nodes.append(node.value)
            visit(node.left)
            visit(node.right)

        visit(self)
        return nodes

    def inorder(self):
        nodes = []

        def visit(node):
            if node is None:
                return

            visit(node.left)
            nodes.append(node.value)
            visit(node.right)

        visit(self)
        return nodes

    def postorder(self):
        nodes = []

        def visit(node):
            if node is None:
                return

            visit(node.left)
            visit(node.right)
            nodes.append(node.value)

        visit(self)
        return nodes


if __name__ == "__main__":
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    print(tree)

    dlr = tree.preorder()
    print(dlr)
    ldr = tree.inorder()
    print(ldr)
    lrd = tree.postorder()
    print(lrd)
