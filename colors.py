def print_sat(same_sat):
    print(len(same_sat))
    print(*[str(i) for i in sorted(same_sat)])
N, M = [int(s) for s in input().split()]
A_color, B_color = set(), set()
for i in range (N):
    A_color.add(int(input()))
for i in range (M):
    B_color.add(int(input()))
print_sat(A_color & B_color)
print_sat(A_color - B_color)
print_sat(B_color - A_color)