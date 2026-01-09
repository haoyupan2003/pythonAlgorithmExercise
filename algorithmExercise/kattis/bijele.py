# https://open.kattis.com/problems/bijele

standard = [1, 1, 2, 2, 2, 8]

mirko_pieces = list(map(int, input().split()))

difference = [standard[i] - mirko_pieces[i] for i in range(6)]

print(*difference)
