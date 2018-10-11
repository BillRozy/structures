from collections import deque
class HashSet:

    p = 1000000007
    x = 263

    @staticmethod
    def hash(string, m):
        res_num = 0
        for i, char in enumerate(string):
            res_num += (ord(char) * pow(HashSet.x, i, HashSet.p)) 
        return res_num % HashSet.p % m

    def __init__(self, max_size=10000000):
        self.max_size = max_size
        self.storage = [deque([]) for i in range(0, max_size)]

    def add(self, key):
        if not self.contains(key):
            self.storage[HashSet.hash(key, self.max_size)].appendleft(key)

    def contains(self, key):
        try:
            self.storage[HashSet.hash(key, self.max_size)].index(key)
            return True
        except ValueError:
            return False
            
    def remove(self, key):
        try:
            self.storage[HashSet.hash(key, self.max_size)].remove(key)
        except:
            pass
    
    def check(self, i):
        return ' '.join(self.storage[i])

def handle_entry(hash_set, cmd_parts):
    cmd = cmd_parts[0]
    if cmd == 'add':
        hash_set.add(cmd_parts[1])
    elif cmd == 'del':
        hash_set.remove(cmd_parts[1])
    elif cmd == 'find':
        print('yes' if hash_set.contains(cmd_parts[1]) else 'no')
    else:
        print(hash_set.check(int(cmd_parts[1])))




def main():
    m, n = int(input()), int(input())
    hash_set = HashSet(m)
    while n:
        handle_entry(hash_set, input().split(' '))
        n -= 1

main()