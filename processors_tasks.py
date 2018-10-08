import heapq
from collections import deque


def spread_to_procs(tasks, n_procs):
    time = 0
    processors = [[0, i] for i in range(0, n_procs)]
    heapq.heapify(processors)
    for task in tasks:
        if processors[0][0] > time:
            next_proc = heapq.heappop(processors)
            wiil_be_free_at = next_proc[0]
            print(next_proc[1], wiil_be_free_at)
            next_proc[0] = wiil_be_free_at + task
            heapq.heappush(processors, next_proc)
            time = wiil_be_free_at
        else:
            if task == 0:
                print(processors[0][1], time)
            else:
                proc = heapq.heappop(processors)
                free_at = proc[0]
                print(proc[1], proc[0])
                proc[0] = time + task
                heapq.heappush(processors, proc)
                time = free_at


def main():
    n_procs, m_tasks = list(map(int, input().split(' ')))
    tasks_durations = list(map(int, input().split(' ')))
    spread_to_procs(tasks_durations, n_procs)

try:
    main()
except Exception as e:
    print(e)