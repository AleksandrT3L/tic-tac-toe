import random

board = list(range(1,10))
winning_combos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
x = []
o = []


# Прорисовка доски
def create_board():
    print("-" * 12)
    for i in range(3):
        print(f"| {board[0+i*3]} | {board[1+i*3]} | {board[2+i*3]} |")
        print("-" * 12)


# Ход живого игрока (крестик или нолик)
def step(letter):
    check_number_in_lists = True
    while check_number_in_lists:
        number = int(input(f"На какую позицию вы хотите поставить {letter}?\n"))
        if number not in o and number not in x:
            board[number - 1] = letter
            if letter == "X":
                x.append(number)
            else:
                o.append(number)
            check_number_in_lists = False
        else:
            print("Эта клетка занята!")


# Ход компьютера
def computer_step():
    check_computer_number_in_lists = True
    while check_computer_number_in_lists:
        rand_number = random.randint(1, 9)
        if rand_number not in o and rand_number not in x:
            check_computer_number_in_lists = False
    return rand_number


# Проверка на условие победы
def check_winner(letter):
    check = 0
    for list in winning_combos:
        if letter == "X":
            result = all(elem in x for elem in list)
            if result:
                check += 1
        else:
            result = all(elem in o for elem in list)
            if result:
                check += 1
    if check != 0:
        return True


player_or_computer = input("С кем вы ходите сыграть: Игрок/Компьютер\n").lower()
step_count = 0
game = True
while game:
    create_board()
    step_count += 1
    if step_count == 1 or step_count % 2 == 1:
        step(letter="X")
    else:
        if player_or_computer == "компьютер":
            computer_number = computer_step()
            board[computer_number - 1] = "O"
            o.append(computer_number)
        else:
            step(letter="O")

    if step_count >=5 and step_count % 2 == 1:
        if check_winner(letter="X"):
            print("Первый игрок победил!")
            create_board()
            game = False
    elif step_count >=5 and step_count % 2 == 0:
        if check_winner(letter="O"):
            print("Второй игрок победил!")
            create_board()
            game = False
