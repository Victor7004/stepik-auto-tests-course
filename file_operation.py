sd ={}
rule = {'read': 'R', 'write': 'W', 'execute': 'X'}
for _ in range(int(input())):
    k, *v = input().split()
    sd[k] = v

for _ in range(int(input())):
    k, v = input().split()
    print('OK' if rule[k] in sd[v] else 'Access denied')
