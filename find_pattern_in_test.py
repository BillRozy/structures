from functools import lru_cache
from collections import deque

class HashSet:

    p = 1000000007
    x = 263   # num of ascii

    @staticmethod
    @lru_cache(maxsize=500000)
    def pow_x_p(order):
        return pow(HashSet.x, order)

    @staticmethod
    def calc_ord(char, order):
        res = (ord(char) * HashSet.pow_x_p(order))
        print('hashing', char, order, ' res = ', res)
        return res

    @staticmethod
    def hash(string):
        m = len(string)
        res_num = 0
        for i, char in enumerate(string):
            res_num += HashSet.calc_ord(char, m - i - 1)
        print('hashed str=', string, 'to ', res_num)
        return res_num


def alg_rabin_carp(pattern, text):
    appearances = deque([])
    m = len(pattern)
    alg_dur = len(text) - m
    hashes = [float('inf')] * (alg_dur + 1)
    xp = pow(HashSet.x, m - 1)
    h_pattern = HashSet.hash(pattern)
    has_prev_symb = False
    for i in range(0, alg_dur + 1, 1):
        current_text_part = text[i:i + m]
        if has_prev_symb:
            curhash = hashes[i - 1]
            added_symb = ord(text[i + m - 1])
            prev_symb = HashSet.calc_ord(text[i - 1], m - 1)
            curhash = curhash - prev_symb
            print('curhash', curhash)
            print('Prev symbol={}, addedsymb={}, prevhash={}'.format(prev_symb, added_symb, hashes[i - 1]))
            print('Print correction from pattern={} to pattern={}, thrown={}, added={}'.format(text[i-1:i + m - 1], current_text_part, text[i - 1], text[i + m - 1]))
            hashes[i] = ((curhash * HashSet.x) + added_symb)
                         
        else:
            hashes[i] = HashSet.hash(current_text_part)
            has_prev_symb = True 
        if hashes[i] == h_pattern:
            if pattern == current_text_part:
                appearances.append(i)
    print(hashes)
    return appearances


def main():
    pattern = input()
    text = input()
    print(*alg_rabin_carp(pattern, text))

main()
