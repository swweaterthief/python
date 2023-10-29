class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if self.tail is None and self.head is None:
            self.tail = self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            removed_node = self.head
            self.head = removed_node.next
            if self.head is not None:
                self.head.prev = None
            if removed_node == self.tail:
                self.tail = None
            return removed_node.data