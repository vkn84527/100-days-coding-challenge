def llist_to_list(llist):
    ans = []
    if llist:
        while True:
            ans.append(llist.val)
            llist = llist.next
            if llist == None:
                break
    else:
        return []
    return ans

def list_to_llist(li):
    if li:
        head = ListNode(li[0])
        head_copy = head
        for l in li[1:]:
            node = ListNode(l)
            head.next = node
            head = head.next
    else:
        return None
    return head_copy

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        li = llist_to_list(head)
        print('li', li)
        l = len(li)
        if l != 0: k %= l
        new_l = li[l - k:] + li[:l - k]
        print(new_l)
        return list_to_llist(new_l)
