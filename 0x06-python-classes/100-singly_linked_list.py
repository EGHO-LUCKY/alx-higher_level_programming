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
    def data(self):
        """Gets the Node data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the Node value"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Sets next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets next node"""
        if not isinstance(value, Node) and (value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list class"""
    def __init__(self):
        """Initializes a singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
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
