matrix_0 = [[" . "," . "," . "],
            [" . "," . "," . "],
             [" . "," . "," . "]]
def Vision():
    print("   0  1  2")
    for i in range (3):
     print(F"{i} {matrix_0[i][0]}{matrix_0[i][1]}{matrix_0[i][2]}")
    return Vision
Vision()
print("__________")
player_1 = str(input(" Введите имя первого игрока: ").title())
print(player_1+" Вы играете за Х")
player_2 = str(input(" Введите имя второго игрока: ").title())
print(player_2+" Вы играете за 0")

def moves():
    while True:
        x, y = map(int, input(" введите координаты через пробел(вводите ТОЛЬКО цифры от 0 до 2) : ").split())

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты не верны,вводите аккуратней :) ")
            continue
        if matrix_0[x][y] != " . ":
            print(" Поле уже занято!!! ")
            continue

        return x, y
def win():
    if matrix_0[0][0] == " X " and matrix_0[0][1] == " X " and matrix_0[0][2] == " X ":
        print(player_1 + " Вы победили! Поздравляем!!!")
        return True
    if matrix_0[1][0] == " X " and matrix_0[1][1] == " X " and matrix_0[1][2] == " X ":
        print(player_1 + " Вы победили! Поздравляем!!!")
        return True
    if matrix_0[2][0] == " X " and matrix_0[2][1] == " X " and matrix_0[2][2] == " X ":
        print(player_1+" Вы победили! Поздравляем!!!")
        return True
    if matrix_0[0][2] == " X " and matrix_0[1][1] == " X " and matrix_0[2][0] == " X ":
        print(player_1 + " Вы победили! Поздравляем!!!")
        return True
    if matrix_0[0][0] == " X " and matrix_0[1][1] == " X " and matrix_0[2][2] == " X ":
        print(player_1 + " Вы победили! Поздравляем!!!")
        return True
    if matrix_0[0][0] == " X " and matrix_0[1][0] == " X " and matrix_0[2][0] == " X ":
        print(player_1 + " Вы победили! Поздравляем!!!")
        return True
    if matrix_0[0][1] == " X " and matrix_0[1][1] == " X " and matrix_0[2][1] == " X ":
        print(player_1 + " Вы победили! Поздравляем!!!")
        return True
    if matrix_0[0][2] == " X " and matrix_0[1][2] == " X " and matrix_0[2][2] == " X ":
        print(player_1 + " Вы победили! Поздравляем!!!")
        return True
    if matrix_0[0][0] == " 0 " and matrix_0[0][1] == " 0 " and matrix_0[0][2] == " 0 ":
        print(player_2 + " Вы победили! Поздравляем!!!")
        return True
    if matrix_0[1][0] == " 0 " and matrix_0[1][1] == " 0 " and matrix_0[1][2] == " 0 ":
        print(player_2 + " Вы победили! Поздравляем!!!")
        return True
    if matrix_0[2][0] == " 0 " and matrix_0[2][1] == " 0 " and matrix_0[2][2] == " 0 ":
        print(player_2 + " Вы победили! Поздравляем!!!")
        return True
    if matrix_0[0][2] == " 0 " and matrix_0[1][1] == " 0 " and matrix_0[2][0] == " 0 ":
        print(player_2 + " Вы победили! Поздравляем!!!")
        return True
    if matrix_0[0][0] == " 0 " and matrix_0[1][1] == " 0 " and matrix_0[2][2] == " 0 ":
        print(player_2 + " Вы победили! Поздравляем!!!")
        return True
    if matrix_0[0][0] == " 0 " and matrix_0[1][0] == " 0 " and matrix_0[2][0] == " 0 ":
        print(player_2 + " Вы победили! Поздравляем!!!")
        return True
    if matrix_0[0][1] == " 0 " and matrix_0[1][1] == " 0 " and matrix_0[2][1] == " 0 ":
        print(player_2 + " Вы победили! Поздравляем!!!")
        return True
    if matrix_0[0][2] == " 0 " and matrix_0[1][2] == " 0 " and matrix_0[2][2] == " 0 ":
        print(player_2 + " Вы победили! Поздравляем!!!")
        return True
summa = 0
while True:
    summa += 1
    Vision()
    if summa % 2 == 1:
        print(" Ходит  "+player_1)
    else:
        print(" Ходит "+player_2)
    x, y = moves()
    if summa % 2 == 1:
        matrix_0[x][y] = " X "

    else:
        matrix_0[x][y] = " 0 "
    if summa == 9:
         print(" 'Боевая' ничья!")
         break
    if win():
         break
Vision()