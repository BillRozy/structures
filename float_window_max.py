from collections import deque
from math import ceil

def maxs_in_float_window(m, nums):
    res = []
    lr = [0] * len(nums)
    rl = [0] * len(nums)
    for i in range(0, ceil(len(nums) / m)):
        mm = min(m, len(nums) - i * m)
        for j in range(0, mm):
            lr[i * m + j] = max(lr[i * m + j - 1], nums[i * m + j]) if j != 0 else nums[i * m + j]
            # print('LR', lr)
            rl[i * m + (mm - j - 1)] = max(rl[i * m + (mm - j)], nums[i * m + (mm - j - 1)]) if j != 0 else nums[i * m + (mm - j - 1)]
            # print('RL', rl)
    for n in range(0, len(nums) - m + 1):
        res.append(max(rl[n], lr[n + m -1]))
    return res

def main():
    n = int(input())
    nums = list(map(int, input().split(' ')))
    m = int(input())
    print(*maxs_in_float_window(m, nums))

main()