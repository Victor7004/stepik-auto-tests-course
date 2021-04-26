def is_ancestor(child, parent):
    if child == parent:
        return True
    if child not in edges:
        return False
    return is_ancestor(edges[child], parent)    

edges = dict(input().split() for _ in range(int(input()) - 1))
for _ in range(int(input())):
    child, parent = input().split()
    answer = 0
    if is_ancestor(child, parent):
        answer = 2
    elif is_ancestor(parent, child):
        answer = 1
    print(answer, end=' ')  