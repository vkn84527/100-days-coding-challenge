# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        l = []
        toli = head
        while toli:
            l.append(toli.val)
            toli = toli.next
        #print(li)
        
        i=0
        nl=[]
        while(i<len(l)):
            x=[]
            ct=0
            while(i<len(l) and ct<k):
                ct+=1
                x.append(l[i])
                i+=1
            if(len(x)==k):
                nl+=x[::-1]
            else:
                nl+=x

        h = dummy = ListNode(0)
        for value in nl:
            h.next = ListNode(value)
            h = h.next
        return dummy.next
