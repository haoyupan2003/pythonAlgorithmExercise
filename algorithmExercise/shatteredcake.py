# https://open.kattis.com/problems/shatteredcake

import sys

W = int(sys.stdin.readline())
N = int(sys.stdin.readline())
total_area = 0
for _ in range(N):
    w, l = map(int, sys.stdin.readline().split())
    total_area += w * l
print(total_area // W)
