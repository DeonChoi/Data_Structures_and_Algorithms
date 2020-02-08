class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, new_element):
        self.items.append(new_element)

    def peek(self):
        return self.items[0]

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


q=Queue()	
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
print(q.isEmpty())