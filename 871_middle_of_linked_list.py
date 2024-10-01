from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Finds the middle node of a linked list.
        
        Uses two pointers, one that moves one step at a time and one that moves
        two steps at a time. When the fast pointer reaches the end, the slow pointer
        will be at the middle.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        if head and not head.next:
            return head

        slow_ptr = head
        fast_ptr = head

        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr
