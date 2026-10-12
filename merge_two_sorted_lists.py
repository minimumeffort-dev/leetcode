"""LeetCode 21: Merge Two Sorted Lists."""


class ListNode:
    """A singly linked list node for local use; LeetCode supplies this class."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        """Reuse the nodes in O(n + m) time with O(1) extra space."""
        # A dummy head lets empty inputs and the first insertion use the same code.
        dummy = ListNode()
        tail = dummy

        while list1 is not None and list2 is not None:
            # Prefer the first list on ties, preserving a stable merge order.
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # The remaining suffix is already sorted and can be attached as a whole.
        tail.next = list1 if list1 is not None else list2
        return dummy.next
