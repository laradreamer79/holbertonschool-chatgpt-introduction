#!/usr/bin/env python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 5)


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


def board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid position. Choose values between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


tic_tac_toe()

