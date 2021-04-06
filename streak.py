n, k = input().split()
n = int(n) + 1
year = [i for i in range(0, n)]
week = [i for i in range(0, n) if i%7==0 or (i+1)%7==0]

temp = list()
for _ in range(int(k)):
    start, interval = input().split()
    temp += year[int(start)::int(interval)]

print(len(set(temp) - set(week))) 