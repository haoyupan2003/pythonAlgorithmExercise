# https://open.kattis.com/problems/catinabox

h, w, l, v = map(int, input().split())

box_volume = h * w * l

if v > box_volume:
    print("TOO TIGHT")
elif v == box_volume:
    print("COZY")
else:
    print("SO MUCH SPACE")
