#!/usr/bin/python3
"""Creates a Node object"""


class Node:
    """Creates a Node object"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value 

"""Creates a Singly Linked List object"""


class SinglyLinkedList:
    """Creates a Singly Linked List object"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a node in sorted position"""
        runner = self.__head
        prev = runner
        if runner is None:
            self.__head = Node(value)
            return

        if runner.data > value:
            self.__head = Node(value, runner)
            return

        while runner is not None and runner.data < value:
            prev = runner
            runner = runner.next_node

        prev.next_node = Node(value, runner)

    def liststr(self):
        """Prints the list"""
        res = []
        runner = self.__head
        if runner is None:
            return ""
        while runner is not None:
            res.append(str(runner.data))
            if runner.next_node is not None:
                res.append("\n")
            runner = runner.next_node
        return ("".join(res))

    def __str__(self):
        """String representation of list"""
        return (self.liststr())
