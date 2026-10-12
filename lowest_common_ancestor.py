"""LeetCode 236: Lowest Common Ancestor of a Binary Tree.

Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""


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
    def lowestCommonAncestor(
        self, root: TreeNode | None, p: TreeNode, q: TreeNode
    ) -> TreeNode | None:
        """Return the lowest common ancestor using node identity.

        The original tree must contain both targets, as the problem guarantees.
        This allows returning a target without searching its descendants.

        Each of n nodes is visited at most once, giving O(n) worst-case time.
        Active calls follow a root-to-leaf path, so recursion uses O(h) space
        for height h: O(log n) in a balanced tree and O(n) in a chain.
        Very deep trees can hit Python's recursion limit.
        """
        # An empty branch returns None; a target may itself be the ancestor.
        if root is None or root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # The targets were found in different branches.
        if left is not None and right is not None:
            return root

        # Pass up a target or the ancestor already found deeper in one branch.
        return left if left is not None else right


if __name__ == "__main__":
    #         3
    #        / \
    #       5   1
    #      / \ / \
    #     6  2 0  8
    #       / \
    #      7   4
    node_6 = TreeNode(6)
    node_7 = TreeNode(7)
    node_4 = TreeNode(4)
    node_2 = TreeNode(2, node_7, node_4)
    node_5 = TreeNode(5, node_6, node_2)
    node_0 = TreeNode(0)
    node_8 = TreeNode(8)
    node_1 = TreeNode(1, node_0, node_8)
    root = TreeNode(3, node_5, node_1)

    solution = Solution()
    test_cases = [
        ("Different sides", node_5, node_1, root),
        ("Both on the left", node_6, node_4, node_5),
        ("Ancestor on the left", node_5, node_4, node_5),
        ("Both on the right", node_0, node_8, node_1),
        ("Ancestor on the right", node_1, node_8, node_1),
        ("Root is a target", root, node_7, root),
        ("Deep siblings", node_7, node_4, node_2),
    ]

    for name, p, q, expected in test_cases:
        ancestor = solution.lowestCommonAncestor(root, p, q)
        value = ancestor.val if ancestor is not None else None
        print(
            f"{name}: p={p.val}, q={q.val}, "
            f"ancestor={value}, expected={expected.val}"
        )
        assert ancestor is expected, name
