class PriorityQueue:
    def __init__(self):
        self.PQueue = []

    def __str__(self):
        if self.isEmpty():
            return "Kolejka jest pusta"
        else:
            return str(self.PQueue)

    def isEmpty(self):
        if len(self.PQueue) == 0:
            return True
        else:
            return False

    def Front(self):
        return self.PQueue[0]

    def Size(self):
        return len(self.PQueue)

    def Push(self, end, priority):
        if not self.isEmpty():
            for i in range(len(self.PQueue)):
                if self.PQueue[i][1] > priority:
                    self.PQueue.insert(i, (end, priority))
                    break
                elif self.PQueue[i][1] == priority:
                    if self.PQueue[i][0] > end:
                        self.PQueue.insert(i, (end, priority))
                        break
                    elif self.PQueue[i][0] == end:
                        print("Taki element już istnieje")
                        break
                elif i == len(self.PQueue) - 1:
                    self.PQueue.append((end, priority))
        else:
            self.PQueue.append((end, priority))

    def Pop(self):
        if self.isEmpty():
            return print("Kolejka jest pusta")
        else:
            self.PQueue.pop(len(self.PQueue) - 1)


q = PriorityQueue()

q.Push('el1', 3)
q.Push('el2', 1)
q.Push('el3', 5)
q.Push('el4', 7)
q.Push('el5', 2)
print(q)