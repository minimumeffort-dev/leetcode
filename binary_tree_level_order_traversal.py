"""LeetCode 102: Binary Tree Level Order Traversal, using breadth-first search.

Problem: https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

from collections import deque


class TreeNode:
    """A binary-tree node matching LeetCode's node definition."""

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
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """Return values from left to right, grouped by tree level.

        Time is O(n): each of the n nodes is queued and removed once, and
        deque operations take O(1) amortized time. The nested loops still
        process only n nodes in total, appending each value once.

        Auxiliary space is O(w), where w is the maximum tree width. The
        queue holds parts of two adjacent levels, at most O(w) nodes.
        The output stores n values across at most n lists, taking O(n) space.
        The original tree is not changed.
        """
        if root is None:
            return []

        levels: list[list[int]] = []
        queue = deque([root])
        while queue:
            # Children appended below belong to the next level, not this one.
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                # Queue only real children, with the left child before the right.
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            # Every queued entry is a node, so this level cannot be empty.
            levels.append(level)

        return levels


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            "LeetCode example",
            TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),
            [[3], [9, 20], [15, 7]],
        ),
        ("Empty tree", None, []),
        ("Single zero-valued node", TreeNode(0), [[0]]),
        (
            "Complete tree",
            TreeNode(
                1,
                TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3, TreeNode(6), TreeNode(7)),
            ),
            [[1], [2, 3], [4, 5, 6, 7]],
        ),
        (
            "Sparse tree",
            TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3, TreeNode(5))),
            [[1], [2, 3], [4, 5]],
        ),
        ("Left chain", TreeNode(1, TreeNode(2, TreeNode(3))), [[1], [2], [3]]),
        (
            "Right chain",
            TreeNode(1, right=TreeNode(2, right=TreeNode(3))),
            [[1], [2], [3]],
        ),
        (
            "Repeated values",
            TreeNode(1, TreeNode(1, TreeNode(1)), TreeNode(1)),
            [[1], [1, 1], [1]],
        ),
    ]

    for name, root, expected in test_cases:
        found = solution.levelOrder(root)
        print(f"{name}: levels={found}, expected={expected}")
        assert found == expected, name
