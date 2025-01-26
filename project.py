import random
import os
import time

class MazeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = self.generate_maze()
        self.player_pos = [1, 1]
        self.exit_pos = [height - 2, width - 2]
        self.start_time = None

    def generate_maze(self):
        maze = [["#" for _ in range(self.width)] for _ in range(self.height)]
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                maze[y][x] = " " if random.randint(0, 3) > 0 else "#"
        maze[1][1] = " "
        maze[self.height - 2][self.width - 2] = " "
        return maze

    def display_maze(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if [y, x] == self.player_pos:
                    print("P", end="")
                elif [y, x] == self.exit_pos:
                    print("E", end="")
                else:
                    print(cell, end="")
            print()

    def move_player(self, direction):
        moves = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
        if direction in moves:
            dy, dx = moves[direction]
            new_y = self.player_pos[0] + dy
            new_x = self.player_pos[1] + dx
            if 0 <= new_y < self.height and 0 <= new_x < self.width and self.maze[new_y][new_x] == " ":
                self.player_pos = [new_y, new_x]

    def play(self):
        self.start_time = time.time()
        while self.player_pos != self.exit_pos:
            self.display_maze()
            move = input("Move (WASD): ").lower()
            self.move_player(move)
        elapsed_time = time.time() - self.start_time
        print(f"\nYou found the exit in {elapsed_time:.2f} seconds!")

if __name__ == "__main__":
    game = MazeGame(width=20, height=15)
    game.play()
