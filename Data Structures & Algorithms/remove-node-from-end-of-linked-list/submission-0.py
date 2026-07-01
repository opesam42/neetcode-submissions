from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # we would use tow pointers and make the like distance from the two pointers at initiation to be n, so if n is 2 the element between the two pointers would be 2 (or 2 nodes)

        first = head
        second = None
        
        # move first pointer n ahead of the head
        count = 0
        while count < n:
            first = first.next
            count += 1

        # move the first and second until first hit null, and due to our initaition, second would be behind the node to be removed
        while first is not None:
            first = first.next
            if second is None:
                second = head
            else:
                second = second.next

        # added to deal when the n node to be removed is the head and this causes problem with the second pointer, can skip now, as it handles like a edge case
        if second is None:
            # remove head
            print("hello")
            head = head.next
            return head

        # now second is behind the nth node from the end to be removed, now change the next of second to point to the next of the node to be removed

        n_node = second.next
        n_node_next = n_node.next

        # point the node to be remove next to none
        n_node.next = None

        # point tthe second next to the original next of the n node to be removed
        second.next = n_node_next

        print(head)

        return head
        

