class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    #returns the node at a given position
    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    #insert new node into a given position in linked list
    def insert(self, new_node, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_node.next = current.next
                    current.next = new_node
                current = current.next
                counter += 1
        elif position == 1:
            new_node.next = self.head
            self.head = new_node

    #delete node with given value from linked list
    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def isEmpty(self):
        return self.head == None


myList = LinkedList()
myList.append(77)
print(myList.isEmpty())