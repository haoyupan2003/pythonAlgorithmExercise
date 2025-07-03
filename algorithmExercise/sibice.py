# https://open.kattis.com/problems/sibice

import math

n, w, h = map(int, input().split())
max_length = math.sqrt(w**2 + h**2)

for _ in range(n):
    match_length = int(input())
    if match_length <= max_length:
        print("DA")
    else:
        print("NE")
