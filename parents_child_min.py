h = dict(input().split() for _ in range(int(input()) - 1))
for _ in range(int(input())):
    e = []
    a, b = input().split() 
    while a in h and a not in e:
        e.append(a)
        a = h[a]
    while b in h and b not in e:
        e.append(b)
        b = h[b]
    print(b) 