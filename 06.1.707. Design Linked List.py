class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
    # left dummy node and right dummy node
    # left dummy node <-> right dummy node

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index ==0:
            return curr.val
        return -1



    def addAtHead(self, val: int) -> None:
        node, next, prev = ListNode(val), self.left.next, self.left
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev



    def addAtTail(self, val: int) -> None:
        node, next, prev = ListNode(val), self.right, self.right.prev
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev


    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            node, next, prev = ListNode(val), curr, curr.prev
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev



    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index == 0:
            next, prev = curr.next, curr.prev
            next.prev = prev
            prev.next = next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# My MyLinkedList object will be instantiated and called as such:
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head, self.tail = Node(0), Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        return cur.val if cur and cur != self.tail else -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        h = self.head
        n = self.head.next
        h.next = newNode
        newNode.next = n
        newNode.prev = h
        n.prev = newNode

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        t = self.tail
        p = self.tail.prev
        t.prev = newNode
        newNode.next = t
        newNode.prev = p
        p.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head.next
        for i in range(index):
            cur = cur.next

        p = cur.prev
        newNode = Node(val)
        p.next = newNode
        newNode.next = cur
        newNode.prev = p
        cur.prev = newNode

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        for i in range(index):
            cur = cur.next

        p = cur.prev
        n = cur.next
        p.next = n
        n.prev = p


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# have bugs:
# try to use the linked list not the double linked list
class MyLinkedList:

    def __init__(self):
        self.head = Node(0)

    def get(self, index: int) -> int:
        cur = self.head.next

        for _ in range(index):
            cur = cur.next
            if not cur:
                return -1

        return cur.val

    def addAtHead(self, val: int) -> None:
        cur = self.head.next
        newNode = Node(val)
        newNode.next = cur
        self.head.next = newNode

    def addAtTail(self, val: int) -> None:
        cur = self.head
        while cur.next:
            cur = cur.next
        newNode = Node(val)
        cur.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head
        for _ in range(index):
            cur = cur.next
            if not cur:
                return
        newNode = Node(val)
        newNode.next = cur.next
        cur.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        for _ in range(index):
            cur = cur.next
            if not cur:
                return
        cur.next = cur.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
