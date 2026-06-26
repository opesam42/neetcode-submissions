from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = None
        curr_list1, curr_list2 = list1, list2
        curr_merge = None

        while curr_list1 is not None and curr_list2 is not None:
            
            lowest_node = None
            if curr_list1.val <= curr_list2.val:
                lowest_node = curr_list1
                curr_list1 = curr_list1.next
            else:
                lowest_node = curr_list2
                curr_list2 = curr_list2.next

            # breakpoint()

            # # check if mergedList is not empty - if empty the first node will be the head
            if mergedList is None:
                mergedList = lowest_node
                curr_merge = mergedList
            else:
                curr_merge.next = lowest_node
                curr_merge = curr_merge.next

        print("hello")

        while curr_list1 is not None:
            if mergedList is None:
                mergedList = curr_list1
                curr_merge = mergedList
            else:
                curr_merge.next = curr_list1
                curr_merge = curr_merge.next
            curr_list1 = curr_list1.next
        
        
        while curr_list2 is not None:
            # breakpoint()
            if mergedList is None:
                mergedList = curr_list2
                curr_merge = mergedList
            else:
                curr_merge.next = curr_list2
                curr_merge = curr_merge.next
                
            curr_list2 = curr_list2.next


        return mergedList








sol = Solution()
list1 = ListNode(-9)
list1.next = ListNode(3)

list2 = ListNode(5)
list2.next = ListNode(7)

result = sol.mergeTwoLists(list1, list2)

node = result
while node is not None:
    print(node.val)
    node = node.next