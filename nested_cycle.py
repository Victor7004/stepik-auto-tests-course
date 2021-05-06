a = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 21]]
#print(len(a))
#print(a[2])
#print(a[2][3])
#print(a[0][3])
#print(a[2][2][3])
b = ['hello', 'Hi', 'world']
#print(b[2])
#print(b[2][0])
for i in a:# обход списка по значению без возможности изменить элементы списка;
    for j in i:
        print(j, end=' ')
    print()
print(a)

for i in range(3):# обход списка по индексу и возможностью изменить элементы списка
    for j in range(4):
        a[i][j] += 10
        print (a[i][j], end=' ')
    print()
print(a)

for j in range(4):#обходим список по столбцам
    for i in range(3):
        print(a[i][j], end=' ')
    print()

for i in range(2, -1, -1):#обходим список по индексу с право на лево
    for j in range(3, -1, -1):
        print(a[i][j], end=' ')
    print()

#сумма по каждой строчке
for i in range(3):
    s = 0
    for j in range(4):
        s += a[i][j]
    print(s)

#сумма по столбцам
for j in range(4):
    s = 0
    for i in range(3):
        s += a[i][j]
    print(s)





