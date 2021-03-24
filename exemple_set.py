#создание множества
a = {1, 2, 3, 1, 2, 3, 1, 2, 3, 4}
print(a, type(a))
b = {'hi', 'ha', 'hi', 'ha', 'hi', 'ho', 'hi', 'ho',}
print(b, type(b))
c = set('abracadabra')
print(c)
d = set([1, 2, 3, 4])
print(d)
e = set(range(5))
print(e)
#создание пустого множества
f = set()
print(f, type(f))
h = {}
print(h)
#исключение из списка дублирующих элементов
k = [1, 2, 3, 4, 1, 2, 3]
k = list(set(k))
print(k)
#добавление элемента в множество
s = {22, 33, 44, 33}
s.add(55)
s.update([5, 7, 33])
s.update('hello')
s.update(range(5, 10))
print(s)
#методы удаления элемента из множества
v = {1, 2, 3, 4, 5}
v.discard(4)
print(v)
print(v.pop())
v.clear()
print(v)