moves = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

def print_board():
    print(" {n1} | {n2} | {n3} \n___|___|___\n {n4} | {n5} | {n6} \n___|___|___\n {n7} | {n8} | {n9} \n   |   |   ".
          format(n1=moves[1], n2=moves[2], n3=moves[3], n4=moves[4], n5=moves[5],
                 n6=moves[6], n7=moves[7], n8=moves[8], n9=moves[9]))


def wait_for_next_move(turn):
    move = int(input("{turn} Player, please type in your next move position in the board: ".format(turn=turn)))
    while not 0 < move < 10 and not move.isdigit() and moves[move] != " ":
        move = input("Invalid input! Please try typing in something else: ")
    else:
        if turn == "First":
            moves[move] = "X"
            turn = "Second"
        else:
            moves[move] = "Y"
            turn = "First"
        print_board()


def is_there_a_winner():
    for v in moves.values():
        if v is " ":
            break
    else:
        return False # Tie! There is no winner.
    if (moves[1] == moves[2] == moves[3]
        or moves[4] == moves[5] == moves[6]
        or moves[7] == moves[8] == moves[9]
        or moves[1] == moves[4] == moves[7]
        or moves[2] == moves[5] == moves[8]
        or moves[3] == moves[6] == moves[9]
        or moves[5] == moves[1] == moves[9]
        or moves[3] == moves[5] == moves[7]):
        return True # We have a winner!
    return None # No one won yet.


print_board()
turn = "First"
wait_for_next_move(turn)
while is_there_a_winner() is None:
    wait_for_next_move(turn)
else:
    if is_there_a_winner is True:
        print("The {turn} Player won the game!".format(turn=turn))
    else:
        print("There was a tie!")
 