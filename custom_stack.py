from custom_linked_list import CustomLinkedList
class CustomStack:

    def __init__(self):
        self.linked_list = CustomLinkedList()
    
    def push(self, element):
        self.linked_list.unshift(element)

    def pop(self):
        return self.linked_list.shift()

    def top(self):
        return self.linked_list.head()

    def size(self):
        return self.linked_list._size()

    def empty(self):
        return self.linked_list.empty()

def test():
    stack = CustomStack()
    stack.push(10)
    stack.push(100)
    stack.push(1000)
    assert stack.top() == 1000
    assert stack.pop() == 1000
    assert stack.pop() == 100
    stack.push(1)
    assert stack.pop() == 1
    assert stack.pop() == 10
    assert stack.empty() == True

test()
