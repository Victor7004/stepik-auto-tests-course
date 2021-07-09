weight = float(input())
height = float(input())
bmi = weight / (height**2)
print("Недостаточная масса" if bmi < 18.5 else "Избыточная масса" if bmi > 25 else "Оптимальная масса")

# Более классический вариант нахождения индекса массы тела :
#m, h = float(input()), float(input())
#imt =m/h/h
#if imt < 18.5:
    #print('Недостаточная масса')
#elif imt > 25:
    #print('Избыточная масса')
#else:
    print('Оптимальная масса')
