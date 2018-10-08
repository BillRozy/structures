import heapq
from collections import deque


def spread_to_procs(tasks, n_procs):
    time = 0
    tasks_in_progress = []
    free_processors = [[i, 0] for i in range(0, n_procs)]
    busy_processors = deque([])
    heapq.heapify(free_processors)
    for index, task in enumerate(tasks):
        # print('Handling task num={}, dur={}'.format(index, task))
        # print('Fre procs is {}, busy procs={},  tasks={}'.format(free_processors, busy_processors, tasks_in_progress))
        if not free_processors:
            next_proc_need = busy_processors[-1][1]  # heapq.heappop(tasks_in_progress)
            # print('Task to remote time = {}'.format(next_proc_need))
            elapsed = 0
            while busy_processors and busy_processors[-1][1] <= next_proc_need:
                proc = busy_processors.pop()
                elapsed = proc[1]
                proc[1] = 0
                heapq.heappush(free_processors, proc)
            for proc in busy_processors:
                proc[1] -= elapsed
            time += elapsed
        if task == 0:
            print(free_processors[0][0], time)
        else:
            proc = heapq.heappop(free_processors)
            print(proc[0], time)
            heapq.heappush(tasks_in_progress, task)
            proc[1] = task
            busy_processors.appendleft(proc)


def main():
    n_procs, m_tasks = list(map(int, input().split(' ')))
    tasks_durations = list(map(int, input().split(' ')))
    spread_to_procs(tasks_durations, n_procs)

main()