class ListNode:
    """A singly linked list node for local use; LeetCode supplies this class."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        while head is not None and head.val == val:
            head = head.next

        if head is None:
            return None

        current = head
        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return head
