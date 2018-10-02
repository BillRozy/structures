from custom_queue import CustomQueue
import numpy

class Processor:

    def __init__(self, capacity):
        self.buffer = CustomQueue()
        self.capacity = capacity
        self.real_time = 0
        self.ticks_to_work = 0
        self.handled = []

    def free(self):
        return self.ticks_to_work == 0

    def tick(self):
        if self.free():
            if not self.buffer.empty():
                self.handle_packet(self.buffer.dequeue())
        self.ticks_to_work -= 1


    def time_update(self, time):
        if self.ticks_to_work <= (time - self.real_time):
            self.ticks_to_work = 0
        else:
            self.ticks_to_work = self.ticks_to_work - (time - self.real_time)
        self.real_time = time

    def handle_packet(self, packet):
        arrival, duration = packet
        self.time_update(arrival)
        if self.buffer.size() >= self.capacity:
            self.handled.append(-1)

        if self.free():
            self.ticks_to_work += duration
            handled.append((packet, self.real_time))




def net_buffer(packets, buf_size):
    result = []
    buffer = CustomQueue()
    processor_busy = 0
    current_time = 0
    prev_time = 0
    for packet in packets:
        arrival, duration = packet
        prev_time = current_time
        current_time = arrival
        processor_busy = 0 if processor_busy <= (current_time - prev_time) else processor_busy - (current_time - prev_time)
        if buffer.size() >= buf_size:
            result.append(-1)
            continue
        buffer.enqueue(packet)
        if processor_busy == 0:
            result.append(current_time)
            processor_busy = duration
            continue

        buffer.enqueue(packet)
    while not buffer.empty():
        arrival, duration = packet
        


def main():
    buf_size, n_packets = list(map(input().split(' ')))
    while n_packets > 0:
        arrival, duration = list(map(input().split(' ')))
        n_packets -= 1

def test():
    assert net_buffer([(0, 0)], 1) == 0
    assert net_buffer([(0, 1)], 1) == 0
    assert numpy.array_equal(net_buffer([(0, 1), (0, 1)], 1), [0, -1])
    assert numpy.array_equal(net_buffer([(0, 1), (1, 1)], 1), [0, 1])