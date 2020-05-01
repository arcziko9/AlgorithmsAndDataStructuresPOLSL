class Stack:
    def __init__(self):
        self.Stack = []

    def __str__(self):
        if self.isEmpty():
            return "Stos jest pusty"
        else:
            return str(self.Stack)

    def Push(self, s):
        self.Stack.append(s)

    def Pop(self):
        self.Stack.pop(len(self.Stack) - 1)

    def Size(self):
        return len(self.Stack)

    def Top(self):
        return self.Stack[len(self.Stack) - 1]

    def isEmpty(self):
        if len(self.Stack) == 0:
            return True
        else:
            return False
