# https://open.kattis.com/problems/equalshots

n1, n2 = map(int, input().split())


def total_alcohol(n):
    total = 0
    for _ in range(n):
        v, p = map(int, input().split())
        total += v * p
    return total


alcohol1 = total_alcohol(n1)
alcohol2 = total_alcohol(n2)

if alcohol1 == alcohol2:
    print("same")
else:
    print("different")
