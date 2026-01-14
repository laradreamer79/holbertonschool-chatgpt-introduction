#!/usr/bin/env python3
import random
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        if mines >= width * height:
            raise ValueError("Number of mines must be less than total cells.")

        self.width = width
        self.height = height
        self.mines_set = set(random.sample(range(width * height), mines))

        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def is_mine(self, x, y):
        return (y * self.width + x) in self.mines_set

    def print_board(self, reveal=False):
        clear_screen()
        print("  " + " ".join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(f"{y} ", end="")
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if self.is_mine(x, y):
                        print("*", end=" ")
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else " ", end=" ")
                else:
                    print(".", end=" ")
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue  # don't count the center cell
                nx, ny = x + dx, y + dy
                if self.in_bounds(nx, ny) and self.is_mine(nx, ny):
                    count += 1
        return count

    def reveal(self, x, y):
        if not self.in_bounds(x, y):
            return True  # ignore invalid coords without crashing

        if self.revealed[y][x]:
            return True  # already revealed

        if self.is_mine(x, y):
            return False  # hit mine

        self.revealed[y][x] = True

        if self.count_mines_nearby(x, y) == 0:
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    nx, ny = x + dx, y + dy
                    if self.in_bounds(nx, ny) and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)

        return True

    def has_won(self):
        # win if all non-mine cells are revealed
        for y in range(self.height):
            for x in range(self.width):
                if not self.is_mine(x, y) and not self.revealed[y][x]:
                    return False
        return True

    def play(self):
        while True:
            self.print_board()

            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
            except ValueError:
                input("Invalid input. Press Enter to continue...")
                continue

            if not self.in_bounds(x, y):
                input("Out of bounds. Press Enter to continue...")
                continue

            if not self.reveal(x, y):
                self.print_board(reveal=True)
                print("Game Over! You hit a mine.")
                break

            if self.has_won():
                self.print_board(reveal=True)
                print("Congratulations! You've won the game.")
                break


if __name__ == "__main__":
    game = Minesweeper()
    game.play()

