from collections import deque


class Processor:

    def __init__(self, capacity, packets_len):
        self.buffer = deque([], capacity)
        self.capacity = capacity
        self.real_time = 0
        self.ticks_to_work = 0
        self.handled = [0 for i in range(0, packets_len)]
        # print('Processor Inited')
    

    def free(self):
        return self.ticks_to_work <= 0

    def tick(self, coof=1):
        # print('Tick: ', self.real_time)
        # self.buffer.linked_list.print()
        if not self.free():
            self.ticks_to_work -= coof
            if self.free():
                self.buffer.pop()
                # print('Finished with: ',  self.buffer.dequeue())
                if self.buffer:
                    self.handle_packet(self.buffer[-1])
        else:
            if self.buffer:                
                self.handle_packet(self.buffer[-1])
            

    def on_packet_arrived(self, packet):
        _id, raw_packet = packet
        arrived, duration = raw_packet
        # print("Arrived: ", packet, " , Time: ", self.real_time)
        # print('Buffer now:', self.buffer.size(), ' , Capacity: ', self.capacity)
        if len(self.buffer) < self.capacity:
            self.buffer.appendleft(packet)
            if self.free():
                self.handle_packet(self.buffer[-1])
        else:
            self.handled[_id] = -1
         

    def handle_packet(self, packet):
        _id, raw_packet = packet
        arrived, duration = raw_packet
        # print("Start Handle: ", packet, " , Time: ", self.real_time)
        self.handled[_id] = self.real_time
        self.ticks_to_work = duration
        if duration == 0:
            self.buffer.pop()
            if self.buffer:
                self.handle_packet(self.buffer[-1])
            # print('Finished with: ', self.buffer.dequeue())
            

    def work(self):
        while self.buffer or self.ticks_to_work > 0:
            if not self.buffer:
                break 
            self.real_time += self.ticks_to_work
            self.tick(self.ticks_to_work)




def net_buffer(packets, buf_size):
    proc = Processor(buf_size, len(packets))
    last_pack = float('inf')
    for packet in packets:
        _id, raw_packet = packet
        arrived, duration = raw_packet
        while proc.real_time < arrived:
            koef = 1
            # if not proc.buffer:
            #     break
            # n, p = proc.buffer[-1]
            # koef = min(proc.ticks_to_work, arrived - last_pack)
            proc.real_time += koef
            proc.tick(koef)
        proc.real_time = arrived
        proc.on_packet_arrived(packet)
        last_pack = arrived
    if proc.buffer:
        proc.work()
    return proc.handled
        


def main():
    buf_size, n_packets = list(map(int, input().split(' ')))
    packets = []
    i = 0
    while i < n_packets:
        packet = list(map(int, input().split(' ')))
        packets.append((i, packet))
        i += 1
    result = net_buffer(packets, buf_size)
    for r in result:
        print(r)

# def test():
#     assert numpy.array_equal(net_buffer([(0, 0)], 1), [0])
#     assert numpy.array_equal(net_buffer([(0, 1)], 1), [0])
#     assert numpy.array_equal(net_buffer([(0, 1), (0, 1)], 1), [0, -1])
#     assert numpy.array_equal(net_buffer([(0, 1), (1, 1)], 1), [0, 1])

main()