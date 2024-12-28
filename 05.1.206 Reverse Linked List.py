class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        
        return pre
        


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        # 注意这里留下的nex临时指针
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        return prev