from typing import Any


class Node:  # Singly Linked Node
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:  # Single Linked List
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self) -> bool:  # Boolean to check if the list is empty
        if self.head is None:
            return True
        else:
            return False

    def prepend(self, data) -> object:  # Encapsulate the data in a Node
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        return node

    def append(self, data) -> object:  # Encapsulate the data in a Node
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return node

    def delete_first_node(self) -> Any:
        current = self.head
        if self.head is None:
            print("No data element to delete")
            return None
        elif current == self.head:
            self.head = current.next
            self.length -= 1
            return current.data

    def delete_last_node(self) -> Any:
        current = self.head
        prev = self.head
        if self.head is None:
            print("No data element to delete")
            return None
        while current:
            if current.next is None:
                prev.next = current.next
                self.tail = prev
                self.length -= 1
                return current.data
            prev = current
            current = current.next

    def printInOrder(self):  # Recurse starting with the head node
        # Start an in-order printing of node items for the given list
        def printNext(node):  # Do not edit this function
            """If the node is valid, print the given node and then continue to recurse"""
            if node is None:
                return None
            if node.next is not None:
                print(str(node.data), " => ", end='')
            else:
                print(str(node.data))
            printNext(node.next)
        printNext(self.head)
        return self.head, self.tail

    def printInReverseOrder(self):  # Edit this function
        """Prints the values of the class in reverse order using recursive calls
        :paramete:
            self.head: The head of the singly linked list
        :returns:
        """
        def printReverse(node):
            if node == self.head:
                printReverse(node.next)
                print(str(node.data))
            elif node:
                printReverse(node.next)
                print(str(node.data), " => ", end='')
        printReverse(self.head)

    def reverseList(self):  # Edit this function
        """Reverse the linked list *in place* using recursion."""
        def reverseRecursion(node):
            if node is not self.head:
                self.append(self.delete_first_node())
                reverseRecursion(node.next)
        reverseRecursion(self.head)
        return self.printInOrder()


class Stack:  # Edit this class
    def __init__(self):
        self.list = SinglyLinkedList()  # A linked list to be used
        self.count = 0  # the number of elements

    # Insert a new element into the stack 
    # i.e just insert a new element at the beginning of the linked list.
    def push(self, data):
        self.list.prepend(data)
        self.count += 1

    # Remove the top element from the stack
    # i.e just delete and return an element
    # at the beginning of the linked list
    # if the list is not empty
    def pop(self):
        if self.count > 0:
            self.count -= 1
            return self.list.delete_first_node()

    # Returns the top element of the stack if the list is not empty
    def top(self):
        if self.count:
            return self.list.head.data

    # Prints out the stack
    def printStack(self):
        def printNextStack(node=self.list.head):
            if node is None:
                return
            # Print to the console
            if node.next is not None:
                print(str(node.data), " <= ", end='')
            else:
                print(str(node.data))
            printNextStack(node.next)
        printNextStack()


class Queue:  # Edit this class
    def __init__(self):
        self.list = SinglyLinkedList()
        self.count = 0  # the number of elements

    def enqueue(self, data):
        # Insert a new element into the queue
        # i.e just insert a new element at the end of the linked list.
        self.count += 1
        return self.list.append(data)

    def dequeue(self):
        # Remove the front element from the queue
        # i.e just delete and return an element
        # at the beginning of the linked list
        # if the list is not empty
        if self.count >= 1:
            self.count -= 1
            return self.list.delete_first_node()

    def front(self):
        # Returns the top element of the stack if the list is not empty
        if self.count >= 1:
            return self.list.head.data

    def printQueue(self):   # Prints out the queue
        def printNextQueue(node=self.list.head):
            if node is None:
                return
            # Print to the console
            if node.next is not None:
                print(str(node.data), " <= ", end='')
            else:
                print(str(node.data))
            printNextQueue(node.next)
        printNextQueue()


# Only run this code if it is called directly from the command line
# This prevents other runs of the code from printing to the console.
# For example, this if statement prevents pydoc from running the code
if __name__ == "__main__":
    # The following codes are given for
    # the example of the use of the linked list.
    # You must modify the following codes to implement
    # a menu driven user interface at the command line

    # Implement a Singly Linked List
    words = SinglyLinkedList()
    words.append('egg')
    words.append('ham')
    words.append('spam')
    words.prepend('egg2')
    words.prepend('ham2')
    words.prepend('spam2')
    words.printInReverseOrder()

    # Implement a stack using a Singly Linked List
    wordStack = Stack()
    wordStack.push("egg")
    wordStack.push("ham")
    wordStack.push("spam")
    wordStack.push("egg2")
    wordStack.push("ham2")
    wordStack.push("spam2")
    wordStack.printStack()

    # Implement a Queue using a Singly Linked List
    wordQueue = Queue()
    wordQueue.enqueue("egg")
    wordQueue.enqueue("ham")
    wordQueue.enqueue("spam")
    wordQueue.enqueue("egg2")
    wordQueue.enqueue("ham2")
    wordQueue.enqueue("spam2")
    wordQueue.printQueue()

    print('')
    print(f'\ndeleted-first: {words.delete_first_node()}')
    words.printInOrder()

    print(f'\ndeleted-last: {words.delete_last_node()}')
    words.printInOrder()
