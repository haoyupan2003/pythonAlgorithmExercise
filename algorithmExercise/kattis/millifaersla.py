# https://open.kattis.com/problems/millifaersla

my_dict = {
    int(input()): "Monnei",
    int(input()): "Fjee",
    int(input()): "Dolladollabilljoll"
}

sorted_items = sorted(my_dict.items())

print(sorted_items[0][1])
