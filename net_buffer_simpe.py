from collections import deque

def net_buffer(packets, buf_size):
    buffer = deque([], buf_size)
    handled = [-1 for i in range(0, len(packets))]
    time = 0
    for packet in packets:
        print("Arrived: ", packet)
        num, arrived, duration = packet
        while time < arrived:
            try:
                head = buffer[-1]
                n, a, d = head
                head_started_at = handled[n]
                if head_started_at == -1:
                    handled[n] = time
                if arrived >= head_started_at + d:
                    time = head_started_at + d
                    print("Finished:", buffer.pop())
            except:
                time = arrived
        try:
            if len(buffer) == 0:
                handled[num] = time
            buffer.appendleft(packet)
        except:
            handled[num] = -1
    return handled
        


def main():
    buf_size, n_packets = list(map(int, input().split(' ')))
    packets = []
    i = 0
    while i < n_packets:
        packets.append([i, *list(map(int, input().split(' ')))])
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