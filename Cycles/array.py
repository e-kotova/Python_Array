# 1.Программа получает на вход натуральное число N (2 ≤ N ≤100, N - четное).
# Выведите на экран таблицу размером NxN, верхняя половина которой заполнена 1, а нижняя 0.

n = int(input())
for i in range(n):
    for j in range(n):
        if i == 0 or i == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()

# 2.Программа получает на вход натуральное число N (2 ≤ N ≤100, N - четное).
# Выведите на экран таблицу размером NxN, верхняя четверть заполнена 1, а все остальные элементы 0.

n = int(input())
for i in range(n):
    for j in range(n):
        if (i == 0 and j == 0) or (i == 1 and j == 0) or (i == 0 and j == 1) or (i == 1 and j == 1):
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()

# 3.Программа получает на вход натуральное число N (3 ≤ N ≤100, N - нечетное).
# Выведите на экран таблицу размером NxN, средний столбец и средняя строка которой заполнены единицами,
# все остальные элементы нули.

n = int(input())
a = [['0'] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][n // 2] = '1'
        a[n // 2][j] = '1'
for lenght in a:
    print(*lenght)

# 4.Программа получает на вход натуральное число N (1 ≤ N ≤100).
# Выведите на экран таблицу размером NxN, в которой на главной диагонали стоят 1,
# а все остальные места заполнен 0.
n = int(input())
a = [['0'] * n for i in range(n)]
for i in range(n):
    for j in range(0, i):
        a[i][j] = '0'
    a[i][i] = '1'
    for j in range(i + 1, n):
        a[i][j] = '0'
for lenght in a:
    print(*lenght)

# 5.Программа получает на вход натуральное число N (1 ≤ N ≤100).
# Выведите на экран таблицу размером NxN, в которой на главной
# диагонали и ниже стоят 1, а все остальные 0
n = int(input())
a = [['0'] * n for i in range(n)]
for i in range(n):
    for j in range(0, i):
        a[i][j] = '1'
    a[i][i] = '1'
    for j in range(i + 1, n):
        a[i][j] = '0'
for lenght in a:
    print(*lenght)

# 6.Программа получает на вход натуральное число N (2 ≤ N ≤100, N - четное).
# Выведите на экран таблицу размером NxN, нижний угол первой четверти которой
# заполнен единицами, а все остальные элементы нулями.

n = int(input())
a = [['0'] * n for i in range(n)]
for i in range(n):
    for j in range(0, i):
        a[i][j] = '1'
    a[i][i] = '1'
    for j in range(i + 1, n):
        a[i][j] = '0'
for lenght in a:
    print(*lenght)
