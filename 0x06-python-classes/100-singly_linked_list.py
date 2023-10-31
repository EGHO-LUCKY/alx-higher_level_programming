#!/usr/bin/python3
"""This is a module on list classes"""


class Node:
    """This is a node class"""
    def __init__(self, data, next_node=None):
        """Initializes a Node object.

        Args:
            data (int): node data
            next_node (Node): node object.

        """
        self.data = data
        self.next_node = next_node

    @property
    """Gets the Node data"""
    def data(self):
        return self.__data

    @data.setter
    """Sets the Node data"""
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    """Gets the next node"""
    def next_node(self):
        return self.__next_node

    @next_node.setter
    """Sets the next node"""
    def next_node(self, value):
        if not isinstance(value, Node) and (value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list class"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct
        sorted position in the list (increasing order)
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """String representation of the Singly linked list class
        """
        printlist = []
        tmp = self.__head

        while tmp is not None:
            printlist.append(str(tmp.data))
            tmp = tmp.next_node
        return ("\n".join(printlist))
