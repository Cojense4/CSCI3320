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


def printInReverseOrder(list):  # Edit this function
    """Print the values of a linked list in reverse order using only recursion"""

    pass


def reverseList(list):  # Edit this function
    """Reverse the linked list *in place* using recursion."""

    pass


class Stack:   # Edit this class
 
    def __init__(self): 
        self.list = SinglyLinkedList()   # A linked list to be used
        self.count = 0                   # the number of elements
 
 
    # Insert a new element into the stack 
    # i.e just insert a new element at the beginning of the linked list.
    def push(self, data):
 
        pass


    # Remove the top element from the stack
    # i.e just delete and return an element
    # at the beginning of the linked list
    # if the list is not empty
    def pop(self):
 
        pass

 
    # Returns the top element of the stack if the list is not empty
    def top(self):
 
        pass

 
    # Prints out the stack
    def printStack(self):

        pass


class Queue:   # Edit this class
 
    def __init__(self): 
        self.list = SinglyLinkedList()   # A linked list to be used
        self.count = 0                   # the number of elements
 
    # Insert a new element into the queue 
    # i.e just insert a new element at the end of the linked list.
    def enqueue(self, data):
 
        pass


    # Remove the front element from the queue
    # i.e just delete and return an element 
    # at the beginning of the linked list
    # if the list is not empty
    def dequeue(self):
 
        pass

 
    # Returns the top element of the stack if the list is not empty
    def front(self):
 
        pass
 

    # Prints out the queue
    def printQueue(self):

        pass





# Only run this code if it is called directly from the command line
# This prevents other runs of the code from printing to the console.
# For example, this if statement prevents pydoc from running the code
if __name__ == "__main__":            

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