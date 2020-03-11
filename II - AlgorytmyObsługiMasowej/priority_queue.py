capacity = 10;

class Item:

  def __init__(self, value, priority):
    self.value = value
    self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, item):
        if self.size() == 0:
            self.queue.append(item)
        else:
            for x in range(0, self.size()):
                # if the priority of new node is greater
                if item.priority >= self.queue[x].priority:
                    # if we have traversed the complete queue
                    if x == (self.size()-1):
                        # add new node at the end
                        self.queue.insert(x+1, item)
                    else:
                        continue
                else:
                    self.queue.insert(x, item)
          return True

    def delete(self):
        return self.queue.pop(0)

    def show(self):
        for x in self.queue:
            print(str(x.info) + " - " + str(x.priority))

    def size(self):
        return len(self.queue)