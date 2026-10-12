"""LeetCode 203: Remove Linked List Elements."""


class ListNode:
    """A singly linked list node for local use; LeetCode supplies this class."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        """Remove matching nodes in O(n) time and O(1) extra space."""
        # Head matches have no previous node to reconnect, so handle them first.
        while head is not None and head.val == val:
            head = head.next

        if head is None:
            return None

        current = head
        while current.next is not None:
            if current.next.val == val:
                # Keep current here: its new next node may also need removal.
                current.next = current.next.next
            else:
                current = current.next

        return head
