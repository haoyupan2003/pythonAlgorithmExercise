# https://open.kattis.com/problems/reversebinary

n = int(input())
b = bin(n)[2:]
r = b[::-1]
print(int(r, 2))
