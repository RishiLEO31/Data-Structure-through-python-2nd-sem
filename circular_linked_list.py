# Circular linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        last_node.next = new_node
        new_node.next = self.head
    
    def print_list(self):
        if not self.head:
            return
        current_node = self.head
        while True:
            print(current_node.data, end=' ')
            current_node = current_node.next
            if current_node == self.head:
                break
        print()
# Example usage
circular_linked_list = CircularLinkedList()
circular_linked_list.append(10)
circular_linked_list.append(20)
circular_linked_list.append(30)
print("Circular linked list contents:")
circular_linked_list.print_list()
