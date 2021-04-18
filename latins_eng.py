lat_eng = {}

for i in range(int(input())):
    eng, lats = input().split(' - ')
    for lat in lats.split(', '):
        lat_eng[lat] = lat_eng.get(lat,[]) + [eng]

print(len(lat_eng))
for lat, eng in sorted(lat_eng.items()):
    print(f"{lat} - {', '.join(eng)}")