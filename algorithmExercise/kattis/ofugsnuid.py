# https://open.kattis.com/problems/ofugsnuid

n = int(input())

result = [0] * n

for i in range(n):
    result[i] = input()

print("\n".join(i for i in result[::-1]))
