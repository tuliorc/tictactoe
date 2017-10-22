import os


def print_board():
    os.system('clear')  # clears terminal from previous printed rounds
    print(
        " {n1} | {n2} | {n3} \n___|___|___\n {n4} | {n5} | {n6} \n___|___|___"
        "\n {n7} | {n8} | {n9} \n   |   |   ".format(n1=moves[1], n2=moves[2],
                                                     n3=moves[3], n4=moves[4],
                                                     n5=moves[5], n6=moves[6],
                                                     n7=moves[7], n8=moves[8],
                                                     n9=moves[9]))


def wait_for_next_move():
    global turn
    move = input(
        "{turn} Player, please type in your next move position in the board: ".
            format(turn=turn))
    while True:
        if not move.isdigit():
            move = input("Invalid input! Please try typing in a number: ")
            continue
        move = int(move)
        if not 0 < move < 10 or moves.get(move, None) is not " ":
            move = input(
                "Invalid input! Please try typing in another number: ")
            continue
        break

    if turn == "First":
        moves[move] = "X"
        turn = "Second"
    else:
        moves[move] = "O"
        turn = "First"
    print_board()


def is_there_a_winner():
    if moves[1] == moves[2] == moves[3] != " " or moves[4] == moves[5] == \
       moves[6] != " " or moves[7] == moves[8] == moves[9] != " " or \
       moves[1] == moves[4] == moves[7] != " " or moves[2] == moves[5] == \
       moves[8] != " " or moves[3] == moves[6] == moves[9] != " " or \
       moves[1] == moves[5] == moves[9] != " " or moves[3] == moves[5] == \
       moves[7] != " ":
        return True  # We have a winner!

    for v in moves.values():
        if v is " ":
            break
    else:
        return False  # Tie! There is no winner.

    return None  # No one won yet.


def print_scores(quit=None):
    if quit == "quit":
        print("THE FINAL RESULT IS: ")
    print("________SCORE_________\n"
          "|Player 1: {player1} victories| \n"
          "|Player 2: {player2} victories| \n"
          "______________________".format(player1=player1, player2=player2))


def start_game():
    global moves, player1, player2, turn
    for key in moves.keys():
        moves[key] = " "
    turn = "First"
    print_board()
    wait_for_next_move()
    while is_there_a_winner() is None:
        wait_for_next_move()
    else:
        if is_there_a_winner() is True:
            if turn == "Second":
                winner = "First"
                player1 += 1
            else:
                winner = "Second"
                player2 += 1
            print("The {winner} Player won the game!".format(winner=winner))
        else:
            print("There was a tie!")
        print_scores()

        again = input(
            "Do you wanna play again? Type in 'YES' to do so or anything "
            "else to leave the input mode: ")
        if again == "yes" or again == "YES":
            start_game()
        else:
            print_scores("quit")
            exit()


player1 = 0
player2 = 0
moves = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ",
         7: " ", 8: " ", 9: " "}
start_game()
