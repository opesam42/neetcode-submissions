# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the mid point
        slow = head
        fast = head
        while fast is not None and fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # slow pointer node becomes pivot
        pivot = slow

        # trying to split the linked list
        # point the prev of the right linked list to none
        right_list_head = pivot.next
        pivot.next = None

        # and reverse the right linked list 
        p1 = None
        p2 = right_list_head

        # this is to capture the head of right linked list after been sorted
        new_right_head = None

        while p2 is not None:
            next = p2.next
            p2.next = p1

            p1, p2 = p2, next
            

        # completely reverse the right side, now time to reorder

        # point the first node of the left to the fist of the right, and so on for second, third 
        left = head
        right = p1

        while left is not None and right is not None:
            left_next = left.next
            right_next = right.next

            left.next = right
            right.next = left_next


            left = left_next
            right = right_next
        
        
        # breakpoint()
        # return head