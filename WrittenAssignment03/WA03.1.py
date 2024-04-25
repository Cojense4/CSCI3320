class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.next_val = None
        self.size = 0


# a
def compareLength(list1, list2):
    # The worst case complexity (Big-O) of this function is O(n)
    # This is because the only non O(1) processes are findLength calls which each take O(len(list) == n) processes each
    """
    Compares the length of two SinglyLinkedList objects
    :param list1: first SinglyLinkedList object
    :param list2: second SinglyLinkedList object
    :return int: 1 if (list1 > list2), -1 if (list1 < list2), else 0
    """
    def findLength(list0):
        """
        Finds the length of a singly linked list
        :param list0: SinglyLinkedList object
        :return int: length of list0
        """
        list_length = 0
        next_val = list0.head
        while next_val:
            list_length += 1
            next_val = next_val.next
        return list_length

    list1_length = findLength(list1)
    list2_length = findLength(list2)

    if list1_length > list2_length:
        return 1
    elif list1_length < list2_length:
        return -1
    else:
        return 0


# part b
def equal_list(list1, list2):
    # The worst-case complexity (Big-O) of this function is O(n) This is because compareLength() function is O(n) and
    # dict_creator() takes O(len(list0) == n) processes This complexity is due in part to the builtin dict.get()
    # function which is a constant time operation, which may have lowered the worst-case complexity
    """
    Checks if two SinglyLinkedList objects are equal
    :param list1: first SinglyLinkedList object
    :param list2: second SinglyLinkedList object
    :return bool: False if equal, True otherwise:
    """
    def dict_creator(list0, list_dict):
        """
        Creates dictionary from list0
        :param list0: SinglyLinkedList object
        :param list_dict: empty dictionary object
        :return dict: completed list_dict object
        """
        next_val = list0.head
        while next_val:
            list_dict[next_val.data] = list_dict.get(next_val.data, 0) + 1
            next_val = next_val.next
        return list_dict

    if compareLength(list1, list2) != 0:
        return True
    else:
        return dict_creator(list1, {}) != dict_creator(list2, {})

