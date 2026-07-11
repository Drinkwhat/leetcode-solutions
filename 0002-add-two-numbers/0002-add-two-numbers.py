# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        curR = ListNode((l1.val + l2.val + 0) % 10)
        rip = (l1.val + l2.val + 0) // 10
        res = curR
        while cur1.next != None or cur2.next != None or rip != 0:
            cur1 = cur1.next if cur1.next != None else ListNode()
            cur2 = cur2.next if cur2.next != None else ListNode()
            curR.next = ListNode((cur1.val + cur2.val + rip) % 10)
            rip = (cur1.val + cur2.val + rip) // 10
            curR = curR.next
        return  res
        
        