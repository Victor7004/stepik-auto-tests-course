#Операции на множества
a = {12, 13, 14, 15}
#длина множества
print(len(a))
#нахождение элемента в множестве
print(12 in a, 7 in a)
#нахождение пересечений множеств
b = {1, 2, 3, 4}
c = {3, 4, 5, 6}
d = {10,11, 12}
print(b & c)
print(b & d)
#объединение множеств
print(b | c)
print(c.union(d))
#задача нахождения пересичений двух множеств и вывода отсортированного результата
print(*sorted(set(input().split()) & set(input().split())))
