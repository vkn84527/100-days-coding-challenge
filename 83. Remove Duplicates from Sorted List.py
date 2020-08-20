# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        a=[]
        s=set()
        node=head
        while node:
            a.append(node.val)
            node=node.next
        for i in a:
            s.add(i)
        node=dummy=ListNode(0)
        s=list(s)
        s.sort()
        for i in s:
            node.next=ListNode(i)
            node=node.next
        return dummy.next
        
