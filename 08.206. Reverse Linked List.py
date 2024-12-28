# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        newHead = head
        # newHead = head 非常重要，如果head.next没有，那么无法运行下面的if语句，newHead相当于没有定义
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
            head.next = None

        return newHead


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        # 相比于上面的方法，这里打个补丁也行
        if not head.next:
            return head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
            head.next = None

        return newHead
