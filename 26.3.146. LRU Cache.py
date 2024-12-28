from typing import Optional, List
from collections import deque, Counter, defaultdict
from bisect import bisect_left, bisect_right
from functools import cache
from itertools import pairwise
import heapq


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        # 双向链表


# Least Recently Used (LRU) cache
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node
        # 输入一个cache[key] 就会映射到它的链表的节点，拥有链表节点的一切属性

        self.left, self.right = Node(0, 0), Node(0, 0)  # dummy node
        self.left.next = self.right
        self.right.prev = self.left
        # 连接初始两个节点：左和右
        # left: least used node, right: most used node

    def remove(self, node):
        # node is a middle node
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        # or we can just use ''node.prev.next = node.next'' and ''node.next.prev = node.prev''

    def insertRight(self, node):
        nextNode = self.right
        prevNode = nextNode.prev
        prevNode.next = node
        nextNode.prev = node
        node.prev = prevNode
        node.next = nextNode

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insertRight(self.cache[key])
            return self.cache[key].val
            # 因为输入一个cache[key] 就会映射到它的链表的节点，拥有链表节点的一切属性
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insertRight(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class Node:
    # 提高访问属性的速度，并节省内存
    __slots__ = "prev", "next", "key", "value"

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()  # 哨兵节点
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_to_node = dict()

    # 获取 key 对应的节点，同时把该节点移到链表头部
    def get_node(self, key: int) -> Optional[Node]:
        if key not in self.key_to_node:  # 没有这本书
            return None
        node = self.key_to_node[key]  # 有这本书
        self.remove(node)  # 把这本书抽出来
        self.push_front(node)  # 放在最上面
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:  # 有这本书
            node.value = value  # 更新 value
            return
        self.key_to_node[key] = node = Node(key, value)  # 新书
        self.push_front(node)  # 放在最上面
        if len(self.key_to_node) > self.capacity:  # 书太多了
            back_node = self.dummy.prev
            del self.key_to_node[back_node.key]
            self.remove(back_node)  # 去掉最后一本书

    # 删除一个节点（抽出一本书）
    def remove(self, x: Node) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev

    # 在链表头添加一个节点（把一本书放在最上面）
    def push_front(self, x: Node) -> None:
        x.prev = self.dummy
        x.next = self.dummy.next
        x.prev.next = x
        x.next.prev = x
