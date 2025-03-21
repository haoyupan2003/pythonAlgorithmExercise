# https://open.kattis.com/problems/aldur

n = int(input())

array = []

for i in range(n):
    array.append(int(input()))

array.sort()

print(array[0])
