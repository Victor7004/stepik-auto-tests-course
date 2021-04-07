s = input()
t = s.split()
d = {}
for w in t:
    d[w] = d.get(w, 0) + 1
    print(d[w] - 1 , end = ' ')
#counter = {}
#for word in input().split():
    #counter[word] = counter.get(word, 0) + 1
    #print(counter[word] - 1, end=' ')