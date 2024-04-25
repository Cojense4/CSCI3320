"""
Programming assignment file for CSCI3320
The University of Nebraska at Omaha
"""

#
# The following clasess should not be edited in this assignment
# (except including the manupulation of the self.tail pointer).
# Look below for the comment with "Start Assignment"
# to see the code that needs to be edited
#

class Node:
    """ A singly-linked node. """
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    # Do Not Add Any Changes to the SinglyLinkedList class
    def __init__ (self):
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

def printInOrder(list):  # Do not edit this function
    """Start an in-order printing of node items for the given list"""
    # Recurse starting with the head node
    printNext(list.head)

def printNext(node):  # Do not edit this function
    """If the node is valid, print the given node and then continue to recurse"""
    # Stopping condition
    if node == None:
        return

    # Print to the console
    if node.next != None:
        print(str(node.data), " => ", end='')
    else:
        print(str(node.data))

    # Recursion     
    printNext(node.next)


#
# Start assignment
# The following functions need to be updated for this assignment
#
def printInReverseOrder(singleLL):
    """Print the values of a linked singleLL in reverse order using only recursion"""
    def printReverse(node):
        if node == singleLL.head:
            printReverse(node.next)
            print(str(node.data))
        elif node:
            printReverse(node.next)
            print(str(node.data), " => ", end='')

    printReverse(singleLL.head)


def reverseList(singleLL):
    """Reverse the singly linked list *in place* using recursion."""
    def reverseRecursion(node, prev=None):
        if not node:
            return prev
        next_node = node.next
        node.next = prev
        return reverseRecursion(next_node, node)
    singleLL.head = reverseRecursion(singleLL.head)

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


class Queue:
    """FILO (First In Last Out) methods to manipulate a SinglyLinkedList() object"""
    def __init__(self):
        self.list = SinglyLinkedList()
        self.count = 0

    def enqueue(self, data):
        """
        DESCRIPTION:
            Inserts a new element to the end of the queue
        Complexity:
            Since this method only appends an element to it's linked list, no matter the size of the data,
            it will take a linear amount of time to complete, thus the complexity is O(1)
        """
        self.list.append(data)
        self.count += 1

    def dequeue(self):
        """
        DESCRIPTION:
            Removes and returns the first element in the queue given queue isn't empty
        Complexity:
            Since this method only returns (and removes) an element, no matter the size of the data,
            it will take a linear amount of time to complete, thus the complexity is O(1)
        Returns:
             first element data after removing it from the queue
        """
        if self.count >= 1:
            self.count -= 1
            return self.list.delete_first_node()

    def front(self):
        """
        DESCRIPTION:
            Returns the first element in the queue given queue isn't empty
        Complexity:
            Since this method only returns the front element, the complexity is O(1)
        Returns
            front data
        """
        if self.count >= 1:
            return self.list.head.data

    def printQueue(self):
        """Prints out the stack using recursion, first item printed is the top"""
        def printNextQueue(node=self.list.head):
            if node is None:
                return
            if node.next is not None:
                print(str(node.data), " <= ", end='')
            else:
                print(str(node.data))
            printNextQueue(node.next)

        printNextQueue()


def main():
    """
    Main function for assignment completion, runs through menu selection as long as 15 is not entered,
    use options list as a reference to what things the program can do
    """
    options = [
        "Enter choice [1-15] from the menu below:",
        "1)\tConstruct a list L1 with comma seperated values",
        "2)\tPrint list L1",
        "3)\tPrint list L1 in reverse",
        "4)\tReverse list L1",
        "5)\tConstruct a stack S1 with comma seperated values",
        "6)\tPrint top element in stack S1"
        "7)\tPop top element in stack S1",
        "8)\tPush element to stack S1",
        "9)\tPrint stack S1",
        "10)\tConstruct a queue Q1 with comma seperated values",
        "11)\tPrint front element in queue Q1",
        "12)\tDequeue top element in queue Q1",
        "13)\tEnqueue new element to queue Q1 ",
        "14)\tPrint queue Q1",
        "15)\tExit the program"
    ]
    option = None
    values = []
    while option != "15":
        for element in options:
            print(element)
        inputSplitBySpace = input("Enter choice (add comma seperated values if creating a list): ").split(" ")
        option = inputSplitBySpace[0]
        try:
            option = int(option)
        except ValueError:
            print(f'INVALID OPTION: {option}\n')
            continue
        if len(inputSplitBySpace) > 1:
            values = inputSplitBySpace[1:][0].split(",")

        if option == 1:
            L1 = SinglyLinkedList()
            for value in values:
                L1.append(value)
        elif option == 2:
            printInOrder(L1)
        elif option == 3:
            printInReverseOrder(L1)
        elif option == 4:
            reverseList(L1)
        elif option == 5:
            S1 = Stack()
            for value in values:
                S1.push(value)
        elif option == 6:
            print(S1.top())
        elif option == 7:
            S1.pop()
        elif option == 8:
            S1.push(values[0])
        elif option == 9:
            S1.printStack()
        elif option == 10:
            Q1 = Queue()
            for value in values:
                Q1.enqueue(value)
        elif option == 11:
            Q1.front()
        elif option == 12:
            Q1.dequeue()
        elif option == 13:
            for value in values:
                Q1.enqueue(value)
        elif option == 14:
            Q1.printQueue()


# Only run this code if it is called directly from the command line
# This prevents other runs of the code from printing to the console.
# For example, this if statement prevents pydoc from running the code
if __name__ == "__main__":
    main()
    # The following codes are given for
    # the example of the use of the linked list.
    # You must modify the following codes to implement
    # a menu driven user interface at the command line

    words = SinglyLinkedList()
    words.append('egg')
    words.append('ham')
    words.append('spam')
    words.prepend('egg2')
    words.prepend('ham2')
    words.prepend('spam2')
    printInOrder(words)

    print(f'\ndeleted-first: {words.delete_first_node()}')
    printInOrder(words)

    print(f'\ndeleted-last: {words.delete_last_node()}')
    printInOrder(words)