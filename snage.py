 n = int(input())
a = [['.' for _ in range(n)] for _ in range(n)]
for i in range(n):
    a[i][i] = '*'
    a[i][- i + n - 1] = '*'
    a[i][n // 2] = '*'
    a[n // 2][i] = '*'

for i in range(n):
    print(*a[i], sep = ' ')