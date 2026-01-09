# https://open.kattis.com/problems/biladlyklabord

import sys

s = sys.stdin.readline().rstrip('\n')
out = []
prev = None
for ch in s:
    if ch != prev:
        out.append(ch)
    prev = ch
print(''.join(out))
