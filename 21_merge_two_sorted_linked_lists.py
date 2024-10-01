# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """Merge two sorted linked lists.
        
        Key is that it uses a dummy head node to simplify the process and then
        takes each node from the two linked lists and just updates their next
        pointers.

        Time complexity: O(n + m)
            - We traverse both linked lists once.
        Space complexity: O(1)
            - We only use pointers and don't use any additional data structures.
        """
        # edge casing
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # create dummy head node
        head = ListNode(val=None, next=None)

        # create output pointer to track progress in the linked list
        output_ptr = head

        # iterate through both linked lists and add the corresponding correct value.
        while (list1 is not None) and (list2 is not None):
            if list1.val <= list2.val:
                # set the next value of the output pointer to be equal to the list1 pointer
                output_ptr.next = list1

                # update the list1 pointer to be the next value
                list1 = list1.next
            else:
                # set the next value of the output pointer to be equal to the list2 pointer
                output_ptr.next = list2

                # update the list2 pointer to be the next value
                list2 = list2.next
            
            # update the output pointer to be the next value in the pointer
            output_ptr = output_ptr.next
        
        # once one of the linked lists has been flushed, flush the remaining list.
        # only need to add the remaining linked list as the 'next' of the last node
        # in output_ptr since that will naturally bring along the rest of the values
        # of the remaining linked list
        if list1:
            output_ptr.next = list1
        elif list2:
            output_ptr.next = list2

        # return the next node after the head, since this will be the first node
        # in the actual linked list
        return head.next
