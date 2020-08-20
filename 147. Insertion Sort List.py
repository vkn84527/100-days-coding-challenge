# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        a=[]
        node=head
        while node:
            a.append(node.val)
            node=node.next
        a=sorted(a)
        dummy=node=ListNode(0)
        for i in a:
            node.next=ListNode(i)
            node=node.next
        return dummy.next
        
