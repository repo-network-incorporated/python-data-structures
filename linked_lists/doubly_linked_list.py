class Node(object):
    def __init__(self, data, previous = None, next = None):
        self.data = data
        self.previous = previous
        self.next = next


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.__increment_size()
            return
        
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next
        
        new_node.previous = current_node
        current_node.next = new_node

        self.__increment_size()
    
    def insert(self, data):
        new_node = Node(data)

        if self.head is not None:
            existing_node = self.head
            existing_node.previous = new_node
            new_node.next = existing_node

        self.head = new_node
        self.__increment_size()

    def find(self, data):
        if self.is_empty():
            return None

        current_node = self.head

        while current_node is not None:
            if current_node.data == data:
                return current_node
            
            current_node = current_node.next
        return None
    
    def get(self, index):
        if index >= self.size or index < 0:
            raise IndexError()

        current_node = self.head

        for i in range(index):
            current_node = current_node.next

        return current_node

    def is_empty(self):
        return self.head is None
    
    def __increment_size(self):
        self.size += 1

    def __decrement_size(self):
        self.size -= 1
