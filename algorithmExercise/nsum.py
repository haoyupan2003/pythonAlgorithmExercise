# https://open.kattis.com/problems/nsum

n = int(input())
list = input().split()
result = 0

for i in range(n):
    result += int(list[i])

print(result)


# Advanced:
# n = int(input())
# print(sum(map(int, input().split())))

# map is commonly used to apply a function to each element of a list, array, or any iterable (e.g., tuples, strings, or even a generator).
# map(function, iterable)
