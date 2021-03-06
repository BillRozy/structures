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

    def print(self):
        res = []
        target = self._head
        while target:
            res.append(target.value)
            target = target.nxt
        print('LIST({}) IS: '.format(self._size), *res)

# def test():
#     lst = CustomLinkedList()
#     lst.append(21)
#     lst.append(22, 0)
#     lst.unshift(16)
#     assert lst.remove() == 22
#     assert lst.shift() == 16
#     lst.append(30)
#     lst.append(41, 0)
#     assert lst.shift() == 21
#     assert lst.shift() == 41
#     assert lst.remove() == 30

# test()




