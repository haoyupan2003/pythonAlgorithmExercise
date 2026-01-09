# https://open.kattis.com/problems/batterup

N = int(input())
at_bats = list(map(int, input().split()))

total_bases = 0
official_at_bats = 0

for result in at_bats:
    if result != -1:
        total_bases += result
        official_at_bats += 1

slugging_percentage = total_bases / official_at_bats
print(slugging_percentage)
