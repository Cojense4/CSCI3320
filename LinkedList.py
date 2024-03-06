class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLink:
    def __init__(self):
        self.head = None

    def printList(self):
        pVal = self.head
        while pVal is not None:
            print(pVal.data, end=" ")
            pVal = pVal.next


liss = SingleLink()
liss.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
liss.head.nextval = e2

# Link second Node to third node
e2.next = e3

liss.printList()
