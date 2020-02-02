class Stack:
    def __init__(self):
        self.items = []

    #check if stack is empty
    def isEmpty(self):
        return self.items == []

    #add value to top of stack
    def push(self, item):
        self.items.append(item)

    #return and delete top value of stack
    def pop(self):
        return self.items.pop()

    #return top value of stack
    def peek(self):
        return self.items[len(self.items)-1]

    #get size of stack
    def size(self):
        return len(self.items)