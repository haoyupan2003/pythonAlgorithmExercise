# https://open.kattis.com/problems/cosmicpathoptimization

n = int(input())
temps = list(map(int, input().split()))
print(sum(temps) // n)
