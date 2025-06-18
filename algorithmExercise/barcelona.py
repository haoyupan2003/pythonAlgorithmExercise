# https://open.kattis.com/problems/barcelona

n, b = map(int, input().split())

bags = list(map(int, input().split()))

index = bags.index(b)

if index == 0:
    print("fyrst")
elif index == 1:
    print("naestfyrst")
else:
    print(f"{index} fyrst")
