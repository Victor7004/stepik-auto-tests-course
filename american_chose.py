#пример сортировки числа по американскому стандарту
d = {}#создаем словарь
for i in range(int(input())):
    a = input().split()
    if a[0] not in d:
        d[a[0]] = int(a[1])
    else:
        d[a[0]] += int(a[1])
        
        
for key , value in sorted(d.items()):
    print(key, value)
