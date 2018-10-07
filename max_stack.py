from collections import deque
from sys import stdin

class MaxStack:

    def __init__(self):
        self.stack = deque([])
        self.max_lvl = deque([])

    def push(self, elem):
        self.stack.append(elem)
        self.max_lvl.append(elem if elem > self.max() else self.max())

    def pop(self):
        self.max_lvl.pop()
        return self.stack.pop()

    def max(self):
        if self.max_lvl:
            return self.max_lvl[-1]
        return 0

def input_handler(n_cmds):
    stack = MaxStack()
    while n_cmds:
        command = stdin.readline()
        if command.startswith('max'):
            print(stack.max())
        elif command.startswith('pop'):
            stack.pop()
        else:
            cmd, elm = command.split(' ')
            stack.push(int(elm))
        n_cmds -= 1

def main():
    n = int(stdin.readline())
    input_handler(n)

main()
