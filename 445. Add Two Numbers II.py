# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a=[]
        b=[]
        node=l1
        node2=l2
        while node:
            a.append(node.val)
            node=node.next
        while node2:
            b.append(node2.val)
            node2=node2.next
        s=''
        k=''
        for i in a:
            s=s+str(i)
        for j in b:
            k=k+str(j)
        print(s,k)
        c=(int(s)+int(k))
        print(c)
        dummy=node=ListNode(0)
        for  i in str(c):
            node.next=ListNode(int(i))
            node=node.next
        return dummy.next
            
        
        
