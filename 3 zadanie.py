def a(k, l):
    if (k + l) % 2 == 0:
        return "белый"
    else:
        return "чёрный"


def b(figure, k, l, m, n):
    if figure == "ферзь" or figure == "ладья":
        if k == m or l == n:
            return True
    if figure == "ферзь" or figure == "слон":
        if abs(k - m) == abs(l - n):
            return True
    if figure == "конь":
        if (abs(k - m) == 2 and abs(l - n) == 1) or (abs(k - m) == 1 and abs(l - n) == 2):
            return True
    return False

def c(figure, k, l, m, n):
    if figure == "ладья":
        if k == m or l == n:
            return True
    if figure == "ферзь":
        if k == m or l == n or abs(k - m) == abs(l - n):
            return True
    if figure == "слон":
        if abs(k - m) == abs(l - n):
            return True
    return False

def d(figure, k, l, m, n):
    if figure == "слон":
        for i in range(1, 9):
            for j in range(1, 9):
                if abs(k - i) == abs(l - j) and abs(i - m) == abs(j - n):
                    return True
        return False
    else:
        return False

def e(figure, k, l, m, n):
    for i in range(1, 9):
        for j in range(1, 9):
            if c(figure, k, l, i, j) and c(figure, i, j, m, n):
                return i, j
    return None

def f(coord):
    letters = ['А', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    letter = letters[coord[1] - 1]
    return f"{letter}{coord[0]}"
print("Введите координаты первого поля (k, l):")
k = int(input())
l = int(input())
print("Введите координаты второго поля (m, n):")
m = int(input())
n = int(input())

# Условие для полей
while k >= 9 or l >= 9 or m >= 9 or n >= 9:
    print("Введенные данные должны быть числами меньше или равными 8.")
    k = int(input("Введите номер вертикали для первого поля: "))
    l = int(input("Введите номер горизонтали для первого поля: "))
    m = int(input("Введите номер вертикали для второго поля: "))
    n = int(input("Введите номер горизонтали для второго поля: "))

# Проверяем цвета шахматных полей
color1 = a(k, l)
color2 = a(m, n)
print("Цвет первого поля:", color1)
print("Цвет второго поля:", color2)

if color1 == color2:
    print("Поля", f((k, l)), "и", f((m, n)), "имеют одинаковый цвет.")
else:
    print("Поля", f((k, l)), "и", f((m, n)), "имеют разный цвет.")

print("Введите фигуру (ферзь, ладья, слон или конь):")
figure = input()

if b(figure, k, l, m, n):
    print("Фигура угрожает полю", f((m, n)), ".")
else:
    print("Фигура не угрожает полю", f((m, n)), ".")

if c(figure, k, l, m, n):
    print("Фигура", figure, "может попасть на поле", f((m, n)), "одним ходом.")
elif d(figure, k, l, m, n):
    next_move = e(figure, k, l, m, n)
    if next_move:
        print("Фигура", figure, "может попасть на поле", f((m, n)), "за два хода.")
        print("Следующий ход:", f(next_move))
    else:
        print("Фигура", figure, "не может попасть на поле", f((m, n)), "за два хода.")