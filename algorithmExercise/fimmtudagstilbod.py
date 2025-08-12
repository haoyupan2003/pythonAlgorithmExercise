# https: // open.kattis.com/problems/fimmtudagstilbod

y = int(input().strip())
price = 1000 + max(0, y - 2020) * 100
print(price)
