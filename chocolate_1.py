n, m, k = int(input()), int(input()), int(input())
#ветвление условий
if k < n * m and ((k % n == 0) or ( k % m == 0)):
    print('YES')
else:
    print('NO')
