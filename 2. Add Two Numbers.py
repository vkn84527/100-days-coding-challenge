class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1=l1[::-1]
        l2=l2[::-1]
        return l1+l2
        
