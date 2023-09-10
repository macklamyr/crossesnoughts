pole = [[" ", " ", " "] for i in range(3)]

def show():
    print("   | 0 | 1 | 2 |")
    print("----------------")
    for i, row in enumerate(pole):
        row_info: str = " | ".join(row)
        print(f"{i}  | {row_info} |")
        print("----------------")

def ask():
    while True:
        cords = input("Ваш ход: ").split()

        if len(cords) != 2:
            print("Введите 2 координаты")
            continue

        x, y = cords
        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа.")
            continue
        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Неверные координаты.")
            continue

        if pole[x][y] != " ":
            print("Клетка занята.")
            continue

        return x, y

def check_win():
    win_cords = [((0,0),(0,1),(0,2)), ((1,0),(1,1),(1,2)), ((2,0),(2,1),(2,2)),
                 ((0,0),(1,0),(2,0)), ((0,1),(1,1),(2,1)), ((0,2),(1,2),(2,2)),
                 ((0,0),(1,1),(2,2)), ((0,2),(1,1),(2,0))]
    for cords in win_cords:
        symbols = []
        for c in cords:
            symbols.append(pole[c[0]][c[1]])
            if symbols == ["X", "X", "X"]:
                print("выйграл крестик!")
                return True
            if symbols == ["O", "O", "O"]:
                print("Выйграл нолик!")
                return True
    return False

def game():
    step = 0

    show()

    while True:
        step += 1
        if step < 10:
            if step % 2 == 1:
                print("Ходит крестик")
            else:
                print("Ходит нолик")
            x, y = ask()
            if step % 2 == 1:
                pole[x][y] = "X"
            else:
                pole[x][y] = "O"
            show()
            if check_win() != False:
                break
        else:
            print("Ничья")
            break

game()

