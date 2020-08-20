# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node=head
        a=[]
        while node:
            a.append(node.val)
            node=node.next
        if a==a[::-1]:
            return 1
        return 0
