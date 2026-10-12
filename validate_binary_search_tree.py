"""LeetCode 98: Validate Binary Search Tree.

Validate a binary search tree using bounds inherited from its ancestors.

Problem: https://leetcode.com/problems/validate-binary-search-tree/
Submission:
https://leetcode.com/problems/validate-binary-search-tree/submissions/2169960110/
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
    def isValidBST(self, root: TreeNode | None) -> bool:
        """Return whether every subtree obeys the strict BST ordering rules.

        Each of n nodes is checked at most once, giving O(n) worst-case time
        with constant-cost comparisons. Active calls follow a root-to-leaf
        path, so the stack uses O(h) space for height h: O(log n) in a balanced
        tree and O(n) in a chain. Very deep trees can hit Python's recursion
        limit.
        """

        def validate(
            node: TreeNode | None, minimum: int | float, maximum: int | float
        ) -> bool:
            if node is None:
                # An empty subtree contains no values that violate the bounds.
                return True

            # Strict bounds also reject duplicates, even below another ancestor.
            if node.val <= minimum or node.val >= maximum:
                return False

            # Tighten one bound for each child and keep the other ancestor limit.
            return validate(node.left, minimum, node.val) and validate(
                node.right, node.val, maximum
            )

        # Infinite bounds allow every integer value at the root.
        return validate(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    solution = Solution()
    valid_tree = TreeNode(2, TreeNode(1), TreeNode(3))

    # 4 is smaller than its parent 7, but cannot be in 5's right subtree.
    invalid_tree = TreeNode(5, TreeNode(1), TreeNode(7, TreeNode(4), TreeNode(8)))

    print("Valid tree:", solution.isValidBST(valid_tree))  # True
    print("Invalid tree:", solution.isValidBST(invalid_tree))  # False
