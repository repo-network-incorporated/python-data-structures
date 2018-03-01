class Node(object):
    def __init__(self, data, next = None):
        self.next = next
        self.data = data

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    def insert(self, data):
        new_head = Node(data, self.head)
        self.head = new_head

    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node


    def is_empty(self):
        return self.head == None
