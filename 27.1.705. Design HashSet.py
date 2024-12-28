class ListNode:
    def __init__(self, key = 0):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for _ in range(10 ** 4)] 
        # use dummy node
        # we cannot use [ListNode(0)] * 10000 because it will create (just copy) 10000 same ListNode(0) object, not creating 10000 ListNode(0) objects

    def add(self, key: int) -> None:
        index = key % len(self.set)
        cur = self.set[index]
        # 这里cur指向了dummy node：node val = 0

        # 疑问：可以写作cur = self.set[index].next吗，省去了许多麻烦
        # 回答：不可以，如果是cur = self.set[index].next，接下来：
        # while cur:
        #     if cur.key == key:
        #         return
        #     cur = cur.next
        # cur = ListNode(key) 这样没有办法把链表链接起来了，必须要用cur.next = ListNode(key)才能链接起来

        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % len(self.set)
        cur = self.set[index]
        # 这里cur指向了dummy node：node val = 0
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        index = key % len(self.set)
        cur = self.set[index]
        # 这里cur指向了dummy node：node val = 0
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
