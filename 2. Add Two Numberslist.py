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
        a=a[::-1]
        b=b[::-1]
        s=''
        s1=''
        for i in a:
            s=s+str(i)
        for i1 in b:
            s1=s1+str(i1)
        s2=int(s)+int(s1)
        print(s2)
        c=[]
        for i in str(s2):
            c.append(int(i))
        c=c[::-1]
        dummy=node=ListNode(0)
        for i in c:
            node.next=ListNode(i)
            node=node.next
        return dummy.next
        
