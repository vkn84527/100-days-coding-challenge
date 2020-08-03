# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        b=[]
        c=[]
        p=[]
        node=head
        while node:
            b.append(node.val)
            node=node.next
        for i in range(len(b)):
            if i%2==0:
                c.append(b[i])
            else:
                p.append(b[i])
        
        d=c+p
        print(c,p,d)
        dummy=node=ListNode(0)
        for i in d:
            node.next=ListNode(i)
            node=node.next
        return dummy.next
                
                
        
