# STOS
# dodawanie elementu
# pobieranie i usuwanie ostatniego elementu ze stosu
# wyswietlanie ostatniego elementu
# wyswietlenie calego stosu


capacity = 10


class Stack:
    def __init__(self):
        self.capacity = capacity
        self.items = [None] * self.capacity
        self.index = 0

    def __str__(self):
        return str(self.items)

    def is_full(self):
        return self.index >= self.capacity

    def push(self, item):
        if not self.is_full():
            self.items[self.index] = item
        else:
            print('Out of range')
        self.index += 1

    def is_empty(self):
        return self.items == []

    def pop(self):
        if not self.is_empty():
            self.items[self.index - 1] = None
        else:
            print('Stack is empty')
        self.index -= 1


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
print(stack)
stack.pop()
stack.push(12)
stack.push(13)
print(stack)
stack.pop()
print(stack)
