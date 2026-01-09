# https://open.kattis.com/problems/ratingproblems

n, k = map(int, input().split())
ratings = [int(input()) for _ in range(k)]

current_sum = sum(ratings)
remaining = n - k

min_total = current_sum + remaining * (-3)
max_total = current_sum + remaining * 3

min_avg = min_total / n
max_avg = max_total / n

print(f"{min_avg:.10f} {max_avg:.10f}")
