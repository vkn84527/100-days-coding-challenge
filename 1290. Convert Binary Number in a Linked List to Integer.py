# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        b=[]
        node=head
        while node:
            b.append(node.val)
            node=node.next
        s=''
        for i in b:
            s=s+str(i)
        c=int(s,2)
        return c
        
