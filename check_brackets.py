class ListNode:

    def __init__(self, value, prv=None, nxt=None):
        self.value = value
        self.prv = prv
        self.nxt = nxt

class CustomLinkedList:

    def __init__(self):
        self._head = None
        self._tail = None 
        self._size = 0

    def head(self):
        return self._head.value if self._head else None
    
    def tail(self):
        return self._tail.value if self._tail else None
    
    def append(self, element, index=None):
        if index is None or index == self._size - 1:
            if self.empty():
                node = ListNode(element)
                self._head = node
                self._tail = node
            else:
                prev_tail = self._tail
                self._tail = ListNode(element, prev_tail)
                prev_tail.nxt = self._tail
        else:
            self._insert(element, index)
        
        self._size += 1

    def remove(self, index=None):
        assert not self.empty()
        elem = None
        if index is None or index == self._size - 1:
            elem = self._tail
            self._tail = elem.prv
            if self._tail:
                self._tail.nxt = None
        else:
            elem = self._remove_indexed(index)
        self._size -= 1
        self._on_null()
        return elem.value

    def unshift(self, element):
        elem = self._head
        self._head = ListNode(element, nxt=elem)
        if elem:
            elem.prv = self._head
        if self._size == 0:
            self._tail = self._head
        self._size += 1

    def shift(self):
        assert not self.empty()
        elem = self._head
        self._head = elem.nxt
        if self._head:
            self._head.prv = None
        self._size -= 1
        self._on_null()
        return elem.value

    def _insert(self, element, index):
        assert index < self._size
        start_index = 0
        target = self._head
        while start_index != index:
            target = target.nxt
            start_index += 1
        after_target = target.nxt
        node = ListNode(element, target, after_target)
        target.nxt = node
        after_target.prv = node
        

    def _remove_indexed(self, index):
        assert index < self._size
        start_index = 0
        target = self._head
        while start_index != index:
            target = target.nxt
            start_index += 1
        before_target = target.prv
        after_target = target.nxt
        before_target.nxt = after_target
        after_target.prv = before_target
        return target.value

    def _on_null(self):
        if self.empty():
            self._head = None
            self._tail = None

    def empty(self):
        return self._size == 0

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

def check_brackets(string):
    stack = CustomStack()
    count = 0
    for char in string:
        count += 1
        if char in {'(', '[', '{'}:
            stack.push((char, count))
        elif char in {')', ']', '}'}:
            if not stack.empty():
                top, c = stack.top()
                if (char == ')' and top == '(') or \
                    (char == ']' and top == '[') or \
                    (char == '}' and top == '{'):
                    stack.pop()
                else:
                    return count
            else:
                    return count
        else:
            continue
    return 'Success' if stack.empty() else stack.pop()[1]

def main():
    brackets = input()
    print(check_brackets(brackets))

def test():
    assert check_brackets('([](){([])})') == 'Success'
    assert check_brackets('()[]}') == 5
    assert check_brackets('{{[()]]') == 7

main()