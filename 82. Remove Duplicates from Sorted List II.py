# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        a=[]
        b=[]
        node=head
        while node:
            a.append(node.val)
            node=node.next
        print(a)
        for i in a:
            if(a.count(i)>1):
                continue
            b.append(i)
        dummy=node=ListNode(0)
        for i in b:
            node.next=ListNode(i)
            node=node.next
        return dummy.next
        
