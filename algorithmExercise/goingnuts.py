# https://open.kattis.com/problems/goingnuts

import sys

s = sys.stdin.read().strip()
if not s:
    raise SystemExit
n = int(s)
# if n==0, zero squirrels are needed; otherwise popcount
print(bin(n).count('1'))
