#!/usr/bin/python3
""" Singly linked list"""


class Node:
    """defines a node of a singly linked list"""

    def __init__(self, data, next_node=None) -> None:
        """ initializer"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """ setter"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ setter"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ singly linked list class"""

    def __init__(self):
        """ initialization"""
        self.head = None

    def __str__(self):
        """ make list printable"""
        all_data = ""
        tmp = self.head
        while (tmp):
            all_data += str(tmp.data) + "\n"
            tmp = tmp.next_node
        # return all data except the new line at the end
        return all_data[:-1]

    def sorted_insert(self, value):
        """ insert into correct sorted position"""
        NewNode = Node(value)
        temp = self.head
        if temp is None:
            self.head = NewNode
            return
        if value < temp.data:
            NewNode.next_node = self.head
            self.head = NewNode
            return

        while (temp.next_node and temp.next_node.data < value):
            temp = temp.next_node
        NewNode.next_node = temp.next_node
        temp.next_node = NewNode
