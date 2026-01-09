# https://open.kattis.com/problems/aterriblefortress

n = int(input())

total_blazes = 0

for _ in range(n):
    blaze_count = int(input())
    total_blazes += blaze_count

print(total_blazes)
