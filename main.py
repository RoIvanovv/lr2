
print('Введите коэффициенты квадратного через , ')
a, b, c = map(int, input().split(','))
D = pow(b, 2) - (4 * a * c)

if D < 0:
    print('Корней нет')
elif D == 0:
    print('x = ' + str(-b / (2 * a)))
else:
    print('x_1 = ' + str((-b + pow(D, 1 / 2)) / (2 * a)))
    print('x_2 = ' + str((-b - pow(D, 1 / 2)) / (2 * a)))
