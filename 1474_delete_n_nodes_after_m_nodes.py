from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None:
            return None

        dummy_head = ListNode(val=None, next=None)
        dummy_head.next = head
        prev = dummy_head
        current = head

        while current is not None:
            # keep 'm' nodes
            for _ in range(m):
                # if we're at the end, return
                if not current:
                    return dummy_head.next
                prev = current
                current = current.next

            # delete 'n' nodes
            for _ in range(n):
                if not current:
                    break
                current = current.next

            # Connect the previous node to the current node (after deletion)
            prev.next = current

        return dummy_head.next