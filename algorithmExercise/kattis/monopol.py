# https://open.kattis.com/problems/monopol

n = int(input())
hotel_sums = set(map(int, input().split()))
ways = {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1}
count = sum(ways.get(s, 0) for s in hotel_sums)
print(count / 36)
