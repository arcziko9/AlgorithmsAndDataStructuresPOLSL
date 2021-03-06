# KOLEJKA
# Sprawdzenie czy kolejka jest pełna
# Sprawdzanie czy kolejka jest pusta
# Usunięcie pierwszego elementu z kolejki
# Dodanie elementu na końcu kolejki

capacity = 10

class Queue:
    def __init__(self):
        self.capacity = capacity
        self.items = [None] * self.capacity
        self.size = 0
        self.front = 0
        self.rear = 0

    def __str__(self):
        return str(self.items[self.front:] + [None] * self.front)

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        if not self.is_full():
            self.items[self.rear] = item
            self.rear = int((self.rear + 1) % self.capacity)
            self.size += 1
        else:
            print('Queue is full')

    def dequeue(self):
        if not self.is_empty():
            print(self.items[self.front], 'is removed')
            self.front = int((self.front + 1) % self.capacity)
            self.size -= 1
        else:
            print('Queue is empty')


q = Queue()

q.enqueue(2)
q.enqueue(4)
q.enqueue(7)
q.enqueue(45)
q.enqueue(-43)
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
q.enqueue(12)
print(q)
q.enqueue(23)
print(q)