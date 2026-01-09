# https://open.kattis.com/problems/lastfactorialdigit

import math

t = int(input())
for _ in range(t):
    x = int(input())
    print(math.factorial(x) % 10)
