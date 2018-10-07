class Heap:

    MAX_HEAP = 0
    MIN_HEAP = 1

    def __init__(self, array=[], heap_type=MAX_HEAP, max_size=100000000):
        self.size = len(array)
        self.heap_type = heap_type
        self.max_size = max_size
        self.buffer = array or [0] * max_size
        self.swaps = []

    def _l_child(self, i):
        return 2 * i + 1

    def _r_child(self, i):
        return 2 * i + 2

    def _parent(self, i):
        return (i - 1) // 2

    def should_sift_up(self, child, parent):
        if self.heap_type == Heap.MAX_HEAP:
            return self.buffer[child] > self.buffer[parent]
        return self.buffer[child] < self.buffer[parent]

    def should_sift_down(self, child, parent):
        if self.heap_type == Heap.MAX_HEAP:
            return self.buffer[parent] < self.buffer[child]
        return self.buffer[parent] > self.buffer[child]

    def _sift_down_child_selector(self, child1, child2):
        if child2 > self.size - 1:
            return child1
        if self.heap_type == Heap.MAX_HEAP:
            if self.buffer[child1] > self.buffer[child2]:
                return child1
            return child2
        else:
            if self.buffer[child1] < self.buffer[child2]:
                return child1
            return child2
    
    def has_childs(self, i):
        return self._l_child(i) < self.size or self._r_child(i) < self.size
        

    def _sift_up(self, i):
        while i > 0 and self.should_sift_up(i, self._parent(i)):
            self.buffer[i], self.buffer[self._parent(i)] = self.buffer[self._parent(i)], self.buffer[i] 
            print('sifted up: ', self._parent(i), i)
            i = self._parent(i)

    def _sift_down(self, i):
        while i <= (self.size - 1) // 2 and self.has_childs(i):
            lc = self._l_child(i)
            rc = self._r_child(i)

            selected_child = self._sift_down_child_selector(lc, rc)
            if self.should_sift_down(selected_child, i):
                self.swaps.append((i, selected_child))
                self.buffer[selected_child], self.buffer[i] = self.buffer[i], self.buffer[selected_child]
            i = selected_child
    
    def insert(self, val):
        self.size += 1
        self.buffer[self.size - 1] = val
        self._sift_up(self.size - 1)

    def extract_root(self):
        mx = self.buffer[0]
        self.buffer[0] = self.buffer[self.size - 1]
        self.size -= 1
        self._sift_down(0)
        return mx

    def remove(self, i):
        self.change_priority(i, float('-inf') if self.heap_type else  float('inf') )
        return self.extract_root()
    
    def change_priority(self, i, val):
        prev = self.buffer[i]
        self.buffer[i] = val
        if prev > val:
            self._sift_down(i)
        else:
            self._sift_up(i)

    @classmethod
    def heapify(cls, array, h_type=MAX_HEAP):
        heap = Heap(array, heap_type=h_type)
        i = len(array) // 2
        while i >= 0:
            heap._sift_down(i)
            i -= 1
        return heap

def heap_sort(array):
    ar_size = len(array)
    as_heap = Heap.heapify(array, Heap.MIN_HEAP)
    # print(as_heap.buffer)
    # for i in range(0, len(array) - 1):
    #     print('swap:', array[0], array[as_heap.size - 1])
    #     array[0], array[as_heap.size - 1] = array[as_heap.size - 1], array[0]
    #     as_heap.size -= 1
    #     as_heap._sift_down(0)
    #     print('on step', i, array)

def main():
    n = int(input())
    array = list(map(int, input().split(' ')))
    heap = Heap.heapify(array, Heap.MIN_HEAP)
    print(len(heap.swaps))
    for swap in heap.swaps:
        print(*swap)

# def test():
#     inp = [7, 6, 5, 4, 3, 2]
#     inp2 = [0, 1, 2, 3, 4, 5]
#     heap = Heap.heapify(inp2, Heap.MIN_HEAP)
#     print(len(heap.swaps))
#     for swap in heap.swaps:
#         print(*swap)

main()