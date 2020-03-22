class Node:
    #wezel listy dwukierunkowej

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class DoubleList:
    #lista dwukierunkowa

    def __init__(self):
        self.length = 0
        self.nil = Node()   # <-------- wartownik
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def is_empty(self):
        # return self.length == 0
        return self.nil.next == self.nil

    def count(self):
        return self.length

    def insert_head(self, node):
        node.next = self.nil.next
        node.prev = self.nil
        self.nil.next.prev = node
        self.nil.next = node
        self.length += 1

    def insert_tail(self, node):
        node.next = self.nil
        node.prev = self.nil.prev
        self.nil.prev.next = node
        self.nil.prev = node
        self.length += 1

    def remove_head(self):   # zwraca node
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.nil.next
        # Teraz ogólny schemat usuwania węzła.
        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1
        return node

    def remove_tail(self):   # zwraca node
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.nil.prev
        # Teraz ogólny schemat usuwania węzła.
        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1
        return node