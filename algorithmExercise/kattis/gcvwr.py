# https://open.kattis.com/problems/gcvwr

GCVWR, truck_weight, n = map(int, input().split())
items = list(map(int, input().split()))

towing_capacity = GCVWR - truck_weight
allowed_capacity = int(towing_capacity * 0.9)
items_total_weight = sum(items)

max_trailer_weight = allowed_capacity - items_total_weight
print(max_trailer_weight)
