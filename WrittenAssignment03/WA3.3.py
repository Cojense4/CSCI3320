
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    # Do Not Add Any Changes to the SinglyLinkedList class
    def __init__(self):
        self.head = None
        self.tail = None

    # Checks if the list is empty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def prepend(self, data): # Do not edit this function
        # Encapsulate the data in a Node
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def append(self, data): # Do not edit this function
        # Encapsulate the data in a Node
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def delete_first_node (self): # Do not edit this function
        current = self.head
        if self.head is None:
            print("No data element to delete")
            return None
        elif current == self.head:
            self.head = current.next
            return current.data

    def delete_last_node (self): # Do not edit this function
        current = self.head
        prev = self.head
        if self.head is None:
            print("No data element to delete")
            return None
        while current:
            if current.next is None:
                prev.next = current.next
                self.tail = prev
                return current.data
            prev = current
            current = current.next


class Stack:
    """FIFO (first in first out) methods to manipulate a SinglyLinkedList() object"""
    def __init__(self):
        self.list = SinglyLinkedList()
        self.count = 0

    def push(self, data):
        """
        DESCRIPTION:
            Inserts a new element on top of the stack
        Complexity:
            Since this method only inserts an element to it's linked list, no matter the size of the data,
            it will take a linear amount of time to complete, thus the complexity is O(1)
        """
        self.list.prepend(data)
        self.count += 1

    def pop(self):
        """
        DESCRIPTION:
            Removes and returns the element at the top of the stack if list isn't empty
        Complexity:
            Since this method only returns (and removes) an element, no matter the size of the data,
            it will take a linear amount of time to complete, thus the complexity is O(1)
        Returns
            top data after removing it from the stack
        """
        if self.count > 0:
            self.count -= 1
            return self.list.delete_first_node()

    def top(self):
        """
        DESCRIPTION:
            Returns the top element of the stack if the list is not empty
        Complexity:
            Since this method only returns the top element, the complexity is O(1)
        Returns
            top data
        """
        if self.count:
            return self.list.head.data

    def printStack(self):
        """
        Description:
            Prints out the stack using recursion, first item printed is the top
        Print Example
            if stack is [top, mid, bottom] where first element is top of the list then...
            "top <= mid <= bottom"
        """
        def printNextStack(node=self.list.head):
            if node is None:
                return
            if node.next is not None:
                print(str(node.data), " <= ", end='')
            else:
                print(str(node.data))
            printNextStack(node.next)
        printNextStack()


# Big-O is O(n == len(queue))
class TwoStackQueue:
    """FILO (First In Last Out) methods to manipulate two Stack() objects"""
    def __init__(self):
        self.stack_head = Stack()
        self.stack_body = Stack()
        self.count = 0

    def front(self):
        """
        DESCRIPTION:
            Returns the first element in the queue given queue isn't empty
        Complexity:
            Since this method only returns the front element, the complexity is O(1)
        Returns
            front data
        """
        if self.stack_body.count >= 1:
            return self.stack_body.top()
        elif self.stack_head.count >= 1:
            return self.stack_head.top()
        else:
            return "Queue is empty"

    def enqueue(self, data):
        """
        DESCRIPTION:
            Inserts a new element to the end of the queue
        Complexity:
            Since this method only appends an element to it's linked stack, no matter the size of the data,
            it will take a linear amount of time to complete, thus the complexity is O(1)
        """
        self.stack_body.push(data)
        self.count += 1

    def dequeue(self):
        """
        DESCRIPTION:
            Removes and returns the first element in the queue given queue isn't empty
        Complexity:
            In the worst case scenario, this method will have to pop all elements from stack_body and push them into stack_head.
            This function has the worst case time complexity of O(n), where n is the number of elements in the queue.
        Returns:
             first element data after removing it from the queue
        """
        if self.count >= 1:
            # If stack_head is empty, pop all elements from stack_body and push them into stack_head
            if self.stack_head.count == 0:
                while self.stack_body.count > 0:
                    self.stack_head.push(self.stack_body.pop())
            self.count -= 1
            return self.stack_head.pop()
        else:
            return "Queue is empty"


    def printQueue(self):
        """Prints out the queue using recursion, first item printed is the front"""
        print("Printing stack_head:")
        self.stack_head.printStack()
        print("Printing stack_body:")
        self.stack_body.printStack()


def main():
    # Create a Queue object
    queue = TwoStackQueue()

    # Enqueue some elements
    queue.enqueue("Apple")
    queue.enqueue("Banana")
    queue.enqueue("Cherry")

    # Print the queue
    queue.printQueue()

    # Print the front element
    print("Front element is: " + queue.front())

    # Dequeue some elements
    print("Dequeued element: " + queue.dequeue())
    print("Dequeued element: " + queue.dequeue())

    # Print the queue
    queue.printQueue()

    # Print the front element
    print("Front element is: " + queue.front())


if __name__ == "__main__":
    main()
