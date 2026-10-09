class ListNode:
    """A singly linked list node for local use; LeetCode supplies this class."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        current = head
        while current is not None:
            if current.next is not None and current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
