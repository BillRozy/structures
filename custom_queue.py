from custom_linked_list import CustomLinkedList

class CustomQueue:

    def __init__(self):
        self.linked_list = CustomLinkedList()

    def enqueue(self, elem):
        self.linked_list.unshift(elem)

    def dequeue(self):
        return self.linked_list.remove()

    def empty(self):
        return self.linked_list.empty()

    def size(self):
        return self.linked_list._size()
