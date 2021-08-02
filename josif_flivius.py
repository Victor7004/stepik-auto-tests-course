kol_voinov = int(input())
kakogo_ubivat = int(input())


tolpa = [i for i in range(1, kol_voinov +1)]
current_pos = 0
step = 0
while len(tolpa) > 1:
    step += 1
    if step == kakogo_ubivat:
        step = 0
        del tolpa[current_pos]
    else:
        current_pos += 1
    if current_pos == len(tolpa):
        current_pos = 0
print(tolpa[0])
