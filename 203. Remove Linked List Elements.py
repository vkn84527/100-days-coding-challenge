# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        node=head
        a=[]
        while node:
            a.append(node.val)
            node=node.next
        print(a)
        while(1):
            if val in a:
                a.remove(val)
            else:
                break
        
        dummy=node=ListNode(0)
        for i in a:
            node.next=ListNode(i)
            node=node.next
        return dummy.next
        
