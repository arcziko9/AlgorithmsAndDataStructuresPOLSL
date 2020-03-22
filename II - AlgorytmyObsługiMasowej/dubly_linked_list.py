class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
          self.head = None

    #push
    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

    #append
    def append(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return

    #print
    def listprint(self, node):
        while (node is not None):
            print(node.data),
            last = node
            node = node.next

list = doubly_linked_list()
list.push(121)
list.append(39)
list.push(81)
list.push(26)
list.append(445)
list.listprint(list.head)