import sys
sd = {}

for i in sys.stdin:
    k, t, v = i.split()
    sd[k][t] = sd.setdefault(k, {}).setdefault(t, 0) + int(v)

for a in sorted(sd):
    print(a + ':')
    for b in sorted(sd[a].items()):
        print(*b)