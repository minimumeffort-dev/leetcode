"""Recursive membership search in a binary search tree."""


class TreeNode:
    """Store an integer value and optional left and right children."""

    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def binary_search(root: TreeNode | None, target: int) -> bool:
    """Return whether target exists in a valid binary search tree.

    Each comparison follows one child, so at most h nodes are checked for
    tree height h. This gives O(h) time with constant-cost comparisons and
    O(h) stack space: O(log n) for a balanced tree, O(n) for a chain.
    Very deep trees can hit Python's recursion limit.
    """
    if root is None:
        # Reaching an empty child means the target is absent from this path.
        return False

    if root.val == target:
        return True

    # All smaller values are on the left; all larger values are on the right.
    if target < root.val:
        return binary_search(root.left, target)
    return binary_search(root.right, target)


if __name__ == "__main__":
    balanced_tree = TreeNode(
        8,
        TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))),
        TreeNode(12, TreeNode(10), TreeNode(14, TreeNode(13))),
    )
    single_node = TreeNode(5)

    # These trees have height n, so a search can visit every node in the chain.
    left_chain = TreeNode(3, TreeNode(2, TreeNode(1)))
    right_chain = TreeNode(1, right=TreeNode(2, right=TreeNode(3)))

    test_cases = [
        ("Balanced tree, root", balanced_tree, 8, True),
        ("Balanced tree, left child", balanced_tree, 3, True),
        ("Balanced tree, left descendant", balanced_tree, 4, True),
        ("Balanced tree, right descendant", balanced_tree, 13, True),
        ("Balanced tree, missing value", balanced_tree, 9, False),
        ("Balanced tree, below minimum", balanced_tree, 0, False),
        ("Balanced tree, above maximum", balanced_tree, 15, False),
        ("Single node, found", single_node, 5, True),
        ("Single node, missing", single_node, 4, False),
        ("Empty tree", None, 5, False),
        ("Left chain, found", left_chain, 1, True),
        ("Left chain, missing", left_chain, 0, False),
        ("Right chain, found", right_chain, 3, True),
        ("Right chain, missing", right_chain, 4, False),
    ]

    for name, root, target, expected in test_cases:
        found = binary_search(root, target)
        print(f"{name}: target={target}, found={found}, expected={expected}")
        assert found is expected, f"{name}: expected {expected}, got {found}"
