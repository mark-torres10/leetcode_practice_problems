from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """Removes elements from a linked list. Creates a new linked list.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        new_head = ListNode(val=None, next=None)
        output_ptr = new_head
        current_node = head
        
        while current_node is not None:
            # skip any nodes that have the value to remove.
            # only operate when the node != val.
            if current_node.val != val:
                # create a new node with the current value
                new_node = ListNode(val=current_node.val)
                # set the new node's "next" to be the existing new linked list
                output_ptr.next = new_node
                # set that new node as the new head
                output_ptr = new_node
            current_node = current_node.next
        return new_head.next
    
    def removeElementsInPlace(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """Removes elements from a linked list. Modifies the existing linked list.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        if not head:
            return None

        dummy_node = ListNode(val=None, next=None)
        dummy_node.next = head
        prev = dummy_node
        current = head

        while current is not None:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return dummy_node.next
