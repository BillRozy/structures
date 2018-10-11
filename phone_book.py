class HashMap:

    def __init__(self, max_size=10000000):
        self.storage = ['not found'] * max_size

    def set(self, key, value):
        self.storage[key] = value
    
    def get(self, key):
        return self.storage[key]

def handle_entry(phone_book, cmd_parts):
    cmd = cmd_parts[0]
    if cmd == 'add':
        phone_book.set(int(cmd_parts[1]), cmd_parts[2])
    elif cmd == 'del':
        phone_book.set(int(cmd_parts[1]), 'not found')
    else:
        print(phone_book.get(int(cmd_parts[1])))


def main():
    phone_book = HashMap()
    n_commands = int(input())
    while n_commands:
        handle_entry(phone_book, input().split(' '))
        n_commands -= 1

main()