moves = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}


def print_board(moves):
    for i in moves:
        if i == 1:
            print(" {value} |".format(value=i))
        if i == 2:
            print(" {value} ".format(value=i))
    print("_" * 3 + "|" + "_" * 3 + "|" + "_" * 3)
    print("_" * 3 + "|" + "_" * 3 + "|" + "_" * 3)
    print(" " * 3 + "|" + " " * 3 + "|" + " " * 3)


def wait_for_next_move(move, turn):
    while not 0 < move < 10 and not move.isdigit():
        move = input("Invalid input. Try something between 1 and 9! Type in your next move position in the board!")
    else:
        if turn == "first":
            moves[move] = "X"
            turn = "second"
        else:
            moves[move] = "Y"
            turn = "first"


def winner(move):
    # TODO check if all values are X or Y (tie!)
    # for(v in moves.values()):
    #	if v != "X" and v != "Y"
    print(move)
    if (moves[1] == moves[2] == moves[3] == move
        or moves[4] == moves[5] == moves[6] == move
        or moves[7] == moves[8] == moves[9] == move
        or moves[1] == moves[4] == moves[7] == move
        or moves[2] == moves[5] == moves[8] == move
        or moves[3] == moves[6] == moves[9] == move
        or moves[5] == moves[1] == moves[9] == move
        or moves[3] == moves[5] == moves[7] == move):
        return move
    return None


print_board(moves)
turn = "first"
move = int(input("Type in your next move position in the board!"))
while winner(move) is None:
    wait_for_next_move(move, turn)
