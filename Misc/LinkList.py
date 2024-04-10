class Node:
    def __init__(self, data=None, nNode=None, pNode=None):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f"Node: {self.data}, next: {self.next}\n"


class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def fInsert(self, nData):
        nNode = Node(nData)
        nNode.next = self.head
        if self.head is not None:
            self.head.prev = nNode
            self.head = nNode
            nNode.prev = None
        else:
            self.head = nNode
            self.tail = nNode
            nNode.prev = None

    def bInsert(self, nData):
        nNode = Node(nData, None, None)
        nNode.next = self.head
        if self.head is not None:
            nNode.prev = self.tail
            self.tail.next = nNode
            self.tail = nNode
        else:
            self.head = nNode
            self.tail = self.head
        self.count += 1

    def locInsert(self, data):
        pass


class SLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def __str__(self):
        return self.head


liss = SLinkedList()
liss.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
liss.head.next = e2

# Link second Node to third node
e2.next = e3

print(liss)
