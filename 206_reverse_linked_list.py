# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        prev_node = None
        while curr_node is not None:
            # save the next node of the current node
            next_node = curr_node.next

            # swap the next node of this node to be equal to the previous node
            curr_node.next = prev_node

            # now make the current node the new 'prev_node' for the next iteration
            prev_node = curr_node

            # move the curr_node to be the next node of the original linked list
            curr_node = next_node

        # return the final prev_node, which becomes the new head
        return prev_node