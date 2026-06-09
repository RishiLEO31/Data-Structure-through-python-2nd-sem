# Double linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node
    
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                return
            current_node = current_node.next
    
    def display(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(current_node.data)
            current_node = current_node.next
        print(" -> ".join(nodes))

# Example usage
if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.append("A")
    dll.append("B")
    dll.append("C")
    dll.display()  # Output: A -> B -> C
    dll.prepend("D")
    dll.display()  # Output: D -> A -> B -> C
    dll.delete("B")
    dll.display()  # Output: D -> A -> C
