# https://open.kattis.com/problems/grafaholur

w1 = int(input())
h1 = int(input())
v1 = int(input())
w2 = int(input())
v2 = int(input())

t2 = h1 * w1 * v2 / (w2 * v1)
print(f"{t2:.15f}")
