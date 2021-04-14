sd = {}
for _ in range(int(input())):
    for v in input().split():
        sd[v] = sd.get(v, 0) - 1

print(*(k for k, _ in sorted(sd.items(), key=lambda x: x[::-1])), sep='\n')