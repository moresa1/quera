a, b, l = map(int, input().split())

smr = 0

if l % 2 == 0:
    smr = (a * (l / 2)) + (b * (l / 2))
    print(int(smr))
else:
    l = l - 1
    smr = (a * (l / 2) + a) + (b * (l / 2))
    print(int(smr))