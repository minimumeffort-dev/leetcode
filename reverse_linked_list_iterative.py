class ListNode:
    """A singly linked list node for local use; LeetCode supplies this class."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        previous = None
        current = head

        while current is not None:
            following = current.next  # Save the next node before changing the link.
            current.next = previous
            previous = current
            current = following

        return previous

    def reverseRecursive(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseRecursive(head.next)
            head.next.next = head
        head.next = None
        return newHead
