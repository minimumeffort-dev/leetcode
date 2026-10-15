"""LeetCode 314: Binary Tree Vertical Order Traversal, using breadth-first search.

Problem: https://leetcode.com/problems/binary-tree-vertical-order-traversal/
"""

from collections import defaultdict, deque


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
    def verticalOrder(self, root: TreeNode | None) -> list[list[int]]:
        """Group values by column, ordered top to bottom and then left to right.

        Expected time is O(n): each node is queued and removed once, with
        O(1) expected dictionary operations and amortized deque operations.
        There are at most n columns, so assembling the result is also O(n).
        Tracking the column bounds avoids sorting the dictionary keys.

        Total space is O(n): the column lists store n values, the dictionary
        has at most n entries, and the queue holds O(w) nodes, where w is
        the maximum tree width. The column lists are reused in the output.
        The original tree is left unchanged.
        """
        if root is None:
            return []

        queue = deque([(root, 0)])
        min_col, max_col = 0, 0
        columns: defaultdict[int, list[int]] = defaultdict(list)

        while queue:
            node, col = queue.popleft()
            min_col, max_col = min(min_col, col), max(max_col, col)
            columns[col].append(node.val)

            # BFS orders rows; left before right preserves ties within a column.
            if node.left is not None:
                queue.append((node.left, col - 1))
            if node.right is not None:
                queue.append((node.right, col + 1))

        # No gaps: reaching a column requires crossing every column on the way.
        return [columns[col] for col in range(min_col, max_col + 1)]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("Empty tree", None, []),
        ("Single zero-valued node", TreeNode(0), [[0]]),
        (
            "Columns around the root",
            TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),
            [[9], [3, 15], [20], [7]],
        ),
        (
            "Several nodes in the middle column",
            TreeNode(
                3,
                TreeNode(9, TreeNode(4), TreeNode(0)),
                TreeNode(8, TreeNode(1), TreeNode(7)),
            ),
            [[4], [9], [3, 0, 1], [8], [7]],
        ),
        (
            "Same position keeps left-to-right order, not value order",
            TreeNode(
                0,
                TreeNode(10, right=TreeNode(99)),
                TreeNode(20, TreeNode(-99)),
            ),
            [[10], [0, 99, -99], [20]],
        ),
        (
            "Shallower node comes before a deeper node in the same column",
            TreeNode(
                1,
                TreeNode(2, right=TreeNode(4, right=TreeNode(5))),
                TreeNode(3),
            ),
            [[2], [1, 4], [3, 5]],
        ),
        (
            "Negative values",
            TreeNode(-1, TreeNode(-2), TreeNode(-3)),
            [[-2], [-1], [-3]],
        ),
        ("Repeated values", TreeNode(2, TreeNode(2), TreeNode(2)), [[2], [2], [2]]),
        ("Left chain", TreeNode(1, TreeNode(2, TreeNode(3))), [[3], [2], [1]]),
        (
            "Right chain",
            TreeNode(1, right=TreeNode(2, right=TreeNode(3))),
            [[1], [2], [3]],
        ),
    ]

    for name, root, expected in test_cases:
        found = solution.verticalOrder(root)
        print(f"{name}: columns={found}, expected={expected}")
        assert found == expected, name
