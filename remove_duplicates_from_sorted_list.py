"""LeetCode 83: Remove Duplicates from Sorted List."""


class ListNode:
    """A singly linked list node for local use; LeetCode supplies this class."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        """Keep one node per value in a sorted list; O(n) time, O(1) space."""
        current = head
        while current is not None and current.next is not None:
            if current.val == current.next.val:
                # Stay at this node to remove the rest of a repeated run too.
                current.next = current.next.next
            else:
                current = current.next
        return head
