import os

moves = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 
         8: " ", 9: " "}


def print_board():
    os.system('cls||clear') # clears terminal from previous printed rounds
    print(" {n1} | {n2} | {n3} \n___|___|___\n {n4} | {n5} | {n6} "+
          "\n___|___|___\n {n7} | {n8} | {n9} \n   |   |   ".format(
            n1=moves[1], n2=moves[2], n3=moves[3], n4=moves[4], 
            n5=moves[5], n6=moves[6], n7=moves[7], n8=moves[8], 
            n9=moves[9]))


def wait_for_next_move():
    global turn

    move = input("{turn} Player, please type in your next move " +
                 "position in the board: ".format(turn=turn))
    while True:
        if not move.isdigit():
            move = input("Invalid input! Please try typing in " +
                         "a number: ")
            continue
        move = int(move)
        if not 0 < move < 10 or moves.get(move, None) is not " ":
            move = input("Invalid input! Please try typing in " +
                          "something else: ")
            continue
        break

    if turn == "First":
        moves[move] = "X"
        turn = "Second"
    else:
        moves[move] = "O"
        turn = "First"
    print_board()
    return move


def is_there_a_winner():
    for v in moves.values():
        if v is " ":
            break
    else:
        return False  # Tie! There is no winner.
    if moves[1] == moves[2] == moves[3] != " " or moves[4] == \
       moves[5] == moves[6] != " " or moves[7] == moves[8] == \
       moves[9] != " " or moves[1] == moves[4] == moves[7] != \
       " " or moves[2] == moves[5] == moves[8] != " " or moves[3] == \
       moves[6] == moves[9] != " " or moves[1] == moves[5] == \
       moves[9] != " " or moves[3] == moves[5] == moves[7] != " ":
        return True  # We have a winner!
    return None  # No one won yet.


print_board()
turn = "First"
move = ""
wait_for_next_move()
while is_there_a_winner() is None:
    move = wait_for_next_move()
else:
    if is_there_a_winner() is True:
        print("The {winner} Player won the game!".format(
              winner="First" if turn == "Second" else "Second"))
    else:
        print("There was a tie!")