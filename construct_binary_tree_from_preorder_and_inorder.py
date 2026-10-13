"""LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal.

Problem:
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

from collections import deque


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


class Solution:
    def buildTree(
        self, preorder: list[int], inorder: list[int]
    ) -> TreeNode | None:
        """Rebuild a tree from valid traversals containing unique values.

        Building the index map takes O(n) time and space. Each of n nodes
        is created once, with an average O(1) lookup for its inorder position,
        giving O(n) expected time. Passing bounds avoids copying sublists.

        The map uses O(n) space and the stack uses O(h), for tree height h:
        O(log n) when balanced and O(n) for a chain. Total working space is
        O(n), and the returned tree stores n new nodes. Very deep trees can
        hit Python's recursion limit.
        """
        positions = {
            value: index
            for index, value in enumerate(inorder)
        }
        preorder_index = 0

        def build(left: int, right: int) -> TreeNode | None:
            nonlocal preorder_index

            # Bounds are inclusive; crossed bounds describe an empty subtree.
            if left > right:
                return None

            # The next preorder value is this subtree's root.
            root_value = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(root_value)

            split = positions[root_value]

            # Building the entire left side moves the pointer to the right root.
            root.left = build(left, split - 1)
            root.right = build(split + 1, right)

            return root

        return build(0, len(inorder) - 1)


if __name__ == "__main__":
    def level_order(root: TreeNode | None) -> list[int | None]:
        """Display the example tree as LeetCode values in O(n) time and space."""
        values: list[int | None] = []
        queue: deque[TreeNode | None] = deque([root])

        while queue:
            node = queue.popleft()
            if node is None:
                values.append(None)
            else:
                values.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        while values and values[-1] is None:
            values.pop()
        return values

    solution = Solution()
    test_cases = [
        (
            "LeetCode example",
            [3, 9, 20, 15, 7],
            [9, 3, 15, 20, 7],
            [3, 9, 20, None, None, 15, 7],
        ),
        ("Single node", [-1], [-1], [-1]),
        ("Empty tree", [], [], []),
        ("Left chain", [3, 2, 1], [1, 2, 3], [3, 2, None, 1]),
        ("Right chain", [1, 2, 3], [1, 2, 3], [1, None, 2, None, 3]),
        (
            "Balanced tree",
            [4, 2, 1, 3, 6, 5, 7],
            [1, 2, 3, 4, 5, 6, 7],
            [4, 2, 6, 1, 3, 5, 7],
        ),
    ]

    for name, preorder, inorder, expected in test_cases:
        root = solution.buildTree(preorder, inorder)
        values = level_order(root)
        print(f"{name}: tree={values}, expected={expected}")
        assert values == expected, name
