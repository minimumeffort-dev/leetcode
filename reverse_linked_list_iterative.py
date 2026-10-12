"""LeetCode 206: Reverse Linked List, with iterative and recursive versions."""


class ListNode:
    """A singly linked list node for local use; LeetCode supplies this class."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        """Reverse links iteratively in O(n) time and O(1) extra space."""
        previous = None
        current = head

        while current is not None:
            # Save the remaining list before redirecting the current link.
            following = current.next
            current.next = previous
            previous = current
            current = following

        return previous

    def reverseRecursive(self, head: ListNode | None) -> ListNode | None:
        """Reverse links recursively in O(n) time and O(n) call-stack space."""
        if head is None or head.next is None:
            return head

        new_head = self.reverseRecursive(head.next)
        # The rest is reversed; its former first node now points back to head.
        head.next.next = head
        # Break the old forward link so these two nodes do not form a cycle.
        head.next = None
        return new_head
