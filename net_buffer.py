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

class CustomQueue:

    def __init__(self):
        self.linked_list = CustomLinkedList()

    def enqueue(self, elem):
        self.linked_list.unshift(elem)

    def dequeue(self):
        return self.linked_list.remove()

    def head(self):
        return self.linked_list.tail()

    def tail(self):
        return self.linked_list.head()

    def empty(self):
        return self.linked_list.empty()

    def size(self):
        return self.linked_list._size


class Processor:

    def __init__(self, capacity):
        self.buffer = CustomQueue()
        self.capacity = capacity
        self.real_time = 0
        self.ticks_to_work = 0
        self.handled = []
        # print('Processor Inited')

    def free(self):
        return self.ticks_to_work <= 0

    def tick(self):
        # print('Tick: ', self.real_time)
        # self.buffer.linked_list.print()
        if not self.free():
            self.ticks_to_work -= 1
            if self.free():
                self.buffer.dequeue()
                # print('Finished with: ',  self.buffer.dequeue())
                if not self.buffer.empty():
                    self.handle_packet(self.buffer.head())
        else:
            if not self.buffer.empty():                
                self.handle_packet(self.buffer.head())
            

    def on_packet_arrived(self, packet):
        _id, raw_packet = packet
        arrived, duration = raw_packet
        # print("Arrived: ", packet, " , Time: ", self.real_time)
        # print('Buffer now:', self.buffer.size(), ' , Capacity: ', self.capacity)
        if self.buffer.size() >= self.capacity:
            # print('Buffer is full, throw away packet:', packet)
            self.handled.append((_id, -1))
        else:
            # print('Enquee: ', packet)
            self.buffer.enqueue(packet)
            if self.free():
                self.handle_packet(self.buffer.head())

            

    def handle_packet(self, packet):
        _id, raw_packet = packet
        arrived, duration = raw_packet
        # print("Start Handle: ", packet, " , Time: ", self.real_time)
        self.handled.append((_id, self.real_time))
        self.ticks_to_work = duration
        if duration == 0:
            self.buffer.dequeue()
            if not self.buffer.empty():
                self.handle_packet(self.buffer.head())
            # print('Finished with: ', self.buffer.dequeue())
            

    def work(self):
        while not self.buffer.empty() or self.ticks_to_work > 0:
            self.real_time += 1
            self.tick()




def net_buffer(packets, buf_size):
    proc = Processor(buf_size)
    for packet in packets:
        _id, raw_packet = packet
        arrived, duration = raw_packet
        while proc.real_time  < arrived:
            proc.real_time += 1
            proc.tick()
        proc.real_time = arrived
        proc.on_packet_arrived(packet)
    if not proc.buffer.empty():
        proc.work()
    return sorted(proc.handled, key=lambda x: x[0])
        


def main():
    buf_size, n_packets = list(map(int, input().split(' ')))
    packets = []
    i = 0
    while i < n_packets:
        packet = list(map(int, input().split(' ')))
        packets.append((i, packet))
        i += 1
    result = net_buffer(packets, buf_size)
    for it in result:
        print(it[1])

# def test():
#     assert numpy.array_equal(net_buffer([(0, 0)], 1), [0])
#     assert numpy.array_equal(net_buffer([(0, 1)], 1), [0])
#     assert numpy.array_equal(net_buffer([(0, 1), (0, 1)], 1), [0, -1])
#     assert numpy.array_equal(net_buffer([(0, 1), (1, 1)], 1), [0, 1])

main()