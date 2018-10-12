from functools import lru_cache
from collections import deque

class HashSet:

    p = 1000000007
    x = 263   # num of ascii

    @staticmethod
    @lru_cache(maxsize=500000)
    def pow_x_p(order):
        return pow(HashSet.x, order, HashSet.p)

    @staticmethod
    def calc_ord(char, order):
        res = (HashSet.pow_x_p(order) * ord(char) % HashSet.p) % HashSet.p
        return res

    @staticmethod
    def hash(string):
        m = len(string)
        res_num = 0
        for i, char in enumerate(string):
            res_num = (res_num % HashSet.p + HashSet.calc_ord(char, i) % HashSet.p) % HashSet.p
        return res_num


def Rabin_Karp_Matcher(text, pattern):
    n = len(text)
    m = len(pattern)
    hashes_count = n - m + 1
    pattern_hash = HashSet.hash(pattern)
    hashes = [float('inf')] * hashes_count
    result = deque([])
    for s in range(hashes_count - 1, -1, -1):
        if s == hashes_count - 1:
            hashes[s] = HashSet.hash(text[s: s + m])
        else:
            effect_of_removed_letter = HashSet.calc_ord(text[s + m], m - 1)
            hashes[s] = ((hashes[s + 1] % HashSet.p - effect_of_removed_letter % HashSet.p) * HashSet.x) % HashSet.p
            effect_of_added_letter = HashSet.calc_ord(text[s], 0)
            hashes[s] = (hashes[s] % HashSet.p + effect_of_added_letter % HashSet.p) % HashSet.p
        if pattern_hash == hashes[s]: 
            if pattern == text[s: s + m]:
                result.appendleft(s)
    return result


def main():
    pattern = input()
    text = input()
    print(*Rabin_Karp_Matcher(text, pattern))

main()
