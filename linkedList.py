from node import Node

class LinkedList:
    def __init__(self, items=None):
        self.head = None
        self.tail = None
        self.length = 0
        
        if items is not None:
            # Check if items is an iterable (and not a string)
            if hasattr(items, '__iter__') and not isinstance(items, (str, bytes)):
                for value in items:
                    self.append(value)
            else:
                self.append(items)

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        # 1. Empty list case
        if self.length == 0:
            return None

        # 2. Single-node case
        if self.head == self.tail:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return popped_node 
        
        # 3. Multiple-node case
        temp = self.head
        prev = None
        while temp.next is not None:
            prev = temp
            temp = temp.next

        prev.next = None
        self.tail = prev
        self.length -= 1

        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        
        if self.head == self.tail:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return popped_node
        
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        self.length -= 1
        return popped_node

my = LinkedList()
my.print_list()
print('after')
my.pop_first()
my.print_list()        

